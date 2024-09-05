from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pack.base__page import WebElementActions


live_test = '//div[@aria-controls=":r1:"]'
virtual_cloud = '//div[@aria-controls=":r2:"]'
real_device_cloud = '//div[@aria-controls=":r3:"]'
dd_option_select = '//li[@data-value="5"]'
live_testing_xpath = '//h3[@class="MuiTypography-root MuiTypography-h5 css-122wcbh"]'
row1_id = ":r1:"
row2_id = ":r2:"
row3_id = ":r3:"

class Pricing(WebElementActions):

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # using scroll method for live testing text visible
    def using_scroll(self):
        WebElementActions.scroll_where(By.XPATH, live_testing_xpath)

    # select the Live Testing Parallel Tests
    def live_testing_platform(self):
        WebElementActions.click_element(By.XPATH, live_test)
        WebElementActions.click_element(By.XPATH, dd_option_select)

    # select the Virtual Cloud Parallel Tests
    def virtual_cloud_platform(self):
        WebElementActions.click_element(By.XPATH, virtual_cloud)
        WebElementActions.click_element(By.XPATH, dd_option_select)

    # select the Real Device Cloud Parallel Tests
    def Real_Device_Cloud_platform(self):
        WebElementActions.click_element(By.XPATH, check_price)
        WebElementActions.click_element(By.XPATH, dd_option_select)

    # click the get start btn
    def get_start_btn(self):
        ele = WebElementActions.click_elements(By.XPATH, '//button[text()="Get started"]')
        print(len(ele))
        get_srt = ele[1].text()
        get_srt.click()


