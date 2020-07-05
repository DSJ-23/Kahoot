from selenium import webdriver
import requests
import json
import time
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()
email = os.getenv('email')
passw = os.getenv('pass')

browser = webdriver.Chrome("./chromedriver")

def set_up():
    browser.get("https://kahoot.com/")
    browser.find_element_by_id('menu-item-8410').click()
    time.sleep(0.2)
    login()

def login():
    browser.find_element_by_id('username').send_keys(email)
    browser.find_element_by_id('password').send_keys(passw)
    browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/form/button').click()
    create()

def create():
    time.sleep(1)
    browser.find_element_by_css_selector("#root > div > div.base-top-bar__TopBarSpacer-sc-1jin4gl-2.jwQUBu > header > nav > div.top-bar__ContentWrapper-sc-1fshj0y-0.dAfnjM > div.actions__Actions-sc-1g1mwpd-0.gTXwGH > button.button__Button-c6mvr2-0.edYoF.actions__PrimaryButton-sc-1g1mwpd-1.hQEoOx").click()
    # browser.find_element_by_class_name("button__Button-c6mvr2-0").click()
    # browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/header/nav/div[2]/div[2]/button[2]/span').click()
    time.sleep(3)

set_up()


open_trivia_db = requests.get("https://opentdb.com/api.php?amount=10").json()


def quit():
    browser.quit()

quit()


def print_all_questions(response_object):
    for question in response_object['results']:
        print(question)


# print_all_questions(open_trivia_db)




# Version 83.0.4103.116 

# https://kahoot.com/

# eg = requests.get("https://jsonplaceholder.typicode.com/todos/1").json()
# print(eg)
# print(eg['userId'])


# x = requests.get('https://w3schools.com')
# print(x.status_code)


# import requests

# x = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# print(x)