import allure
import data
from pages.page_base import PageBase
from locators.locators_login import LoginLocators

class PageLogin(PageBase):

    @allure.step("Подождать загрузки страницы")
    def page_loading_wait(self):
        self.wait_element_hide(LoginLocators.loading_modal)

    @allure.step("Логин на странице входа")
    def send_email_password_enter(self):
        self.send_keys_to_input(LoginLocators.email_field, data.email)
        self.send_keys_to_input(LoginLocators.password_field, data.password)
        self.click_element(LoginLocators.enter_button)
