# -*- coding: utf-8 -*-
"""
Exam server
"""

import falcon
import json
import logging

class HandleRequest(object):
    def on_post(self, req, resp):
        raw_json = req.bounded_stream.read()
        obj = json.loads(raw_json.decode("utf-8"))
        logging.debug(obj)
        if 'jackPot' in obj:
            resp.body = json.dumps({'Status': 'OK'})
        else:
            resp.body = json.dumps({'Status': 'Fail', 'Reason': 'no jackPot'})
        resp.status = falcon.HTTP_200

app = falcon.API()

app.add_route('/abracadabra', HandleRequest())

# Useful for debugging problems in API, it works with pdb
if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()

#success
#curl -i -X POST -H 'Content-Type: application/json' -d '{"jackPot": "winwin"}' http://127.0.0.1:8000/abracadabra

#fail
#curl -i -X POST -H 'Content-Type: application/json' -d '{"jackPot1": "rainwin"}' http://127.0.0.1:8000/abracadabra

