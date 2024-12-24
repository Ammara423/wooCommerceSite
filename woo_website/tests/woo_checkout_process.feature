# Created by owner at 12/6/24
Feature: Add a product and complete the check out process
  As a user
  I want to add my favourite product in the cart and complete
  the billing details and place order on the required address.

  Scenario: 1 Add the favourite product and complete the check out process.
    Given I navigate to the home page of the woo commerce website
    When I click on the "Shop" in the header to navigate to the shop page
    Then I should see a demo image of the product
    And I should see the product name as "Demo Product" under the image

    #And the product page title should be "Product"
    #And the price of the product should be "10 $" under the product name"

    And there should be a "Add to cart" on the product page

   Scenario: 2 Viewing cart after adding a product
      Given I click the "Add to cart" button
      Then I should see a message indicating the product is "1 in cart" on the cart page
      And The cart icon in the header should display "1" of selected items
#     And  A "View cart" link should appear below the product
      When I click on the "View cart" to view cart page
      Then I should be navigated to the cart page
#      And On the cart page, product "Demo Product" should be listed in the cart with a price of "10 $"

   Scenario: 3  When user click on Proceeding to Checkout button.
      When I click the "Proceed to Checkout" button on the cart page
      Then I should be navigated to the checkout page, and heading should be "Billing details"
      And  I should see following fields for entering billing details
        | First name        |  Last name         |  Company name      | Country / Region      |  Street address       | Town / City     | State        | ZIP Code        | Phone           | Email address |
        | Required (*)      |  Required (*)      |  Optional          | Required (dropdown)   |  Required (*)         | Required (*)    | Required (*) | Required (*)    | Required (*)    | Required (*)  |
#      And I should see the order details with the following fields.
#        | Product           | Subtotal      | Shipping        | Total  |
#        | Demo Product  * 1 | $10.00        | Free shipping   | $10.00 |
#      And I should see the following payment methods in accordian.
#        |Payment_methods|
#        | Credit Card |
#        | PAYARC Hosted Checkout  |
#      And I should see the disable checkbox option of "Ship to a different address"?
#      And I should see the "Order notes(optional) field under the checkbox option.

    Scenario: 4 Filling out valid checkout details and choose the payment method.
      Given I fill in the following details on checkout page on the cart page
#        | First name        |  Last name         |  Company name      | Country / Region      |  Street address       | Town / City     | State        | ZIP Code        | Phone           | Email address |
#        | John              |  Smith             |  IT                | American Samoa        |  California,street1   | california      | CA           | 2001            |+1234324639      | johnsmith1@gmail.com  |

        | First name        |  Last name         |  Company name          |  Street address       | Town / City             | ZIP Code        | Phone           | Email address |
        | John              |  Smith             |  IT                    |  California,street1   | california              | 20001            |+1234324639      | johnsmith1@gmail.com  |
#      Then I click on the "PAYARC Hosted Checkout" payment method
#      And I should see following information message after clicking on the payment method.
#        | Message |
#        | You'll be asked to provide your credit card details |
#      And I should see the "Continue to Payment" button to book the order.
      When I should see the "Moneris Payment" label
      When I click on the "Place order" button
      Then I fill in following card details on customer checkout screen
        | Cardholder Name   | Card Number       | MM/YY         | CVV     |
        | Test demo         | 4242424242424242  | 0123          | 123     |
      Then I click on the "Checkout" button to book order

#      When I click on the "Continue to Payment" button
#      Then A pop up appear with the card and Billing Details fields.
#      Then I fill the Credit Card details in the following fields on the checkout page
#        | Card Number         | Expiration date    | CVV    |
#        | 4242424242424242    | 0125               | 123   |
#      And I fill the billing address details on payrac pop up.
#      |First Name   | Last Name        | Address Line 1  | Address Line 2   | City       | State        | ZIP Code       | Email address |
#      | John        | Smith            | Oppsiste street1| Oppsiste street1 | California | California   | 20001          |johnsmith1@gmail.com
#      Then I click on the "Pay $10.00" button to book order
#      And I should see following success message on the pop up.
#      |Message  |
#      |Please wait! We are proccessing you process|
