import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.paodeacucar.com/')
content = response.content
print('Status code:', response.status_code)
print('↓↓ Header ↓↓')
print(response.headers)
print('\n↓↓ Content ↓↓')
print(response.content)
site = BeautifulSoup(content,'html.parser')
print (type(site))
