from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_case4():
    print("TEST CASE 4.")

    driver = webdriver.Firefox()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# The computer detects the element Dropdown(select).
    
    select_element = driver.find_element(By.NAME, "my-select")
    
# The computer waits to make sure all options are loaded.

    time.sleep(2)

# The computer selects an option by the visable text "Two".

    select = Select(select_element)
    select.select_by_visible_text("Two")
    selected_option = select.first_selected_option.text

# The computer waits to make sure all procedures are done.

    time.sleep(2)

# Assert is used to check the selected option.

    assert selected_option == "Two"

# The computer detects the element Submit button.
# The computer clicks on the submit button and receivs the message "Reiceived!" appears in a new window.

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn").click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

# The browser shuts down.

    driver.quit()





























# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By

# def test_case1():
#     print("TEST CASE 1.")
#     driver = webdriver.Firefox()

#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#     title = driver.title
#     assert title == "Web form"


#     dropdown_box = driver.find_element(by=By.TAG_NAME, value="Option")
#     i = 0
#     while i < len(dropdown_box):
#         if(dropdown_box[i.text == "One"]):
#             dropdown_box[i].click()

#             i = i + 1

#     # submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn")

#     # text_box.select("Open this select menu")
#     # text_box.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

#     driver.quit() 










#     drop = Select(driver.find.element.by.id)("Open-this-select-menu")

#     drop.select_by_value("One")



    
    
    
    
    
    # ddelement= Select(driver.find_element_by_id('id_of_element'))

    # ddelement= Select(driver.find_element_by_css_selector('css_selector_of_element'))

    # ddelement= Select(driver.find_element_by_xpath('xpath_of_element'))

    # ddelement= Select(driver.find_element_by_css_selector('css_selector_of_element'))

    # ddelement.select_by_index(1)

    # ddelement.select_by_value('1')

    # ddelement.select_by_visible_text('One')