import allure
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PageBase:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать, пока изменится url")
    def wait_for_url(self, url):
        WebDriverWait(self.driver, timeout=10).until(EC.url_to_be(url))

    @allure.step("Подождать, пока элемент спрячется")
    def wait_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Подождать, пока элемент не исчезнет")
    def wait_element_removed(self, locator):
        # отличие от того, что элемент спрячется в том, что элемент вообще исчезает из DOM и вернуть его нельзя
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))

    @allure.step("Подождать, пока текст элемента изменится")
    def wait_element_text_changes(self, locator):
        text = self.get_element_text(locator)
        WebDriverWait(self.driver, timeout=10).until(EC.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source, target):
        draggable = self.driver.find_element(*source)
        droppable = self.driver.find_element(*target)
        drag_and_drop(self.driver, draggable, droppable)

    @allure.step("Подождать наличия элемента")
    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step("Подождать видимости элемента")
    def wait_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        element = self.wait_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Проверить отображение элемента')
    def if_element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step("Получить url текущей страницы")
    def get_url(self):
        return self.driver.current_url

    @allure.step("Проверка наличия элемента по составному локатору")
    def if_element_text_exists(self, locator_str, text):
        locator = (By.XPATH, locator_str.replace("{text}", str(text)))
        element = self.wait_element(locator)
        return element.is_displayed()

