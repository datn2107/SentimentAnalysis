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

    # try:
    click_link(browser, id="expanding_cta_close_button")
    print("version 1")
    open_comment_link = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a"
    open_all_comment_table_link = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/div/div/div/a"
    select_all_comment_option = "/html/body/div[1]/div[3]/div[3]/div/div/div/ul/li[3]/a"
    expand_comment_link = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a/div/span"
    # except:
    #     print("version 2")
    #     open_comment_link = "/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a"
    #     open_all_comment_table_link = "/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/div/div/div/a"
    #     select_all_comment_option = "/html/body/div[1]/div[3]/div[3]/div/div/div/ul/li[3]/a"
    #     expand_comment_link = "/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a/div/span"

    # print(open_comment_link)
    click_link(browser, xpath=open_comment_link)
    click_link(browser, xpath=open_all_comment_table_link)
    click_link(browser, xpath=select_all_comment_option)

    while True:
        try:
            click_link(browser, xpath=expand_comment_link)
        except:
            print("Already load all comment!")
            break

    comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
    content_list = []

    for comment in comment_list:
        try:
            comment.find_element_by_class_name("_5v47").click()
        except:
            pass
        try:
            content = comment.find_element_by_class_name("_3l3x").text
            content_list.append(content)
        except:
            continue

    sleep(10)
    browser.close()

    return content_list

# get_comment_in_post(r"https://www.facebook.com/windows/posts/10158599769677669")

