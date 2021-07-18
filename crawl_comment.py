import random
from time import sleep

from selenium import webdriver


def click_link(browser, id=None, xpath=None):
    # scroll down to last of page to load all data in web
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if (id != None):
        link = browser.find_element_by_id(id)
    else:
        link = browser.find_element_by_xpath(xpath)
    link.click()
    sleep(random.randint(5, 10))


def get_comment_in_post(url):
    browser = webdriver.Chrome("chromedriver.exe")

    browser.get(url)
    sleep(random.randint(10, 11))

    click_link(browser, id="expanding_cta_close_button")
    click_link(browser,
               xpath="/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
    click_link(browser,
               xpath="/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/div/div/div/a")
    click_link(browser, xpath="/html/body/div[1]/div[3]/div[3]/div/div/div/ul/li[3]/a")

    while True:
        try:
            click_link(browser,
                       xpath="/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a/div/span")
        except:
            print("Already load all comment!")
            break

    comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
    content_list = []

    print("Comment: ")
    for comment in comment_list:
        try:
            content = comment.find_element_by_class_name("_3l3x").text
            print(content)
            content_list.append(content)
        except:
            continue

    sleep(10)
    browser.close()

    return content_list

# get_comment_in_post(r"https://www.facebook.com/baobongda24h.net/posts/2050600804955470?__tn__=-R")
