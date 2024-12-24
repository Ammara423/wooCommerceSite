from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Automatically installs and uses the compatible ChromeDriver
# driver = webdriver.Chrome(ChromeDriverManager(version="131.0.0").install())

def before_all(context):
    #context is as start global varialble to access throughout all the tests.

    context.driver = webdriver.Chrome()
    # context.ammara = "ammara"
    # print("ammara")

def after_all(context):
    context.driver.quit()
