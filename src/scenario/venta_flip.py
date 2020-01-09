from time import sleep
from selenium import webdriver
import random
from src.scenario.generate_nric import generate

from selenium.webdriver.common.action_chains import ActionChains

from src.service.selenium_.webdriver import *
from src.service.selenium_.window_size import *
from src.config import WEBDRIVER_REMOTE_HUB

letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l","1","2","3","4","5","6"]
email_value = ''
policy_start_date = ''
driver  = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)
url = 'https://release.gigacover.com/flip'

#region plan
basic = '/html/body/div[1]/main/div[2]/section[1]/div/div[1]/div[1]/div/div[2]/button/span'
enhance = '/html/body/div[1]/main/div[2]/section[1]/div/div[1]/div[2]/div/div[2]/button/span'
premium = '/html/body/div[1]/main/div[2]/section[1]/div/div[1]/div[3]/div/div[2]/button/span'
# endregion

#region unit
weekly = '/html/body/div[1]/main/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[3]/div/div/button'
monthly = '/html/body/div[1]/main/div[2]/div/div[2]/div[4]/div[2]/div[1]/div[3]/div/div/button'
yearly = '/html/body/div[1]/main/div[2]/div/div[2]/div[4]/div[3]/div[1]/div[3]/div/div/button'
# endregion

def get_one_random_email(letters):
    name = ""
    for i in range(7):
        name = name + random.choice(letters)
        email_input = name + '@' + 'gigacover.com'
        global email_value
        email_value = email_input
    return email_input

def plan(plan):
    global policy_start_date
    driver.get(url)
    sleep(3)
    driver.execute_script("window.scrollTo(0,1000);")
    sleep(3)
    plan = driver.find_element_by_xpath(plan)
    plan.click()
    sleep(3)
    brith_day = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/input')
    brith_day.clear()
    brith_day.send_keys('1990-10-16')
    sleep(3)
    policy_start = driver.find_element_by_xpath('//*[@id="page-top"]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/input')
    policy_start_value = policy_start.get_attribute('value')
    policy_start_date = policy_start_value
    occupations = driver.find_element_by_xpath('//*[@id="page-top"]/div[3]/div[2]/div/div[2]/div/div[2]/div[8]/label/span[1]/span[1]/input')
    occupations.click()
    driver.execute_script("window.scrollTo(0,500);")
    submit_btn = driver.find_element_by_xpath('//*[@id="page-top"]/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/button/span')
    submit_btn.click()
    driver.execute_script("window.scrollTo(0,0);")
    sleep(3)

def unit(unit):
    unit = driver.find_element_by_xpath(unit)
    unit.click()

def submit():
    check_box = driver.find_element_by_xpath('//*[@id="headless-checkbox-daily_benefit"]')
    check_box.click()
    proceed_btn = driver.find_element_by_xpath('//*[@id="headless-proceed-info-button"]')
    proceed_btn.click()

def input_infomation():
    get_one_random_email(letters)
    first_name = driver.find_element_by_name('first_name')
    first_name.send_keys('trang')
    last_name = driver.find_element_by_name('last_name')
    last_name.send_keys('truong')
    nricfin = driver.find_element_by_name('nricfin')
    nricfin.send_keys(generate())
    postalcode = driver.find_element_by_name('postalcode')
    postalcode.send_keys('123456')
    email = driver.find_element_by_name('email')
    email.send_keys(email_value)
    mobile = driver.find_element_by_name('mobile')
    mobile.send_keys('84654321')
    confirm_checkbox = driver.find_element_by_id('headless-checkbox-confirm-info')
    confirm_checkbox.click()
    required_checkbox = driver.find_element_by_id('headless-checkbox-required')
    required_checkbox.click()
    checkout_btn = driver.find_element_by_id('headless-proceed-checkout-button')
    checkout_btn.click()

def checkout():
    proceed_btn = driver.find_element_by_id('headless-proceed-payment-button')
    proceed_btn.click()
    sleep(5)
    iframe = driver.find_element_by_xpath("//iframe[@name='stripe_checkout_app']")
    driver.switch_to.frame(iframe)
    card_number = driver.find_element_by_xpath('//input[@placeholder="Card number"]')
    card_number.send_keys('4242424242424242')
    card_date = driver.find_element_by_xpath('//input[@placeholder="MM / YY"]')
    card_date.send_keys('1122')
    card_cvc = driver.find_element_by_xpath('//input[@placeholder="CVC"]')
    card_cvc.send_keys('933')
    zip_code = driver.find_element_by_xpath('//input[@placeholder="ZIP Code"]')
    zip_code.send_keys('123456')
    sleep(3)
    pay_btn = driver.find_element_by_xpath('//*[@id="container"]/section/span[2]/div/div/main/form/nav/div/div/div/button')
    pay_btn.click()
    sleep(10)
    mes = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/section/div/div/div/h2')
    success_msg = mes.text
    driver.save_screenshot("screenshot.png")
    return success_msg

def buy(a, b):
    plan(a)
    unit(b)
    submit()
    input_infomation()
    checkout()
    # driver.quit()

buy(basic, weekly)