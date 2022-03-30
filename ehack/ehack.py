import requests
print('######       #     #    #    ######  #   #')
print('#            #     #   # #   #       #  #')
print('#            #     #  #   #  #       # #')
print('####    ###  #######  #####  #       ##')
print('#            #     #  #   #  #       # #')
print('#            #     #  #   #  #       #  #')
print('######       #     #  #   #  ######  #   #')
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
#Lets test what headers are sent by sending a request to HTTPBin
to = input('Enter target e-mail (example: anonymous@example.com):')
subject = input('Enter subject:')
msg = input('Enter message:')
send = input('From (example: ehack@python.scr):')
requests.post(url=f'https://hoster7533.000webhostapp.com/sendmail.php',headers=headers,data={'to':to,'sb':subject,'msg':msg,'from':send})
print('[!] Message send [!]')
print('[!] E-Hack Python Script [!]')
