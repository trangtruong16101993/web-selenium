from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
load_dotenv()

def loadWebDriver_chrome():
    driver = webdriver.Remote(
        command_executor=os.environ.get('CHROME'),
        desired_capabilities=DesiredCapabilities.CHROME,
    )
    driver.implicitly_wait(10)
    return driver

def loadWebDriver_firefox():
    driver = webdriver.Remote(
        command_executor=os.environ.get('FIREFOX'),
        desired_capabilities=DesiredCapabilities.FIREFOX,
    )
    driver.implicitly_wait(10)
    return driver

def loadWebDriver_opera():
    driver = webdriver.Remote(
        command_executor=os.environ.get('OPERA'),
        desired_capabilities=DesiredCapabilities.OPERA,
    )
    driver.implicitly_wait(10)
    return driver
