from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_case1():
    print("TEST CASE 2.")
    driver = webdriver.Firefox()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

 # The computer detects the element Password.

    password_box = driver.find_element(by=By.NAME, value="my-password")
    
# The computer writes "123" inside the Password box.
    password_box.send_keys("123")

# The computer waits to make sure all procedures are done.

    time.sleep(3)

# Sanity check

    current_value = password_box.get_attribute("value")

    predicted_value = "123"

# Assert is used to check the value.

    assert current_value == predicted_value

# The computer detects the element Submit button.
 # The computer clicks the on submit button and receivs the message "Reiceived!" appears in a new window.

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn").click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

# The browser shuts down.

    driver.quit()