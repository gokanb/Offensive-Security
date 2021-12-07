#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 


import argparse
from data_download.HTTPClient import HTTPClient

REMOTE_SERVER_HOST = 'http://www.cnn.com'

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Client Example')
    parser.add_argument('--host', action="store", dest="host", default=REMOTE_SERVER_HOST)
    
    given_args = parser.parse_args()
    host = given_args.host
    client = HTTPClient(host)
    print (client.fetch())