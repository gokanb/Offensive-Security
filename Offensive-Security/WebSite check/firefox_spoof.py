#!/usr/bin/python
#Author: Gokan Bektas
#Description: This application will spoof the browser cookies as given browser. 

import urllib.request
import urllib.error
import urllib.parse

BROWSER = 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0'
URL = 'http://www.python.org'

def firefox_spoof():
    
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', BROWSER)]
    result = opener.open(URL)
    print("Response headers: ")
    
    for header in result.headers:
        print(f'{header}: {result.headers.get(header)}')
        
if __name__ == '__main__':
    firefox_spoof()