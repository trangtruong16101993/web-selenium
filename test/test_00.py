import unittest

from src.config import WEBDRIVER_REMOTE_HUB
from src.service.selenium_.snapshot_debug import takeSnapshot
from src.service.selenium_.webdriver import loadWebDriver, wait4VisibleXPath
from src.service.selenium_.window_size import WindowSize


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):
        self.wd = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)

    def tearDown(self): pass  # nothing here for now


    def test_apkathon2019_homepage(self):
        url = 'https://release.gigacover.com/flip'
        self.wd.get(url)
        title = self.wd.title
        assert title =='Flexible Group Benefits'

