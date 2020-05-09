# -*- coding: utf-8 -*-
"""
Exam server
"""

import falcon
import json
import logging

logger = logging.getLogger('Backend_App')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

class HandleRequest(object):
    def on_get(self, req, resp):
        raw_data = req.bounded_stream.read()
        logger.debug(raw_data.decode("utf-8"))
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


