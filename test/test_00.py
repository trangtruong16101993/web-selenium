import unittest
from webdriver_docker import *
from webdriver import *
from main.venta_flip import *

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = loadWebDriver_chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self): self.driver.quit()

    def test_buy_on_venta(self):
        plan(self.driver, '//h2[contains(@class,"text-center")and(text()="BASIC")]/../..//button')
        get_quote_now(self.driver)
        unit(self.driver, '(//*[@class="payment-option-flip"])[1]//button')
        submit(self.driver)
        input_infomation(self.driver)
        checkout(self.driver, 'headless-proceed-payment-button')
        sleep(5)
        success = wait_xpath_sendkey(self.driver, "//*[contains(@class,'success-content')]/h2").is_displayed()
        assert success is True
