import allure
from pages.page_base import PageBase
from locators.locators_order_feed import OrderFeedLocators

class PageOrderFeed(PageBase):

    @allure.step("Подождать загрузки страницы")
    def page_loading_wait(self):
        self.wait_element_removed(OrderFeedLocators.loading_modal)

    @allure.step("Щелчок мышью по кнопке \"Конструктор\"")
    def click_constructor_button(self):
        self.click_element(OrderFeedLocators.button_constructor)

    @allure.step("Проверка наличия номера заказа в списке \"В работе\"")
    def if_order_number_in_work(self, number):
        return self.if_element_text_exists(locator_str=OrderFeedLocators.order_in_work, text=number)

    @allure.step("Получить значение счетчика \"Выполнено за всё время\"")
    def get_whole_time_counter_value(self):
        return int(self.get_element_text(OrderFeedLocators.whole_time_counter))

    @allure.step("Получить значение счетчика \"Выполнено за сегодня\"")
    def get_today_counter_value(self):
        return int(self.get_element_text(OrderFeedLocators.today_counter))