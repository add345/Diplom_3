from selenium.webdriver.common.by import By

class ConstructorLocators:

    loading_modal = (By.CSS_SELECTOR, 'div.Modal_modal__P3_V5')
    button_constructor = (By.XPATH, "//ul/li/a/p[contains(.,'Конструктор')]")
    button_feed = (By.XPATH, "//ul/li/a/p[contains(.,'Лента Заказов')]")

    ingredient_bul = (By.XPATH, '//a[descendant::p[contains(.,"булка")]][1]')

    ingredient_counter = (By.XPATH, '//a[descendant::p[contains(.,"булка")]][1]//p[@class="counter_counter__num__3nue1"]')
    popup_ingredient_window = (By.CSS_SELECTOR, 'section.Modal_modal__P3_V5')

    popup_close_cross = (By.XPATH, "//div[descendant::h2[contains(.,'Детали ингредиента')]]/button")
    burger_basket = (By.CSS_SELECTOR, 'section.BurgerConstructor_basket__29Cd7')
    make_order_button = (By.XPATH, '//button[text()="Оформить заказ"]')
    order_info = (By.XPATH, '//div[descendant::p[text()="идентификатор заказа"]]')
    order_number = (By.XPATH, '//div[descendant::p[text()="идентификатор заказа"]]/h2')
