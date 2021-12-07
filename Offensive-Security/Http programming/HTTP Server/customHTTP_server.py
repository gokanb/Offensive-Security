#!/ur/bin/env python

from request_handler import RequestHandler
from http.server import HTTPServer

class CustomHTTPServer(HTTPServer):
    "A custom HTTP server"
    def __init__(self, host, port):
        server_address = (host, port)
        HTTPServer.__init__(self, server_address, RequestHandler)
