# -*- coding: utf-8 -*-
"""Main Controller"""

import random
from tg import expose, flash, require, url, lurl, abort
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from central import model
from central.controllers.secure import SecureController
from central.model import DBSession
from central.model.lot import Lot
from central.model.node import Node
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from central.lib.base import BaseController
from central.controllers.error import ErrorController

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the central application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "central"

    @expose('central.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('central.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        """Start the user login."""
        if failure is not None:
            if failure == 'user-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)

    @expose('json')
    def register(self, lot=None):
        node = Node(key = random.randint(0, 1<<31))
        node.lot_id = lot
        DBSession.add(node)
        return {
            'key': node.key,
        }

    @expose('json')
    def report(self):
        if request.method == "POST":
            data = request.json
            key = data['key']
            node = DBSession.query(Node).filter(Node.key==key).first()
            if not node:
                abort(404, "no such node")

            delta = int(data.get('enter') or 0) - int(data.get('exit') or 0)
            if node.lot:
                node.lot.cars += delta
                DBSession.add(node.lot)

            return {}
        else:
            abort(405)

    @expose('json')
    def lot(self, lot):
        lot = DBSession.query(Lot).filter(Lot.id==lot).first()
        if lot is not None:
            return {
                'id': lot.id,
                'name': lot.name,
                'cars': lot.cars,
            }
        else:
            abort(404)
