from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pack.base__page import WebElementActions


class Login(WebElementActions):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # login method
    def method_login(self, username, password):

        # Entering username
        WebElementActions.send_keys_to_element(By.ID, 'user-name', username)
        # Entering password
        WebElementActions.send_keys_to_element(By.ID, 'password', password)
        # Clicking login button
        WebElementActions.click_element(By.ID, 'login-button')
        # accept the alert
        WebElementActions.handle_alert_if_present()

    # logout method
    def method_logout(self):

        # Clicking logout button
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))) #logout_sidebar_link

        # WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout'))) #Logout

