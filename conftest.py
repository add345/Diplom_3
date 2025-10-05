import pytest
from selenium import webdriver
import urls
from pages.page_constructor import PageConstructor
from pages.page_login import PageLogin
from pages.page_order_feed import PageOrderFeed
import data

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        request.cls.driver = driver
        driver.get(urls.base_url)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        request.cls.driver = driver
        driver.get(urls.base_url)


    yield
    driver.quit()

@pytest.fixture
def constructor_page(request):
    request.cls.driver.get(urls.base_url)
    page = PageConstructor(request.cls.driver)
    page.page_loading_wait()
    request.cls.constructor_page = page

@pytest.fixture
@pytest.mark.usefixtures("driver")
def orders_feed_page(request):
    request.cls.driver.get(urls.orders_feed_url)
    page = PageOrderFeed(request.cls.driver)
    page.page_loading_wait()
    request.cls.orders_feed_page = page

@pytest.fixture
def login(request):
    request.cls.driver.get(urls.login_url)
    page = PageLogin(request.cls.driver)
    page.page_loading_wait()
    page.send_email_password_enter(data.email, data.password)
    page.wait_for_url(urls.base_url)

    request.cls.authorized_page = page
