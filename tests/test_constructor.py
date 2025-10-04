import allure
import pytest
import urls
from conftest import constructor_page


class TestConstructor:

    @allure.title("Переход по кнопке \"Конструктор\"")
    @pytest.mark.usefixtures("driver", "constructor_page")
    def test_constructor_button(self):
        self.constructor_page.click_constructor_button()
        assert self.constructor_page.get_url() == urls.base_url


    @allure.title("Появление окна при щелчке по ингредиенту")
    @pytest.mark.usefixtures("driver", "constructor_page")
    def test_ingredient_popup(self):
        self.constructor_page.click_ingredient_bul()
        assert self.constructor_page.is_ingredient_popup_displayed()

    @allure.title("Закрытие окна при щелчке по крестику")
    @pytest.mark.usefixtures("driver", "constructor_page")
    def test_ingredient_popup_close(self):
        self.constructor_page.click_ingredient_bul()
        self.constructor_page.wait_for_ingredient_popup_displayed()
        self.constructor_page.click_ingredient_popup_close()
        self.constructor_page.wait_for_ingredient_popup_closed()

        assert self.constructor_page.is_ingredient_popup_displayed() == False

    @allure.title("Увеличение счетчика ингредиента при добавлении его в корзину")
    @pytest.mark.usefixtures("driver", "constructor_page")
    def test_ingredient_counter_increase(self):
        counter1 = int(self.constructor_page.get_ingredient_counter_value())
        self.constructor_page.move_ingredient_to_basket()
        self.constructor_page.wait_for_ingredient_counter_change()
        counter2 = int(self.constructor_page.get_ingredient_counter_value())
        assert counter1 < counter2


