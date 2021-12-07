#!/ur/bin/env python

import argparse
import sys
from customHTTP_server import CustomHTTPServer
from request_handler import RequestHandler

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8800

def run_server(port):
    try:
        server = CustomHTTPServer(DEFAULT_HOST, port)
        print(f'Custom HTTP server started on port: {port}')
        server.serve_forever()

    except Exception as err:
        print (f'Error: {err}')

    except KeyboardInterrupt:
        print("Server interrupted and is shutting down...")
        server.socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple HTTP server")
    parser.add_argument('--port', action="store", dest="port", type=int, default=DEFAULT_PORT)
    given_args = parser.parse_args()
    port = given_args.port
    run_server(port)