# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
#
# # Load credentials from environment variables
# username = os.getenv("ORANGEHRM_USERNAME")
# password = os.getenv("ORANGEHRM_PASSWORD")
#
# # Ensure credentials are available
# if not username or not password:
#     raise ValueError("Environment variables for username or password are not set!")
#
# # Set up the Selenium WebDriver
# driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# # Automate login
# driver.find_element(By.NAME, "username").send_keys(username)
# driver.find_element(By.NAME, "password").send_keys(password)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# # Verify successful login (Check for dashboard presence)
# try:
#     dashboard = driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb")
#     print("Login successful!")
# except Exception as e:
#     print("Login failed:", str(e))
#
# # Close the browser
# driver.quit()
