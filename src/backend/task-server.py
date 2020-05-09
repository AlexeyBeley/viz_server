# -*- coding: utf-8 -*-
"""
Exam server
"""

import falcon
import json
import logging

class HandleRequest(object):
    def on_get(self, req, resp):
        raw_data = req.bounded_stream.read()
        logging.debug(raw_data.decode("utf-8"))
        resp.body = json.dumps({'Status': 'OK'})
        resp.status = falcon.HTTP_200

app = falcon.API()

app.add_route('/abracadabra', HandleRequest())

# Useful for debugging problems in API, it works with pdb
if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()

#test
#curl -i -H 'Content-Type: application/json' http://127.0.0.1:8000/abracadabra


