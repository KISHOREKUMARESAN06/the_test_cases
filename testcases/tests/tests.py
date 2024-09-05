import pytest
from selenium import webdriver
from base_pack.base__page import WebElementActions
from page_pack.login__page import Login
from page_pack.login_pack.all__items__page import All_items
from page_pack.login_pack.all_items_pack.cart_pack.cart__page import Cart
from page_pack.login_pack.all_items_pack.cart_pack.address_info__page import AddInfo
from page_pack.login_pack.all_items_pack.cart_pack.overview__page import Overview
from page_pack.login_pack.about_pack.about__page import About
from page_pack.login_pack.about_pack.pricing_pack.pricing__page import Pricing

after_login_home_page_url = 'https://www.saucedemo.com/inventory.html'
cart_page_url = 'https://www.saucedemo.com/cart.html'
add_info_page_url = 'https://www.saucedemo.com/checkout-step-one.html'
overview_url = "https://www.saucedemo.com/checkout-step-two.html"
pricing_page_url = 'https://saucelabs.com/pricing'
span_live_299 = '//span[@text()="299"]'
span_virtual_cloud = '//span[@text()="899"]'

@pytest.mark.usefixtures("setup")
class Tests:

# valid credential---------------testcase 01
    def test_case_login(self, setup):
        try:
            login = Login(self.setup)
            base_page = WebElementActions(self.setup)
            login.method_login('standard_user', 'secret_sauce')
            expt_url = base_page.is_visible(after_login_home_page_url)
            assert self.current_url == expt_url, "successfully login"
            assert self.current_url != expt_url, "login failed"
            login.method_logout()

        except Exception as e:
            print("testcase 01 is somthing issues", e)

# valid credential---------------testcase 02
    def test_case_login(self, setup):
        try:
            login = Login(self.setup)
            base_page = WebElementActions(self.setup)
            login.method_login('locked_out_user', 'secret_sauce')
            expt_url = base_page.is_visible(after_login_home_page_url)
            assert self.current_url == expt_url, "successfully login"
            assert self.current_url != expt_url, "login failed"
            login.method_logout()

        except Exception as e:
            print("testcase 02 is somthing issues", e)

# valid credential---------------testcase 03
    def test_case_login(self, setup):
        try:
            login = Login(self.setup)
            base_page = WebElementActions(self.setup)
            login.method_login('problem_user', 'secret_sauce')
            expt_url = base_page.is_visible(after_login_home_page_url)
            assert self.current_url == expt_url, "successfully login"
            assert self.current_url != expt_url, "login failed"
            login.method_logout()

        except Exception as e:
            print("testcase 03 is somthing issues", e)

# valid credential---------------testcase 04
    def test_case_login(self, setup):
        try:
            login = Login(self.setup)
            base_page = WebElementActions(self.setup)
            login.method_login('performance_glitch_user', 'secret_sauce')
            expt_url = base_page.is_visible(after_login_home_page_url)
            assert self.current_url == expt_url, "successfully login"
            assert self.current_url != expt_url, "login failed"
            login.method_logout()

        except Exception as e:
            print("testcase 04 is somthing issues", e)


# valid credential---------------testcase 05
    def test_case_login(self, setup):
        try:
            login = Login(self.setup)
            base_page = WebElementActions(self.setup)
            login.method_login('error_user', 'secret_sauce')
            expt_url = base_page.is_visible(after_login_home_page_url)
            assert self.current_url == expt_url, "successfully login"
            assert self.current_url != expt_url, "login failed"
            login.method_logout()

        except Exception as e:
            print("testcase 05 is somthing issues", e)


# valid credential---------------testcase 06
    def test_case_login(self, setup):
        try:
            login = Login(self.driver)
            base_page = WebElementActions(self.driver)
            login.method_login('visual_user', 'secret_sauce')
            expt_url = base_page.is_visible(after_login_home_page_url)
            assert self.current_url == expt_url, "successfully login"
            assert self.current_url != expt_url, "login failed"
            login.method_logout()

        except Exception as e:
            print("testcase 06 is somthing issues", e)

# invalid credential---------------testcase 07
    def test_case_login(self, setup):
        try:
            login = Login(self.driver)
            base_page = WebElementActions(self.driver)
            login.method_login('secret_sauce', '1234567901')
            expt_url = base_page.is_visible(after_login_home_page_url)
            assert self.current_url == expt_url, "successfully login"
            assert self.current_url != expt_url, "login failed"
            login.method_logout()

        except Exception as e:
            print("testcase 07 is somthing issues", e)

# valid address---------------testcase 08
    def test_case_valid_address(self, setup):
        try:
            login = Login(self.driver)
            login.method_login('standard_user', 'secret_sauce')

            select_items = All_items(self.setup)
            select_items.select_Sauce_Labs_Backpack()
            select_items.select_Sauce_Labs_Bike_Light()
            select_items.select_Test_allTheThings_T_Shirt_Red()
            select_items.select_Sauce_Labs_Onesie()

            cart = Cart(self.setup)
            cart.click_cart_icon()

            expt_url = base_page.is_visible(cart_page_url)
            assert self.current_url == expt_url, "this is cart page"

            cart.click_shopping_button()
            addr = AddInfo(self.setup)
            addr.fill_the_address(firstname="kishore", lastname='k', zipcode="123456")
            basepage = WebElementActions(self,driver)
            basepage.take_screenshot()

            overview = Overview(self.setup)
            overview.finish_btn()
            login.method_logout()

        except Exception as e:
            print("somthing this issue", e)

# invalid address---------------testcase 09
    def test_case_invalid_address(self, setup):
        try:
            login = Login(self.setup)
            login.method_login('standard_user', 'secret_sauce')

            select_items = All_items(self.setup)
            select_items.select_Sauce_Labs_Backpack()
            select_items.select_Sauce_Labs_Bike_Light()

            cart = Cart(self.setup)
            cart.click_cart_icon()

            expt_url = base_page.is_visible(cart_page_url)
            assert self.current_url == expt_url, "this is cart page"

            cart.click_shopping_button()
            addr = AddInfo(self.setup)
            addr.fill_the_address(firstname="786841536", lastname='68465135', zipcode="score123406")
            basepage = WebElementActions(self.setup)
            basepage.take_screenshot()

            overview = Overview(self.setup)
            overview.finish_btn()
            login.method_logout()

        except Exception as e:
            print("somthing this issue", e)

# visiting the pricing module of live_testing--------------------testcase 10
    def test_case_visit_price_live_testing(self):
        try:
            login = Login(self.setup)
            login.method_login('standard_user', 'secret_sauce')

            about = About(self.setup)
            about.click_pricing_text()

            price = Pricing(self.setup)
            price.using_scroll()
            price.live_testing_platform()

            assert is_visible(By.XPATH, span_live_299).text == "299", "Per month, billed annually or $289 month to month"
            login.method_logout()

        except Exception as e:
            print("somthing this issue", e)

# visiting the pricing module of virtual_cloud--------------------testcase 11
    def test_case_visit_price_virtual_cloud(self):
        try:
            login = Login(self.setup)
            login.method_login('standard_user', 'secret_sauce')

            about = About(self.setup)
            about.click_pricing_text()

            price = Pricing(self.setup)
            price.using_scroll()
            price.live_testing_platform()
            assert is_visible(By.XPATH, span_virtual_cloud).text() == "899", "Per month, billed annually or $1199 month to month"
            price.get_start_btn()

            basepage = WebElementActions(self.setup)
            basepage.take_screenshot()
            login.method_logout()

        except Exception as e:
            print("somthing this issue", e)

