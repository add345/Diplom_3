import allure
import pytest
from pages.page_base import PageBase
from locators.locators_constructor import ConstructorLocators

class PageConstructor(PageBase):

    @allure.step("Подождать загрузки страницы")
    def page_loading_wait(self):
        self.wait_element_hide(ConstructorLocators.loading_modal)

    @allure.step("Щелчок мышью по кнопке \"Конструктор\"")
    def click_constructor_button(self):
        self.click_element(ConstructorLocators.button_constructor)

    @allure.step("Щелчок мышью по ингредиенту")
    def click_ingredient_bul(self):
        self.click_element(ConstructorLocators.ingredient_bul)

    @allure.step("Проверить, отобразилось ли всплывающее окно с описанием ингредиента")
    def is_ingredient_popup_displayed(self):
        return self.if_element_displayed(ConstructorLocators.popup_ingredient_window)

    @allure.step("Ожидание появления всплывающего окна с описанием ингредиента")
    def wait_for_ingredient_popup_displayed(self):
        self.wait_element(ConstructorLocators.popup_ingredient_window)

    @allure.step("Ожидание закрытия всплывающего окна с описанием ингредиента")
    def wait_for_ingredient_popup_closed(self):
        self.wait_element_hide(ConstructorLocators.popup_ingredient_window)

    @allure.step("Щелчок мышью по крестику для закрытия окна с описанием ингредиента")
    def click_ingredient_popup_close(self):
        self.click_element(ConstructorLocators.popup_close_cross)

    @allure.step("Ожидание загрузки (значок loading)")
    def wait_loading_overlay_displayed(self):
        self.wait_element_hide(ConstructorLocators.loading_modal)

    @allure.step("Переместить ингредиент в корзину")
    def move_ingredient_to_basket(self):
        self.drag_and_drop(ConstructorLocators.ingredient_bul, ConstructorLocators.burger_basket)

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter_value(self):
        return self.get_element_text(ConstructorLocators.ingredient_counter)

    @allure.step("Ожидание изменения значения счетчика ингредиента")
    def wait_for_ingredient_counter_change(self):
        self.wait_element_text_changes(ConstructorLocators.ingredient_counter)

    @allure.step("Нажать кнопку \"Оформить заказ\"")
    def make_order_button(self):
        self.click_element(ConstructorLocators.make_order_button)

    @allure.step("Ожидание окна с информацией о заказе")
    def wait_for_order_info(self):
        self.wait_element_visible(ConstructorLocators.order_info)

    @allure.step("Ожидание окна с информацией о заказе")
    def wait_for_order_number(self):
        self.wait_element_text_changes(ConstructorLocators.order_number)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        return int(self.get_element_text(ConstructorLocators.order_number))