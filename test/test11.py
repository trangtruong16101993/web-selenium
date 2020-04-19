from time import sleep

from selenium import webdriver
from src.config import WEBDRIVER_REMOTE_HUB
from src.service.selenium_.snapshot_debug import takeSnapshot
from src.service.selenium_.webdriver import loadWebDriver, wait4VisibleXPath
from src.service.selenium_.window_size import WindowSize


driver = webdriver.Chrome(executable_path="/Users/trangtruong/Desktop/web-selenium/chromedriver")
driver.implicitly_wait(10)

url = 'https://release.gigacover.com/'

driver.get(url)
c = driver.find_elements_by_xpath("//a[(text()='Income Protection')]").click()
