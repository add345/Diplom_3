from selenium.webdriver.common.by import By

class OrderFeedLocators:

    loading_modal = (By.XPATH, '//*[@id="root"]/div/main/div[contains(text(), "Загрузка...")]')
    button_constructor = (By.XPATH, "//ul/li/a/p[contains(.,'Конструктор')]")
    button_feed = (By.XPATH, "//ul/li/a/p[contains(.,'Лента Заказов')]")
    order_in_work = "//ul/li[contains(.,'{text}')]"
    whole_time_counter = (By.XPATH, ".//*[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number__')]")
    today_counter = (By.XPATH, ".//*[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number__')]")
