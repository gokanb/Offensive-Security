#!/ur/bin/env python

from http.server import BaseHTTPRequestHandler #importing from server 

class RequestHandler(BaseHTTPRequestHandler):  #creating class 
    """Custom request handler"""

    def do_GET(self):                          #create function get requests and writes a file.
        """Handler for the Get requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #send the message to browser
        self.wfile.write("Hello from server!")
        return