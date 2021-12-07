#!usr/bin/env python

import http.cookiejar
import urllib

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = 'your@email.com'
PASSWORD = 'mypassword'
LOGIN_URL = 'https://bitbucket.org/account/signin/?next=/'
NORMAL_URL = 'https://bitbucket.org'

def extract_cookie_info():
    """Fake login to a site with cookie"""
    
    vart = http.cookiejar.CookieJar()
    login_data = urllib.parse.urlencode({ID_USERNAME : USERNAME, ID_PASSWORD : PASSWORD}).encode("utf-8")
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(vart))
    
    resp = opener.open(LOGIN_URL, login_data)
    
    for cookie in vart:
        print(f'[-]First time cookie: {cookie.name} --> {cookie.value}')
    
    print(f'Headers: {resp.headers}')
    
    #now access without any login info
    resp = opener.open(NORMAL_URL)
    for cookie in vart:
        print(f'[+]Second time cookie: {cookie.name} --> {cookie.value}')
        
    print(f'Headers: {resp.headers}')
    
if __name__ == '__main__':
    extract_cookie_info()
        
