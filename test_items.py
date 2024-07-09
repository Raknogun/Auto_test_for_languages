from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    browser.get(link)
    assert len(browser.find_elements(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')) > 0, 'Кнопки добавить нет'
    time.sleep(5)
