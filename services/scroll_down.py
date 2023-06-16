from time import sleep
def scroll_down(browser):
    height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == height:
            break
        height = new_height