from util.util import *
from pathlib import Path

Path("/tmp/aQA").mkdir(parents=True, exist_ok=True)

url=f'https://release.gigacover.com'

def plan(driver, plan):
    driver.get(url)

    wait_xpath_click(driver, "//a[(text()='Income Protection')]").click()
    human_wise()

    driver.execute_script("window.scrollTo(0,1200);")

    human_wise()
    plan =  wait_xpath_click(driver, plan)
    plan.click()

def get_quote_now(driver):
    brith_day = wait_xpath_sendkey(driver, '//*[div[text()="Birthday"]]//input')
    brith_day.clear()
    brith_day.send_keys('1990-10-16')

    policy_start = wait_xpath_sendkey(driver, '//*[div/label[text()="Policy Start"]]//input')
    policy_start_date = policy_start.get_attribute('value')
    write_to_file(policy_start_date, '/tmp/aQA/policy_start')

    occupations = wait_xpath_click(driver, '//*[text()="Please select all relevant work that you do"]/following-sibling::div/div[8]')
    occupations.click()

    driver.execute_script("window.scrollTo(0,1000);")

    submit_btn = wait_xpath_click(driver, '//*[@class="col-sm-4 hidden-xs hidden-sm"]//span[text()="Show me my quote"]')
    submit_btn.click()

    driver.execute_script("window.scrollTo(0,0);")

def unit(driver, unit):
    unit = wait_xpath_click(driver, unit)
    unit.click()

def submit(driver):
    check_box = driver.find_element_by_id('headless-checkbox-daily_benefit')
    check_box.click()

    proceed_btn = wait_id_click(driver, 'headless-proceed-info-button')
    proceed_btn.click()

def buy(driver, p, u):
    plan(driver, p)
    get_quote_now(driver)
    unit(driver, u)
    submit(driver)
    input_infomation(driver)
    checkout(driver, 'headless-proceed-payment-button')

