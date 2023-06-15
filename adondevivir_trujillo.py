from bs4 import BeautifulSoup as bs
from selenium.webdriver import Chrome
from time import sleep

casa_list = []
huan = 'https://www.adondevivir.com/departamentos-en-alquiler-en-huanchaco.html'
url = 'https://www.adondevivir.com/departamentos-en-alquiler-en-trujillo-ciudad-de-trujillo-soles.html'
bro = Chrome()

bro.get(huan)
soup = bs(bro.page_source, 'lxml')
sleep(3)
#price = soup.find('div', class_='sc-12dh9kl-4 hbUMaO').text.strip()
#link = 'https://www.adondevivir.com' + soup.find('a', class_='sc-i1odl-11').get('href')
deps = soup.findAll('div', class_="sc-i1odl-2")
for d in deps:
    price = d.find('div', class_='sc-12dh9kl-4').text.strip()
    link = 'https://www.adondevivir.com' + d.find('a', class_='sc-i1odl-11').get('href')
    address = d.find('div', class_='jneaYd').text.strip()
    size = d.find('div', class_ = 'eodGhu').text.strip()

    casa_list.append([address, price, size, link])

for c in casa_list:
    print(*c)



