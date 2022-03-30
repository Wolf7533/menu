import requests
import socket
print('____________________________________________________________')
print('|                      Python script                       |')
print('|                                                          |')
print('|   .oOo.------------.[ Host Info ].------------.oOo.      |')
print('|                                                          |')
print('|                  Example: example.com                    |')
print('|                                                          |')
print('|   .oOo.------------.[ Host Info ].------------.oOo.      |')
print('|__________________________________________________________|')
host = input('Please enter a target URL:')
ip = socket.gethostbyname(host)
response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
print('[IP]:', response.get('query'),"\n",
'[Int prov]:', response.get('isp'),"\n",
'[Org]:', response.get('org'),"\n"
'[Country]:',response.get('city'),"\n",
'[Region Name]:', response.get('regionName'),"\n",
'[City]:', response.get('city'),"\n",
'[ZIP]:', response.get('zip'),"\n",
'[Lat]:', response.get('lat'),"\n",
'[Lon]:',response.get('lon'),)
print("[!] HOST INFORMATION [!]");

