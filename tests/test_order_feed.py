import allure
import pytest
import urls
from pages.page_constructor import PageConstructor

class TestOrderFeed:

    @allure.title("Переход по кнопке \"Конструктор\"")
    @pytest.mark.usefixtures("driver", "orders_feed_page")
    def test_constructor_button(self):
        self.orders_feed_page.click_constructor_button()
        assert self.orders_feed_page.get_url() == urls.base_url


    @allure.title("При создании нового заказа счётчик \"Выполнено за всё время\" увеличивается")
    @pytest.mark.usefixtures("driver", "login", "constructor_page", "orders_feed_page")
    def test_whole_time_counter_increase(self):
        # получить исходное состояние счётчика
        counter1 = self.orders_feed_page.get_whole_time_counter_value()

        # перейти на страницу конструктора
        self.driver.get(urls.base_url)
        # сделать заказ
        self.constructor_page.make_order()

        # возвратиться на страницу летны заказов
        self.driver.get(urls.orders_feed_url)
        self.orders_feed_page.page_loading_wait()

        # получить новое состояние счётчика
        counter2 = self.orders_feed_page.get_whole_time_counter_value()
        assert counter2 > counter1


    @allure.title("При создании нового заказа счётчик \"Выполнено за сегодня\" увеличивается")
    @pytest.mark.usefixtures("driver", "login", "constructor_page", "orders_feed_page")
    def test_today_counter_increase(self):
        # получить исходное состояние счётчика
        counter1 = self.orders_feed_page.get_today_counter_value()

        # перейти на страницу конструктора
        self.driver.get(urls.base_url)
        # сделать заказ
        self.constructor_page.make_order()

        # возвратиться на страницу летны заказов
        self.driver.get(urls.orders_feed_url)
        self.orders_feed_page.page_loading_wait()

        # получить новое состояние счётчика
        counter2 = self.orders_feed_page.get_today_counter_value()
        assert counter2 > counter1


    @allure.title("После оформления заказа его номер появляется в разделе \"В работе\"")
    @pytest.mark.usefixtures("driver", "login", "orders_feed_page", "constructor_page")
    def test_order_number_in_progress(self):
        # сделать заказ
        order_number = self.constructor_page.make_order()

        # возвратиться на страницу летны заказов
        self.driver.get(urls.orders_feed_url)
        self.orders_feed_page.page_loading_wait()

        assert self.orders_feed_page.if_order_number_in_work(order_number)
