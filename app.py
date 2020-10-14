import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Search(unittest.TestCase):

    def setUp(self):
        chrome_options = Options() 
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)

    def test_search_in_url(self):
        driver = self.driver
        driver.get("http://www.repubblica.it/")
        self.assertIn("Covid", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
