# Created by owner at 11/29/24
Feature: Navigate to the Shop page and Validate Product Details
  As a user
  I want to navigate to the shop link and add the product in to cart
  and finally proceed to check out and add the billing details.

#  Scenario: 1 Verify the cart functionality
#    Given the user go to the home page of the WooCommerce website
#    When the user click on the cart link in the header menu
#    Then the page should redirect to the cart page having listing of product to add in the cart
#    When the user click on the " Add to cart " button to add the product in the cart
#    Then the selected item should be display in the cart
#
#  Scenario: 2 Verify the Proceed to Checkout process
#    Given the user is on the cart page having product in the cart of 10 dollar
#    When the user clicks on the "Proceed to Checkout" button

    Scenario: 1 From home page navigate to the Shop page and viewing product details
      Given I have opened the website at "http://100.29.35.3/"
      When I click on the "Shop" link in the header
      Then I should see a demo product with the image of "horse"
      And I should see the product name as "Demo Product" and by clicking the name it goes to product page.
      And the product page title should be "Product"
      And the price of the product should be "$10.00"
      And there should be a "Add to cart" button on the product page

    Scenario: 2 Viewing cart after adding a product
      Given I am on the product page "http://100.29.35.3/product/demo-product/"
      When I click the "Add to cart" button
      Then I should see a message indicating the product is "1 in cart"
      And The cart icon in the header should display "1" item
      And  A "View cart" link should appear below the product
      When I click on the "View cart" link
      Then I should be navigated to the cart page
      And On the cart page, product "Demo Product" should be listed in the cart with a price of "$10"

    Scenario: 3 Add product to the cart and Proceeding to Checkout

      And the product "Demo Product" with a price of "$10" is listed in the cart
      When I click the "Proceed to Checkout" button
      Then I should be navigated to the checkout page
      And  I should see folowing fields for entering billing details
        | First name        |  Last name         |  Company name      | Country / Region      |  Street address       | Town / City     | State        | ZIP Code        | Phone           | Email address |
        | Required (*)      |  Required (*)      |  Optional          | Required (dropdown)   |  Required (*)         | Required (*)    | Required (*) | Required (*)    | Required (*)    | Required (*)  |
      And I should see the order details with the following fields.
        | Product           | Subtotal      | Shipping        | Total  |
        | Demo Product  * 1 | $10.00        | Free shipping   | $10.00 |
      And I should see the two payment methods in accordian.
        | Credit Card |
        | PAYARC Hosted Checkout  |
      And I should Credit Card option with following fields.
        |Card Number | Expiration (MM/YY) | Card Security Code |
        | Required   | Required           | Required           |
      And I should see the "Place order" button to book the order while credit card option is selected.
      And I should PAYARC Hosted Checkout option with the following field.
        | You'll be asked to provide your credit card details |
      And I should see the "Continue to Payment" button to book the order while PAYMARC Hosted Checkout option is selected.
      And I should see the disable checkbox option of "Ship to a different address"?
      And I should see the "Order notes(optional) field under the checkbox option.

    Scenario: 4 Filling out valid checkout details
      Given I fill in the following details on checkout page
        | First name        |  Last name         |  Company name      | Country / Region      |  Street address       | Town / City     | State        | ZIP Code        | Phone           | Email address |
        | John              |  Smith             |  IT                | American Samoa        |  California,street1   | california      | CA           | 2001            |+1234324639      | johnsmith1@gmail.com  |
#      (Should I write the order view step again here )
#      And I fill the Credit Card details in the following fields
#        |Card Number         | Expiration (MM/YY) | Card Security Code |
#        | 4242424242424242   | 0123               | 123                |
      And I fill in following card details on customer checkout screen
      | Card Holder   | Card Number       | Expiry Date   | CVV     |
      | Test demo     | 4242424242424242  | 0123          | 123     |
      Then I click on the "Place order" button to book order
      And I should see following thanks message on the thank you page.
      |Message  |
      |Thank you. Your order has been received.|
      And I should see following order details below the thank you message.
      | Order number | Date             | Total            |  Email                       | Payment method |
      | 81           | Decemebr 4,2024  | $10.00           |  johnsmith1@gmail.com        | Credit Card    |

      And I should see order details in the following fields.
       | Product           | Subtotal      | Shipping        | Total  |
       | Demo Product  * 1 | $10.00        | Free shipping   | $10.00 |

      And I should see Billing address details as confirmation.
#      I have to confirm form sir that which fields will come here







