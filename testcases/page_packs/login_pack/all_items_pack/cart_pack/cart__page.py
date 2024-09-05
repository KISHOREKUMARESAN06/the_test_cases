from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pack.base__page import WebElementActions


cont_shop_id = 'continue-shopping'
checkout_btn_id = 'checkout'
cart_icon = '//a[@class="shopping_cart_link"]'


class Cart(WebElementActions):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # clicking cart icon for what are the products selected
    def click_cart_icon(self):
        WebElementActions.click_element(By.XPATH, cart_icon)

    # click the shopping btn
    def click_shopping_button(self):
        WebElementActions.click_element(By.ID, cont_shop_id)

    # click the checkout btn
    def click_checkout_button(self):
        WebElementActions.click_element(By.ID, checkout_btn_id)