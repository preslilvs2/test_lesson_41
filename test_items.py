import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestMultiLangSite():
    def test_button_add_to_basket_is_exist(self, browser):
        browser.get(link)
        wait_clickable_add_to_basket = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
        add_to_basket = ""
        try:
            add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
            print (add_to_basket)
        except NoSuchElementException:
            assert add_to_basket, "button .btn-add-to-basket not exist"
        time.sleep(5)