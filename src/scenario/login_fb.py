from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from src.service.selenium_.snapshot_debug import *
from src.service.selenium_.webdriver import *
from src.service.selenium_.window_size import *
from src.config import WEBDRIVER_REMOTE_HUB

url = 'https://www.facebook.com/aptechvietnam.hcm'
username = 'vippro56@yahoo.com.vn'
password = 'matkhau1'
wd = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)

def human_wise():
    sleep(randint(3, 6))


def login_fb():
    wd.get(url)
    human_wise()

    #region input username and password into textbox
    username_box = wd.find_element_by_id("email").send_keys(username)
    human_wise()
    password_box = wd.find_element_by_id("pass").send_keys(password)
    human_wise()
    #endregion

    # click login button
    login_btn = wd.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()
    human_wise()

def select_like():
    height = 500
    # select 10 like button
    while True:
        wd.execute_script("window.scrollTo(0,"+ str(height) +");")
        like_btn = wd.find_elements_by_class_name('_666k')
        human_wise()
        random = randint(300, 600)
        height+=random
        if len(like_btn)>=10:
            return like_btn

def like_post():
    select_like()
    like_btn = select_like()
    for i in like_btn:
        ActionChains(wd).move_to_element(i) # move to like button and click
        i.click()
        human_wise()

login_fb()
like_post()
takeSnapshot(wd, printOutcome=True, suffix='snap0', forceSnapshot=True)

