from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_case1():
    print("TEST CASE 3.")
    driver = webdriver.Firefox()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

# The computer detects the element Textarea.

    textArea_box = driver.find_element(by=By.NAME, value="my-textarea")
    
# The computer sends the text "Cool" to Textarea box.

    textArea_box.send_keys("Cool")

# The computer waits to make sure all procedures are done.
    
    time.sleep(3)

# Sanity check

    current_value = textArea_box.get_attribute("value")

    predicted_value = "Cool"

# Assert is used to check the value.

    assert current_value == predicted_value

# The computer detects the element Submit button.
# The computer clicks on the submit button and receivs the message "Reiceived!" appears in a new window.
    
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn").click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

# # The browser shuts down.

    driver.quit()