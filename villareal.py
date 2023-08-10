import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://www.villarrealonline.com.br/')
content = response.read()

print('Status code:', response.getcode())
print('↓↓ Header ↓↓')
print(response.headers)
print('\n↓↓ Content ↓↓')
#print(content)
site: BeautifulSoup = BeautifulSoup(content, 'html.parser')
#print (type(site))

#title = site.find_all("div", class_="product-cardstyles__Container-sc-1uwpde0-1 hNTkow")
items = site.find_all('div')
for item in items:
	#print(type(item))
	value = item.get('class')
	if not value:
		continue
	print(value)
	if 'border-promotion' == item.get('class'):
		print(item)
		print('-------------------------------------------------------')
