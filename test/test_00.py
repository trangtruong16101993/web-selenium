import unittest
from time import sleep
from webdriver import *

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now

class Test(unittest.TestCase):

    def setUp(self):
        self.wd = loadWebDriver_firefox()
        self.wd.implicitly_wait(10)

    def tearDown(self): self.wd.quit()

    def test_apkathon2019_homepage(self):
        url = 'https://release.gigacover.com/flip'
        self.wd.get(url)
        title = self.wd.title
        assert title =='Flexible Group Benefits'
        self.wd.save_screenshot('a.png')

    def test_legend(self):
        url = 'https://champion.gg/statistics/'
        self.wd.get(url)
        list_ad = self.wd.find_elements_by_xpath("//tr[contains(@class, 'ng-scope')]/td[(text()='ADC')]/..")
        list = []
        for i in list_ad:
            ad = i.text
            list.append(float((ad.split(' ')[2]).split('%')[0]))

        list = sorted(list, reverse=True)
        print(list)
