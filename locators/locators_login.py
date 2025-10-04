from selenium.webdriver.common.by import By

class LoginLocators:
    loading_modal = (By.CSS_SELECTOR, 'div.Modal_modal__P3_V5')
    email_field = (By.XPATH, "//div[label[contains(text(), 'Email')]]/input")
    password_field = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input")
    enter_button = (By.XPATH, "//form/button")