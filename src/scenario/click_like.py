from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

from src.service.selenium_.snapshot_debug import *
from src.service.selenium_.webdriver import *
from src.service.selenium_.window_size import *
from src.config import WEBDRIVER_REMOTE_HUB

url = 'https://www.youtube.com/watch?v=Z_VRZ8RBpkg'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(25)
like_btn = driver.find_element_by_xpath('//*[@id="button"]')
ActionChains(driver).move_to_element(like_btn)
like_btn.click()
