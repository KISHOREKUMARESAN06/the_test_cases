from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pack.base__page import WebElementActions


pricing_xpath = '//a[@href="/pricing"]'
pricing_page_url = 'https://saucelabs.com/pricing'


class About(WebElementActions):

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # pricing page open method
    def click_pricing_text(self):
        WebElementActions.click_element(By.XPATH, pricing_xpath)


