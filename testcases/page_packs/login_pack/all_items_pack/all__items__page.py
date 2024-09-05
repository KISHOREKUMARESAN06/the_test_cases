from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pack.base__page import WebElementActions


menu_id = "react-burger-menu-btn"
# menu_xpath = '//button[@id="react-burger-menu-btn"]'
about_id = "about_sidebar_link"
# about_xpath = '//a[@id="about_sidebar_link"]'
back_bag = '//button[@id="add-to-cart-sauce-labs-backpack"]'
bike_light = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
bolt_tshirt = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
fleece_jacket = '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]'
one_side = '//button[@id="add-to-cart-sauce-labs-onesie"]'
t_shirt_red = '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'
cart_link = '//a[@class="shopping_cart_link"]'
DD = '//select[@class="product_sort_container"]'
twitter = '//a[@data-test="social-twitter"]'
facebook = '//a[@data-test="social-facebook"]'
linkedin = '//a[@data-test="social-linkedin"]'


class All_items(WebElementActions):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # click menu for options
    def click_the_menu(self):
        WebElementActions.click_element(By.ID, menu_id)
        # WebElementActions.click_element(By.XPATH, menu_xpath)

    # select the about option
    def select_about(self):
        WebElementActions.click_element(By.ID, about_id)

    # select Backpack
    def select_Sauce_Labs_Backpack(self):
        WebElementActions.click_element(By.XPATH, back_bag)

    # select Bike_Light
    def select_Sauce_Labs_Bike_Light(self):
        WebElementActions.click_element(By.XPATH, bike_light)

    # select Bolt_T_Shirt
    def select_Sauce_Labs_Bolt_T_Shirt(self):
        WebElementActions.click_element(By.XPATH, bolt_tshirt)

    # select Fleece_Jacket
    def select_Sauce_Labs_Fleece_Jacket(self):
        WebElementActions.click_element(By.XPATH, fleece_jacket)

    # select Onesie
    def select_Sauce_Labs_Onesie(self):
        WebElementActions.click_element(By.XPATH, one_side)

    # select T_Shirt_Red
    def select_Test_allTheThings_T_Shirt_Red(self):
        WebElementActions.click_element(By.XPATH, t_shirt_red)

    # click cart link on top right
    def click_cart_link(self):
        WebElementActions.click_element(By.XPATH, cart_link)

    # select Z_to_A drop down
    def select_Z_to_A(self):
        WebElementActions.select_drop_down_visible_text(By.XPATH, DD, "Name (Z to A)")

    # select low_to_high drop down
    def select_low_to_high(self):
        WebElementActions.select_drop_down_visible_text(By.XPATH, DD, "Price (low to high)")

    # select high_to_low drop down
    def select_high_to_low(self):
        WebElementActions.select_drop_down_visible_text(By.XPATH, DD, "Price (high to low)")

    # select A_to_Z drop down
    def select_A_to_Z(self):
        WebElementActions.select_drop_down_visible_text(By.XPATH, DD, "Name (A to Z)")

    # (Social media methods)
    # twitter
    def click_twitter_logo(self):
        WebElementActions.click_element(By.XPATH, twitter)
    # facebook
    def click_facebook_logo(self):
        WebElementActions.click_element(By.XPATH, facebook)
    # linkedin
    def clcik_linkedin_logo(self):
        WebElementActions.click_element(By.XPATH, linkedin)

