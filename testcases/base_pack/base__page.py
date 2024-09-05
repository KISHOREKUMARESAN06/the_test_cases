from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains,Keys


class WebElementActions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # clicking method
    def click_element(self, locator_type, locator_value):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((locator_type, locator_value)))
        element.click()

    # send keys method
    def send_keys_to_element(self, locator_type, locator_value, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((locator_type, locator_value)))
        element.send_keys(text)

    # scroll down method
    def scroll_down_method(self,locator_type, locator_value):
        scroll = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((locator_type, locator_value)))
        scroll.send_keys(Keys.PAGE_DOWN)

    # handle the alert popup
    def handle_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()  # Accept the alert
        except:
            pass  # No alert found

    # select the visible text drop down
    def select_drop_down_visible_text(self, locator_type, locator_value, visibletext):
        drop_down = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_type, locator_value)))
        drop_down.select_by_visible_text(visibletext)

    # select the index drop down
    def select_drop_down_index(self, locator_type, locator_value, index):
        drop_down = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_type, locator_value)))
        drop_down.select_by_index(index)

    # select the value drop down
    def select_drop_down_value(self, locator_type, locator_value, value):
        drop_down = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_type, locator_value)))
        drop_down.select_by_value(value)

    # scroll where we want ?..
    def scroll_where(self,locator_type, locator_value):
        flag = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((locator_type, locator_value)))
        self.driver.exeute_script("arguments[0].scrollIntoView();", flag)
        value = self.driver.exeute_script("return window.pageYOffset;")
        print("Number of Pixels Moved", value)

    # conformation Is_visible method
    def is_visible(self, value):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(value))
        return bool(element)


    # take the screenshot
    def take_screenshot(self, file_name='screenshot.png', save_path='./screenshots'):
        # Ensure the directory exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Construct the full file path
        file_path = os.path.join(save_path, file_name)

        # Take the screenshot
        self.driver.save_screenshot(file_path)
        return file_path

    # check element is visible
    def is_element_visible(self, locator_type, locator_value):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((locator_type, locator_value)))
            return True
        except:
            return False

"""
    # check element is displayed
    def is_element_displayed(self, locator_type, locator_value):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((locator_type, locator_value)))
            return element.is_displayed()
        except:
            return False

    # check element is enabled
    def is_element_enabled(self, locator_type, locator_value):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((locator_type, locator_value)))
            return element.is_enabled()
        except:
            return False
            
     # check element is visible
    def is_element_visible(self, locator_type, locator_value):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((locator_type, locator_value)))
            return True
        except:
            return False
"""

# ------------------------------------------------------------------------------------------------------------------

'''
    # 
    # # taking screenshot method
    #
    # def take_screenshot(self, file_name='screenshot.png', save_path='./screenshots'):
    #     # Ensure the directory exists
    #     if not os.path.exists(save_path):
    #         os.makedirs(save_path)
    # 
    #     # Construct the full file path
    #     file_path = os.path.join(save_path, file_name)
    # 
    #     # Take the screenshot
    #     self.driver.save_screenshot(file_path)
    #     return file_path
    #------------------------------------------------------------------------------------------------------------------
    # 
    # # taking screenshot method
    #
    # def scroll_and_capture(self, num_screenshots, wait_time=2, save_path='./screenshots'):
    #     # Ensure the directory exists
    #     if not os.path.exists(save_path):
    #         os.makedirs(save_path)
    #
    #     for i in range(num_screenshots):
    #         # Take a screenshot
    #         file_name = f'screenshot_{i + 1}.png'
    #         file_path = os.path.join(save_path, file_name)
    #         self.driver.save_screenshot(file_path)
    #         print(f"Screenshot {i + 1} saved at: {file_path}")
    #
    #         # Scroll down the page
    #         self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
    #
    #         # Wait for the page to load (adjust wait_time as needed)
    #         time.sleep(wait_time)
'''

