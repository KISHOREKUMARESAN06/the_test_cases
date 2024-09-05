from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pack.base__page import WebElementActions


finish_btn_id = "finish"
back_home = '//button[@id="back-to-products"]'

class Overview(WebElementActions):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # click cancel btn
    def click_cancel(self):
        WebElementActions.click_element(By.ID, cancel_id)

    # click the finish btn
    def finish_btn(self):
        WebElementActions.click_element(By.ID, finish_btn_id)
        WebElementActions.click_element(By.XPATH, back_home)

