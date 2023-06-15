from selenium.webdriver.common.by import By

def create_dict(browser):
    num = 1
    d = dict()
    casas = browser.find_elements(By.PARTIAL_LINK_TEXT, 'S/')
    for casa in casas:
        d[num] = {}
        link = casa.get_attribute('href')
        casa = casa.text.split('\n')
        if len(casa) == 3 and 'Trujillo' in casa[2]:
            d[num]['price'] = casa[0]
            d[num]['comment'] = casa[1]
            d[num]['place'] = casa[2]
            d[num]['link'] = link
            num += 1
    return d





#count = 1
#for c in casa:
#    flat = c.text.split('\n')
#    link = c.get_attribute('href')
#    casa_dict[count] = {}
#    casa_dict[count]['link'] = link
#    if len(flat) == 3:
#        if 'Trujillo' in flat[2]:
#            for element in flat:
#                casa_dict[count]['price'] = flat[0]
#                casa_dict[count]['comment'] = flat[1]
#                casa_dict[count]['place'] = flat[2]
#            count += 1