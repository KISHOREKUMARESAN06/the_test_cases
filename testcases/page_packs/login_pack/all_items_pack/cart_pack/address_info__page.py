from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pack.base__page import WebElementActions

first_name_id = 'first-name'
last_name_id = 'last-name'
zip_code_id = 'postal-code'
continue_btn_id = 'continue'
cancel_id = 'cancel'

class AddInfo(WebElementActions):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # filling address form
    def fill_the_address(self, firstname, lastname, zipcode):
        # first name
        WebElementActions.send_keys_to_element(By.ID, first_name_id, firstname)
        # last name
        WebElementActions.send_keys_to_element(By.ID, last_name_id, lastname)
        # zip code
        WebElementActions.send_keys_to_element(By.ID, zip_code_id, zipcode)
        # press continue btn
        WebElementActions.click_element()(By.ID, continue_btn_id)


    # click cancel btn
    def click_cancel(self):
        WebElementActions.click_element(By.ID, cancel_id)
