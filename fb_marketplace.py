from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from services.scroll_down import scroll_down
from  services.create_dept_dict import create_dict

url = 'https://www.facebook.com/marketplace/trujillo/apartments-for-rent?minPrice=500&maxPrice=3000&sortBy=best_match&exact=true'
options = ChromeOptions()
options.add_argument('--headless')
bro = Chrome(options=options)
bro.get(url)
sleep(4)

scroll_down(bro)
sleep(2)

rent_dict = create_dict(bro)

for n, desc in rent_dict.items():
    print(str(n) + ' : ' + str(desc))

