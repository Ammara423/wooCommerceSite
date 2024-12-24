# step_definitions.py
import time
from tabnanny import check

from behave import given, when, then
# from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.ui import WebDriverWait

from my_project.woo_website.locators.woo_checkout_locators import Locators
from my_project.woo_website.pages.woo_checkout_objects import ShopPage, CartPage, CheckoutPage


@given("I navigate to the home page of the woo commerce website")
def step_navigate_to_home(context):
    shop_page = ShopPage(context.driver)
    shop_page.open_home_page()


@when('I click on the "{link}" in the header to navigate to the shop page')
def step_click_shop_link(context, link):
    shop_page = ShopPage(context.driver)
    shop_page.navigate_to_shop()


@then("I should see a demo image of the product")
def step_verify_demo_image(context):
    shop_page = ShopPage(context.driver)
    print("drive executed")
    # time.sleep(1)
    shop_page.verify_product_image()
    print("verify executed")
    # time.sleep(1)
    print("test case is pass")


@then('I should see the product name as "{product_name}" under the image')
def step_verify_product_name(context,product_name):
    shop_page = ShopPage(context.driver)
    print("drive executed")
    # time.sleep(1)
    shop_page.verify_product_name(product_name)
    print("verify executed")

# @then('the price of the product should be "{price}" under the product name')
# def step_verify_product_price (context, price):
#     shop_page = ShopPage(context.driver)
#     print("drive executed")
#     time.sleep(2)
#     shop_page.verify_product_price(price)
#     print("verify executed")
#     time.sleep(2)
#     print("test case is pass")
@then ('there should be a "{button}" on the product page')
def step_verify_button(context,button):
    shop_page = ShopPage(context.driver)
    print("drive executed")
    shop_page.verify_add_to_cart_button(button)
    print("verify executed")
    # time.sleep(2)
    print("test case is pass")

@given('I click the "{cta_button}" button')
def step_add_to_cart(context, cta_button):
    shop_page = ShopPage(context.driver)
    shop_page.add_to_cart(cta_button)
    # time.sleep(2)
    print("test case is pass")

@then('I should see a message indicating the product is "{no_of_items}" on the cart page')
def step_verify_cart_message(context, no_of_items):
    cart_page = CartPage(context.driver)
    cart_page.verify_cart_contents(no_of_items)

@then('The cart icon in the header should display "{badge}" of selected items')
def step_verify_cart_badge(context,badge):
    cart_page = CartPage(context.driver)
    cart_page.verify_no_of_badge(badge)
    # print("verify executed")
    # print("test case is pass")
# @then('A "View cart" link should appear below the product')

@when('I click on the "{link}" to view cart page')
def step_view_cart(context,link):
    cart_page = CartPage(context.driver)
    cart_page.navigate_to_cart(link)
    # time.sleep(5)

@then("I should be navigated to the cart page")
def step_verify_cart_navigation(context):
    cart_page = CartPage(context.driver)
    cart_page.verify_product_in_cart()

@when ('I click the "{proceed_to_checkout_button_click}" button on the cart page')
def step_proceed_to_checkout(context,proceed_to_checkout_button_click):
    cart_page = CartPage(context.driver)
    cart_page.proceed_to_checkout(proceed_to_checkout_button_click)
    # time.sleep(2)

@then ('I should be navigated to the checkout page, and heading should be "{title}"')
def step_verify_checkout_navigation(context,title):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.verify_checkout_page(title)

# @then ('I should see following fields for entering billing details')
# def step_verify_billing_details_fields(context):
#         checkout_page = CheckoutPage(context.driver)
#         expected_dict = {}
#         for row in context.table:
#             for expect_label, exp_value in row.as_dict().items():
#                 expected_dict[expect_label] = exp_value
#         fields_dict = checkout_page.verify_billing_fields()
#         assert_equals(expected_dict, fields_dict)

@then('I should see following fields for entering billing details')
def step_verify_billing_details_fields(context):
    checkout_page = CheckoutPage(context.driver)
    # Define the expected fields and their properties
    expected_fields = (
        {"name": "First name", "required": "Required (*)"},
        {"name": "Last name", "required": "Required (*)"},
        {"name": "Company name", "required": "Optional"},
        {"name": "Country / Region", "required": "Required (dropdown)"},
        {"name": "Street address", "required": "Required (*)"},
        {"name": "Town / City", "required": "Required (*)"},
        {"name": "State", "required": "Required (*)"},
        {"name": "ZIP Code", "required": "Required (*)"},
        {"name": "Phone", "required": "Required (*)"},
        {"name": "Email address", "required": "Required (*)"},
    )
    # Verify the fields on the page
    checkout_page.verify_billing_fields(expected_fields)

@given('I fill in the following details on checkout page on the cart page')
def step_fill_checkout_details(context):
    print("Filling in checkout details...")
    checkout_page = CheckoutPage(context.driver)
    for row in context.table:
        for field, value in row.as_dict().items():
            checkout_page.fill_billing_details(field, value)
            # time.sleep(2)

@when('I should see the "{payment_type}" label')
def step_verify_payment_type(context, payment_type):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.verify_payment_type()
    # time.sleep(2)
    print("test case is pass")

@when ('I click on the "{continue_button}" button')
def step_click_place_holder_button(context,continue_button):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.click_place_holder_button()
    # time.sleep(8)
    print("test case is pass")


@then('I fill in following card details on customer checkout screen')
def step_fill_card_details(context):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.switch_to_payrac_iframe()
    time.sleep(5)

    # for row in context.table:
    #     cardholder_name = ["Cardholder Name"]
    #     card_number = row["Card Number"]
    #     expiration_date = row["MM/YY"]
    #     cvv = row["CVV"]
    # checkout_page.fill_card_details(cardholder_name, card_number, expiration_date, cvv)
    for row in context.table:
        for field, value in row.as_dict().items():
            checkout_page.fill_card_details(field, value)
            time.sleep(4)

@then ('I click on the "{proceeding}" button to book order')
def step_click_checkout_button(context, proceeding):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.click_checkout_button()
    time.sleep(5)
    print("test case is pass")



# @then('I click on the "{method_name}" payment method')
# def step_select_payment_method(context, method_name):
#     checkout_page = CheckoutPage(context.driver)
#     checkout_page.select_payment_method(method_name)
#     time.sleep(2)

# @when('I click on the "{continue_button}" button')
# def step_click_continue(context,continue_button):
#     checkout_page = CheckoutPage(context.driver)
#     checkout_page.proceed_to_payment()
#     time.sleep(10)

# @when("I fill the Credit Card details in the following fields")
# def step_fill_card_details(context):
#     checkout_page = CheckoutPage(context.driver)
#     card_details = {row["Field"]: row["Value"] for row in context.table}
#     checkout_page.fill_card_details(card_details)
#
# @then("I should see following success message on the pop up")
# def step_verify_success_message(context):
#     assert "Please wait! We are processing your process" in context.driver.page_source
# @then('A pop up appear with the card and Billing Details fields.')
# def step_verify_popup_with_card_details(context):
#     checkout_page = CheckoutPage(context.driver)
#     checkout_page.switch_to_payrac_iframe()
#     print("iframe not displayed")
#     assert checkout_page.is_card_popup_displayed(), "The card details popup is not displayed."
#
# #
# @then('I fill the Credit Card details in the following fields on the payrac pop')
# def step_fill_credit_card_details(context):
#     checkout_page = CheckoutPage(context.driver)
    # checkout_page.switch_to_payrac_iframe()
    # print("iframe not displayed")
    # for row in context.table:
    #     card_number = row["Card Number"]
    #     expiration_date = row["Expiration date"]
    #     cvv = row["CVV"]
    # #     checkout_page.fill_card_details(card_number, expiration_date, cvv)
    # for row in context.table:
    #     for field, value in row.as_dict().items():
    #         checkout_page.fill_card_details(field, value)
