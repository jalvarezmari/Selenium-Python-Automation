from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



firefox = webdriver.Firefox(executable_path='./geckodriver')

firefox.maximize_window()
firefox.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

#assert 'Selenium Easy Demo' in firefox.title

try:
    element = WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "at-cv-button.at-cv-lightbox-yesno.at-cm-no-button"))
    )

    shit_button = firefox.find_element_by_class_name("at-cv-button.at-cv-lightbox-yesno.at-cm-no-button")
    shit_button.click()


    user_message = (firefox.find_element_by_id("user-message"))
    user_message.clear()
    user_message.send_keys('YES')

    button = firefox.find_element_by_class_name("btn-default")
    button.click()


    output = firefox.find_element_by_id('display')

    time.sleep(5)
finally:
    firefox.quit()




