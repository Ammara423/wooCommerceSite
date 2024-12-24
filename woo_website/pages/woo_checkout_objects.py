# page_objects.py
import time
from time import sleep

from my_project.woo_website.locators.woo_checkout_locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        # driver = webdriver.Chrome(ChromeDriverManager(version="131").install())

    def open_home_page(self) -> object:
        self.driver.get("http://100.29.35.3/")
        self.driver.maximize_window()

    def navigate_to_shop(self):
        shop_link = self.driver.find_element(By.XPATH, Locators.SHOP_LINK)
        shop_link.click()

    def verify_product_image(self):
        assert self.driver.find_element(By.XPATH, Locators.PRODUCT_IMAGE).is_displayed()
        print("image")

    def verify_product_name(self,product_name):
        product_name_element = self.driver.find_element(By.XPATH, Locators.PRODUCT_NAME).text
        print("name")
        assert product_name_element == product_name

    # def verify_product_price(self, price):
    #     product_price = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, Locators.PRODUCT_PRICE))
    #     ).text.strip()
    #     print(f"Expected price: {price}, Actual price: {product_price}")
    #     assert product_price == price, f"Price mismatch: Expected {price}, but got {product_price}"
    def verify_add_to_cart_button(self,button_text):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.ADD_TO_CART_BUTTON))
        )
        assert add_to_cart_button.is_displayed(), "Add to cart button not found"

        # assert self.driver.find_element(By.XPATH, Locators.ADD_TO_CART_BUTTON).is_displayed()
        # print("button is displayed")

    # def verify_product_details(self):
    #     assert self.driver.find_element(By.XPATH, Locators.PRODUCT_IMAGE).is_displayed()
    #     print("image")
    #     product_name = self.driver.find_element(By.XPATH, Locators.PRODUCT_NAME).text
    #     assert product_name == "Demo Product"
    #     print("name")
    #     # product_te = self.driver.title
    #     #         # assert product_title == "Product"itl
    #     product_price = self.driver.find_element(By.XPATH, Locators.PRODUCT_PRICE).text
    #     assert product_price == "10 $"
    #     print("price")
    #     assert self.driver.find_element(By.XPATH, Locators.ADD_TO_CART_BUTTON).is_displayed()
    #     print("button is displayed")

    def add_to_cart(self,cta_button):
        add_to_cart_button = self.driver.find_element(By.XPATH, Locators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_cart_contents(self,no_of_items):
        # cart_message = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, Locators.CART_ITEM_ICON))
        #     )
        cart_message = self.driver.find_element(By.XPATH, Locators.CART_ITEM_ICON).text
        assert no_of_items in cart_message

    def verify_no_of_badge(self,badge):
        selected_items_no = self.driver.find_element(By.XPATH, Locators.CART_BADGE).text
        assert badge in selected_items_no

    def navigate_to_cart(self,link):
        # self.driver.get(link)
        view_cart_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.VIEW_CART_LINK))
        )
        view_cart_link.click()

    def verify_product_in_cart(self):
        product_name = self.driver.find_element(By.XPATH, Locators.CART_PRODUCT_NAME).text
        product_price = self.driver.find_element(By.XPATH, Locators.CART_PRODUCT_PRICE).text
        assert product_name == "Demo Product"
        assert product_price == "10 $"

    def proceed_to_checkout(self, proceed_to_checkout_button_click):
        # self.driver.get(proceed_to_checkout_button_click)
        proceed_to_checkout_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Locators.PROCEED_TO_CHECKOUT_BUTTON))
        )
        proceed_to_checkout_button.click()
        # assert proceed_to_checkout_button.is_displayed()

class CheckoutPage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.CARD_POPUP = (By.CLASS_NAME, "payment-popup")
        self.driver = driver
        # self.billing_fields_locators = {
        #     "First name": (By.ID, "billing_first_name"),
        #     "Last name": (By.ID, "billing_last_name"),
        #     "Company name": (By.ID, "billing_company"),
        #     "Country / Region": (By.ID, "billing_country"),
        #     "Street address": (By.ID, "billing_address_1"),
        #     "Town / City": (By.ID, "billing_city"),
        #     "State": (By.ID, "billing_state"),
        #     "ZIP Code": (By.ID, "billing_postcode"),
        #     "Phone": (By.ID, "billing_phone"),
        #     "Email address": (By.ID, "billing_email"),
        # }

    def verify_checkout_page(self, title):
        heading_title = self.driver.find_element(By.XPATH, Locators.TITLE_TEXT)
        assert title in heading_title.text
        print("resolved")


    def verify_billing_fields(self, expected_fields):
        for field in expected_fields:
            field_name = field["name"]
            required_status = field["required"]

            # Find the field element
            field_locator = Locators.billing_fields_locators[field_name]
            field_element: object = self.driver.find_element(*field_locator)

            # Verify the field is displayed
            assert field_element.is_displayed(), f"Field '{field_name}' is not displayed on the page."

            # Additional checks based on required status
            if "Required" in required_status:
                # Check for a required attribute
                if "*" in required_status:
                    required_attr = field_element.get_attribute("aria-required")
                    assert required_attr is not None, f"Field '{field_name}' is not marked as required."
                elif "dropdown" in required_status:
                    assert field_element.tag_name == "select", f"Field '{field_name}' should be a dropdown."
            elif "Optional" in required_status:
                # Optionally, you can verify it doesn't have a required attribute
                pass

        print("All billing fields are displayed and meet the required conditions.")

    def fill_billing_details(self, field, value):
            field_locator = Locators.BILLING_DETAILS_FIELDS[field]
            self.driver.find_element(By.CSS_SELECTOR, field_locator).send_keys(value)

    # def select_payment_method(self, method):

    def verify_payment_type(self):
        assert self.driver.find_element(By.XPATH, Locators.PAYMENT_TYPE).is_displayed()
        print("payment type")

    def click_place_holder_button(self):
        place_holder_button = self.driver.find_element(By.XPATH, Locators.PLACE_ORDER_BUTTON)
        place_holder_button.click()
        # time.sleep(2)


    #def select_payment_method(self, method_name):

    #             # XPath to locate the label text dynamically and find its preceding sibling input (radio button)
    #             payment_method_xpath = f"//label[contains(text(), '{method_name}')]/preceding-sibling::input[@type='radio']"
    #             #payment_method_xpath = f"//label[contains(text(), '{method_name}')]/ul/li/input/following-sibling::label"
    #             time.sleep(2)
    #             # Find the radio button
    #             radio_button = self.driver.find_element(By.XPATH, payment_method_xpath)
    #             time.sleep(2)

    #             Check if radio button already selected for the selected payment method
    #             if not radio_button.is_selected():
    #                 print(f"Selecting the payment method: {method_name}")
    #                 radio_button.click()
    #                 time.sleep(2)
    #             else:
    #                 print(f"The payment method '{method_name}' is already selected.")


            # wait = WebDriverWait(self.driver, 10)
            #
            #  Dynamically create the XPath expression for the payment method
            #  xpath_expression = f"//*[contains(text(), '{method}')]/following::ul[1]/li/input/following-sibling::label"
            #  xpath_expression = f"//label[contains(text(), '{method}')]/preceding-sibling::input[@type = 'radio'"]
            #
            # Check if the element exists within the timeout period
            # elements = self.driver.find_elements(By.XPATH, xpath_expression)
            #
            # if elements:
            #     # Access the first matching element
            #     radio_button = wait.until(EC.presence_of_element_located((By.XPATH, xpath_expression)))
            #
            #     # Check if the radio button is already selected
            #     if not radio_button.is_selected():
            #         # Click the radio button if not selected
            #         radio_button.click()
            #         time.sleep(5)
            #         print(f"'{method}' option was not selected, now clicked.")
            #     else:
            #         print(f"'{method}' option is already selected.")
            # else:
            #     print(f"The payment method '{method}' was not found on the page.")

        # payment_method_locator = Locators.PAYMENT_METHODS[method]
        # payment_method = (self.driver.find_element(By.XPATH, Locators.PAYARC_Hosted_Checkout).click())
        # assert select_payment_method()
        # time.sleep(2)

        # assert payment_method.is_displayed()
        # print("payment method")

    # def proceed_to_payment(self):
    #     continue_button_element = self.driver.find_element(By.CSS_SELECTOR, Locators.CONTINUE_TO_PAYMENT_BUTTON)
    #     continue_button_element.click()
    #     time.sleep(2)

    # def is_card_popup_displayed(self):
    #     return self.wait.until(EC.visibility_of_element_located(self.CARD_POPUP)).is_displayed()
    # time.sleep(3)


    def switch_to_payrac_iframe(self):
        try:
            # Wait for presence of iframe and ensure it is an iframe
            iframe_element = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, Locators.PAYMENT_PAGE))
            )

            # Switch to the iframe
            self.driver.switch_to.frame(iframe_element)

            # Wait for "#cardholder" element to be clickable
            # WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#cardholder"))
            # ).send_keys("abcd")

        except Exception as e:
            print(f"An error occurred: {e}")

    def fill_card_details(self, field, value):
        field_locator = Locators.CARD_DETAILS[field]

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, field_locator))
        ).send_keys(value)

    def click_checkout_button(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.CHECK_OUT_BUTTON).click()
