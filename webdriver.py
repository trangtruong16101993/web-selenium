import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

filepath = os.path.dirname(__file__)

def options():
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs',  {
        "download.default_directory": f'{filepath}/venta/pdf_file',
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
        })

    return chrome_options

def wd():
    chrome_driver = f'{filepath}/chromedriver'
    driver = webdriver.Chrome(options=options(), executable_path=chrome_driver)
    driver.implicitly_wait(10)
    return driver
