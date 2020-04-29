from random import *
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def wait_xpath_sendkey(driver,xpath):
    return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def wait_id_sendkey(driver, id):
    return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, id)))

def wait_name_sendkey(driver,name):
    return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, name)))

def wait_xpath_click(driver,xpath):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))

def wait_id_click(driver,id):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, id)))

def human_wise():
    sleep(randint(2, 4))

def generate_nricfin(first='S', age=-1):
    if first != 'S' and first != 'T' and first != 'F' and first != 'G':
        return

    if not (age >= -1 and age <= 9):
        age = -1

    chars = list(str(randint(0, 9999999)).zfill(7))

    if age != -1: chars[0] = age
    output = first + ''.join(chars)

    chars[0] = str(int(chars[0]) * 2)
    chars[1] = str(int(chars[1]) * 7)
    chars[2] = str(int(chars[2]) * 6)
    chars[3] = str(int(chars[3]) * 5)
    chars[4] = str(int(chars[4]) * 4)
    chars[5] = str(int(chars[5]) * 3)
    chars[6] = str(int(chars[6]) * 2)

    sum = 0
    for i in range(7):
        sum += int(chars[i])

    offset = 4 if (first == "T" or first == "G") else 0
    temp = (offset + sum) % 11
    st = ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    fg = ["X", "W", "U", "T", "R", "Q", "P", "N", "M", "L", "K"]

    if first == "S" or first == "T":
        alpha = st[temp]
    elif first == "F" or first == "G":
        alpha = fg[temp]
    else:
        alpha = "?"
    nric = output + alpha
    write_to_file(nric, '/tmp/aQA/nricfin')
    return nric

def generate_email():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    name = ""
    for i in range(6):
        name = name + choice(letters)
    email = name + '@' + 'gigacover.com'
    write_to_file(email, '/tmp/aQA/email')
    return email

def write_to_file(name, path):
    with open(path, "w") as file:
        file.write(name)

def read_file(path):
    with open(path, "r") as file:
        return file.read()

def input_infomation(driver):
    generate_email()
    first_name = wait_name_sendkey(driver,'first_name')
    first_name.send_keys('trang')

    last_name = wait_name_sendkey(driver,'last_name')
    last_name.send_keys('truong')

    nric = generate_nricfin()
    nricfin = wait_name_sendkey(driver,'nricfin')
    nricfin.send_keys(nric)

    postalcode = wait_name_sendkey(driver,'postalcode')
    postalcode.send_keys('123456')

    email = wait_name_sendkey(driver,'email')
    email.send_keys(read_file('/tmp/aQA/email'))

    mobile = wait_name_sendkey(driver,'mobile')
    mobile.send_keys('84654321')

    confirm_checkbox = driver.find_element_by_id('headless-checkbox-confirm-info')
    confirm_checkbox.click()

    required_checkbox = driver.find_element_by_id('headless-checkbox-required')
    required_checkbox.click()

    checkout_btn = wait_id_click(driver,'headless-proceed-checkout-button')
    checkout_btn.click()

def checkout(driver,id):
    proceed_btn = wait_id_click(driver,id)
    proceed_btn.click()

    human_wise()
    iframe = wait_xpath_click(driver,'//iframe[@name="stripe_checkout_app"]')
    driver.switch_to.frame(iframe)

    card_number = wait_xpath_sendkey(driver,'//input[@placeholder="Card number"]')
    card_number.send_keys('4242424242424242')

    card_date = wait_xpath_sendkey(driver,'//input[@placeholder="MM / YY"]')
    card_date.send_keys('1122')

    card_cvc = wait_xpath_sendkey(driver,'//input[@placeholder="CVC"]')
    card_cvc.send_keys('933')

    zip_code = wait_xpath_sendkey(driver,'//input[@placeholder="ZIP Code"]')
    zip_code.send_keys('123456')

    pay_btn = wait_xpath_click(driver,'//*[contains(@class,"Section-button")]//button')
    pay_btn.click()

def flep_range(r):
    if r == 'range1':
        r = '1995-07-01'
    elif r == 'range4':
        r = '1965-07-01'
    elif r == 'range5':
        r ='1962-07-01'
    else:
        r = '1958-07-01'
    return r

def flip_plan(p):
    if p == 'basic':
        p = '//h2[contains(@class,"text-center")and(text()="BASIC")]/../..//button'
    elif p == 'enhance':
        p = '//h2[contains(@class,"text-center")and(text()="ENHANCED")]/../..//button'
    else:
        p = '//h2[contains(@class,"text-center")and(text()="PREMIUM")]/../..//button'
    return p

def flip_unit(u):
    if u == 'weekly':
        u = '(//*[@class="payment-option-flip"])[1]//button'
    elif u == 'monthly':
        u = '(//*[@class="payment-option-flip"])[2]//button'
    else:
        u = '(//*[@class="payment-option-flip"])[3]//button'
    return u

