from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_case1():
    print("TEST CASE 1.")
    driver = webdriver.Firefox()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

# The computer detects the element Text input.
    text_box = driver.find_element(by=By.NAME, value="my-text")
    

# The computer sends the text "Hello" to Text input box.
    text_box.send_keys("Hello")
    
# The computer waits to make sure all procedures are done.

    time.sleep(3)

# Sanity check

    current_value = text_box.get_attribute("value")

    predicted_value = "Hello"

# Assert is used to check the value.

    assert current_value == predicted_value

# The computer detects the element Submit button.
# The computer clicks on the submit button and receivs the message "Reiceived!" appears in a new window.

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn").click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

# The browser shuts down.

    driver.quit()