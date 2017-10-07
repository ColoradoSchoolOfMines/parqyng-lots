import json
from http.client import HTTPConnection
import os.path

class Node:
    def __init__(self, cfg):
        self.cfg = cfg
        self.enter = 0
        self.exit = 0
        self.con = HTTPConnection(self.cfg['server'])

    def delta(self, delta):
        if delta < 0:
            self.exit += -delta
        else:
            self.enter += delta

    def send_report(self):
        self.con.request('POST', '/report', json.dumps({
            'key': self.cfg['key'],
            'enter': self.enter,
            'exit': self.exit,
        }))
        res = self.con.getresponse()
        assert res.code == 200

        self.enter = 0
        self.exit = 0

    def retrieve(self):
        self.con.request('GET', '/node/{}'.format(self.cfg['key']))
        res = self.con.getresponse()
        assert res.code == 200
        return json.load(res)

def connect(**kwargs):
    loaded = json.load(open('config.json'))
    cfg = {**loaded, **kwargs}

    do_lock = cfg.get('lock')
    do_lock = (do_lock is None or do_lock)
    if do_lock and os.path.isfile('lock.json'):
        cfg = {**json.load(open('lock.json')), **cfg}

    key = cfg.get('key')
    if key is None:
        con = HTTPConnection(cfg['server'])
        lot = cfg.get('lot')
        if lot:
            con.request('GET', '/register?lot={}'.format(lot))
        else:
            con.request('GET', '/register')
        res = con.getresponse()
        assert res.code == 200

        new = json.load(res)
        if do_lock:
            json.dump(new, open('lock.json', 'w'))
        cfg = {**new, **loaded, **kwargs}

    return Node(cfg)
