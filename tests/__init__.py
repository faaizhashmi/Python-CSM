import unittest
from selenium import webdriver
from lib.utils.urls import Url

from webdriver_manager.chrome import ChromeDriverManager

class Init(unittest.TestCase):
    @classmethod
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(Url.CHROME_PATH, options=options)
        # self.driver= webdriver.Chrome(ChromeDriverManager().install())

        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get(Url.HOME_URL)

    @classmethod
    def tearDown(self):
       self.driver.close()
       self.driver.quit()