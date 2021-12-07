#!/ur/bin/env python

from http.server import BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    """Custom request handler"""

    def do_GET(self):
        """Handler for the Get requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #send the message to browser
        self.wfile.write("Hello from server!")
        return