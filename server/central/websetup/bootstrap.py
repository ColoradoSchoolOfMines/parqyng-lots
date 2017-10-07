# -*- coding: utf-8 -*-
"""Setup the central application"""
from __future__ import print_function, unicode_literals
import transaction
from central import model


def bootstrap(command, conf, vars):
    """Place any commands to setup central here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        u = model.User()
        u.user_name = 'admin'
        u.display_name = 'Ad Min'
        u.email_address = 'admin@example.com'
        u.password = 'password'

        model.DBSession.add(u)

        g = model.Group()
        g.group_name = 'admin'
        g.display_name = 'Admin Group'

        g.users.append(u)

        model.DBSession.add(g)

        p = model.Permission()
        p.permission_name = 'admin'
        p.description = 'This permission gives an administrative right'
        p.groups.append(g)

        model.DBSession.add(p)

        l = model.Lot()
        l.name = 'Empty Lot'
        model.DBSession.add(l)

        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your auth data, '
              'it may have already been added:')
        import traceback
        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')

    # <websetup.bootstrap.after.auth>
