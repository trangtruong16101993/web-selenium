import os
import venta_flip
from random import randint
from time import sleep

from src.service.selenium_.webdriver import *
from src.service.selenium_.window_size import *
from src.config import WEBDRIVER_REMOTE_HUB

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

customer_email = venta_flip.email_value
email_to_search = 'developers+' + customer_email
amount = 'S' + venta_flip.total_amount

start_date = venta_flip.policy_start_date


filepath = os.path.dirname(__file__)

driver       = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)

url      = 'https://mail.google.com/'
email    = 'trang.truong@gigacover.com'
password = 'trangtruong'

def human_wise():
    sleep(randint(5, 7))

def login_gmail():
    driver.get(url)
    username_box = driver.find_element_by_id('identifierId'); username_box.send_keys(email)
    u_next_btn = driver.find_element_by_id('identifierNext')

    human_wise()
    ActionChains(driver).move_to_element(u_next_btn)
    u_next_btn.click()

    human_wise()
    password_box = driver.find_element_by_name("password"); password_box.send_keys(password)
    p_next_btn = driver.find_element_by_id('passwordNext')

    human_wise()
    ActionChains(driver).move_to_element(p_next_btn)
    p_next_btn.click()

def search_email():
    human_wise()
    found_email = driver.find_element_by_xpath('//*[@id="gs_lc50"]/input[1]')
    found_email.send_keys(f'to:{email_to_search} subject:(Freelancer Income Protection bill and policy schedule)')

    human_wise()
    found_email.send_keys(Keys.RETURN)

    human_wise()
    email = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div/table/tbody/tr")
    email.click()

def check_info():
    human_wise()
    move = driver.find_element_by_xpath("//*[contains(text(), 'DAILY CASH BENEFIT')]")
    driver.execute_script("arguments[0].scrollIntoView();", move)
    ActionChains(driver).move_to_element(move)
    price = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[3]/div/b[2]/span').text

    policy_start = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[3]/div/b[3]/span').text

    amount_paid = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[3]/div/b[6]/span').text

    if (policy_start == venta_flip.policy_start_date and price == 'S$50' and amount_paid == amount):
        print('PASS')
    else:
        print('FAIL')

login_gmail()
search_email()
check_info()
driver.quit()

