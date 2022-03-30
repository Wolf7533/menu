import requests
print('                Get fast information             ')
print('oOo------------IP INFORMATION SERVICE------------oOo')
print('                   check ip info              ')
ip = input('Please enter a target IP:')
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



