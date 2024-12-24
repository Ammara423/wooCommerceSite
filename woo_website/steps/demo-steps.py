from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@given("I am on the OrangeHRM login page")
def step_open_login_page(context):
    context.driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when("I enter the username and password from environment variables")
def step_enter_credentials(context):
    usernamefield = os.getenv("ORANGEHRM_USERNAME")
    passwordfield = os.getenv("ORANGEHRM_PASSWORD")
    print(usernamefield)
    print(passwordfield)

    # Locate fields using correct locators
    username_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    password_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )

    username_field.send_keys(usernamefield)
    password_field.send_keys(passwordfield)

@when("I click the login button")
def step_click_login_button(context):
    login_button = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    login_button.click()

# @then("I should see the dashboard")
# def step_verify_dashboard(context):
#     try:
#         dashboard =  WebDriverWait(context.driver, 10).until(
#         EC.presence_of_element_located(By.CLASS_NAME, "oxd-topbar-header-breadcrumb"))
#         assert dashboard.is_displayed(), "Dashboard not found, login failed!"
#     finally:
#         context.driver.quit()



# @given("I am on the OrangeHRM login page")
# def step_open_login_page(context):
#     context.driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
#     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#
# @when("I enter the username and password from environment variables")
# def step_enter_credentials(context):
#     username = os.getenv("ORANGEHRM_USERNAME")
#     password = os.getenv("ORANGEHRM_PASSWORD")
#
#     print(username)
#     print(password)
#
#     # context.driver.find_element(By.NAME, "username").send_keys(username)
#     # context.driver.find_element(By.NAME, "password").send_keys(password)
#
#     # assert username and password, "Environment variables not set!"
#     #
#     # context.driver.find_element(By.NAME, "username").send_keys(username)
#     # context.driver.find_element(By.NAME, "password").send_keys(password)
#
#
# @when("I click the login button")
# def step_click_login(context):
#     context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#
#
# @then("I should see the dashboard")
# def step_verify_dashboard(context):
#     dashboard = context.driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb")
#     assert dashboard.is_displayed(), "Dashboard not found, login failed!"
#     context.driver.quit()
