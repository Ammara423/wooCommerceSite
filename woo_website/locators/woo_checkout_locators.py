# locators.py
from selenium.webdriver.common.by import By

class Locators:
    # Home Page
    SHOP_LINK = '//*[@id="modal-1-content"]/ul/ul/li[6]/a'

    # Shop Page
    PRODUCT_IMAGE =  '//*[@id="wp--skip-link--target"]/div[4]/ul/li/div[1]/a/img'
        # '//*[@id="wp--skip-link--target"]/div[4]/ul/li/div[1]/a/img'
    PAYMENT_TYPE = '//*[@id="payment"]/ul/li/label'
    PRODUCT_NAME =   '//*[@id="wp--skip-link--target"]/div[4]/ul/li/h3/a'
    PRODUCT_PRICE =  '//*[@id="wp--skip-link--target"]/div[4]/ul/li/div[2]/div/span'
    ADD_TO_CART_BUTTON = '//*[@id="wp--skip-link--target"]/div[4]/ul/li/div[3]/button/span'
    PLACE_ORDER_BUTTON = '//*[@id="moneris_place_order"]'
    # PAYRAC_POP_UP = '/html/body/div/iframe[contains(@class, "payarc-js-sdk-modal-layer__iframe")]'
    # PAYRAC_POP_UP = '//iframe[contains(@class, "payarc")]'
    PAYMENT_PAGE ='//*[@id="monerisCheckout-Frame"]'
    # Cart Page
    CART_ITEM_ICON = '//*[@id="wp--skip-link--target"]/div[4]/ul/li/div[3]/button/span'
    CART_BADGE = '/html/body/div[1]/header/div/div/div[2]/div[2]/button/span/span'
    VIEW_CART_LINK =  '//*[@id="wp--skip-link--target"]/div[4]/ul/li/div[3]/span/a'
    CART_PRODUCT_NAME = '//*[@id="wp--skip-link--target"]/div[2]/div/div[4]/div/div/div[2]/table/tbody/tr/td[2]/div/a'
    CART_PRODUCT_PRICE = '//*[@id="wp--skip-link--target"]/div[2]/div/div[4]/div/div/div[2]/table/tbody/tr/td[2]/div/div[1]/span/span'
    PROCEED_TO_CHECKOUT_BUTTON = '//*[@id="wp--skip-link--target"]/div[2]/div/div[4]/div/div/div[3]/div[3]/div[2]/a'
    TITLE_TEXT = '//*[@id="customer_details"]/div[1]/div/h3'
    # PAYARC_Hosted_Checkout = '//*[@id="payment_method_payarc_hosted"]'

    billing_fields_locators = {
        "First name": (By.ID, "billing_first_name"),
        "Last name": (By.ID, "billing_last_name"),
        "Company name": (By.ID, "billing_company"),
        "Country / Region": (By.ID, "billing_country"),
        "Street address": (By.ID, "billing_address_1"),
        "Town / City": (By.ID, "billing_city"),
        "State": (By.ID, "billing_state"),
        "ZIP Code": (By.ID, "billing_postcode"),
        "Phone": (By.ID, "billing_phone"),
        "Email address": (By.ID, "billing_email"),
    }

    # Checkout Page
    BILLING_DETAILS_FIELDS = {
        "First name": "#billing_first_name",
        "Last name": "#billing_last_name",
        "Company name": "#billing_company",
        "Country / Region": "#billing_country",
        "Street address": "#billing_address_1",
        "Town / City": "#billing_city",
        "State": "#billing_state",
        "ZIP Code": "#billing_postcode",
        "Phone": "#billing_phone",
        "Email address": "#billing_email"
    }
    # PAYMENT_METHODS = {
    #     # "credit_card": "#payment_method_credit_card",
    #         "PAYARC Hosted Checkout": "#payment_method_payarc"
    # }
    # Replace with the correct locator
    CONTINUE_TO_PAYMENT_BUTTON = "#place_order"
    SHIP_TO_DIFFERENT_ADDRESS_CHECKBOX = "#ship_to_different_address"
    ORDER_NOTES_FIELD = "#order_comments"
    SUCCESS_MESSAGE = ".success-message"  # Update with actual selector

    # PayARC Popup
    CARD_DETAILS = {
        "Cardholder Name": "#cardholder",
        "Card Number": "#pan",
        "MM/YY": "#expiry_date",
        "CVV": "#cvv"
    }
    CHECK_OUT_BUTTON = "#process"
