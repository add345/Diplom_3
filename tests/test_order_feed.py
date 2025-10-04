import allure
import pytest
import urls
from pages.page_constructor import PageConstructor

class TestOrderFeed:

    @allure.step("Сделать заказ")
    def _make_order(self):
        self.driver.get(urls.base_url)
        self.constructor_page = PageConstructor(self.driver)

        self.constructor_page.page_loading_wait()
        self.constructor_page.move_ingredient_to_basket()
        self.constructor_page.make_order_button()

        self.constructor_page.wait_for_order_info()
        self.constructor_page.wait_for_order_number()

        self.constructor_page.page_loading_wait()

        self.order_number = self.constructor_page.get_order_number()

    @allure.title("Переход по кнопке \"Конструктор\"")
    @pytest.mark.usefixtures("driver", "orders_feed_page")
    def test_constructor_button(self):
        self.orders_feed_page.click_constructor_button()
        assert self.orders_feed_page.get_url() == urls.base_url


    @allure.title("При создании нового заказа счётчик \"Выполнено за всё время\" увеличивается")
    @pytest.mark.usefixtures("driver", "login", "orders_feed_page")
    def test_whole_time_counter_increase(self):
        # получить исходное состояние счётчика
        counter1 = self.orders_feed_page.get_whole_time_counter_value()
        # сделать заказ
        self._make_order()

        # возвратиться на страницу летны заказов
        self.driver.get(urls.orders_feed_url)
        self.orders_feed_page.page_loading_wait()

        # получить новое состояние счётчика
        counter2 = self.orders_feed_page.get_whole_time_counter_value()
        assert counter2 > counter1


    @allure.title("При создании нового заказа счётчик \"Выполнено за сегодня\" увеличивается")
    @pytest.mark.usefixtures("driver", "login", "orders_feed_page")
    def test_today_counter_increase(self):
        # получить исходное состояние счётчика
        counter1 = self.orders_feed_page.get_today_counter_value()
        # сделать заказ
        self._make_order()

        # возвратиться на страницу летны заказов
        self.driver.get(urls.orders_feed_url)
        self.orders_feed_page.page_loading_wait()

        # получить новое состояние счётчика
        counter2 = self.orders_feed_page.get_today_counter_value()
        assert counter2 > counter1


    @allure.title("После оформления заказа его номер появляется в разделе \"В работе\"")
    @pytest.mark.usefixtures("driver", "login", "orders_feed_page")
    def test_order_number_in_progress(self):
        # сделать заказ
        self._make_order()

        # возвратиться на страницу летны заказов
        self.driver.get(urls.orders_feed_url)
        self.orders_feed_page.page_loading_wait()

        assert self.orders_feed_page.if_order_number_in_work(self.order_number)
