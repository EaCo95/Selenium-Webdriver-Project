from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import keyboard
import time

def test_case4():
    print("TEST CASE 5.")

    driver = webdriver.Firefox()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # The computer identifies the element Dropdown(datalist).

    DropDown_textbox = driver.find_element(By.NAME, "my-datalist")
    
# The computer writes "Chi" inside the Dropdown(datalist) box.

    DropDown_textbox.send_keys("Chi")

#The computer waits to ensure all options are loaded.

    time.sleep(4)

    # The computer moves down to the first option "Chicago" in the dropdown menu.

    DropDown_textbox.send_keys(Keys.ARROW_DOWN)

    # The computer clicks enter to select the first option "Chicago" in the dropdown menu.

    DropDown_textbox.send_keys(Keys.ENTER)

# The computer waits to make sure all procedures are done.

    time.sleep(2)

    # Sanity check

    current_value = DropDown_textbox.get_attribute("value")

    predicted_value = "Chicago"

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