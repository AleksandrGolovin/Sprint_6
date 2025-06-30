import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from data import Urls, ORDER_DATA_1, ORDER_DATA_2


@allure.title('Тестовые сценарии страницы заказов')
class TestOrderPage:
    "Тестовые сценарии для страницы заказов"

    @allure.title('Проверка регистрации заказа')
    @allure.description('Перейти на главную страницу, нажать кнопку "Заказать", заполнить данные для заказа, проверить, что появилось сообщение об успешном завершении заказа')
    @pytest.mark.parametrize('create_order_locator, order_data', [
        (MainPageLocators.BUTTON_ORDER_UPPER, ORDER_DATA_1),
        (MainPageLocators.BUTTON_ORDER_LOWER, ORDER_DATA_2)
    ])
    def test_create_order(self, create_order_locator, order_data, firefox_driver):
        """Проверка регистрации заказа

        Args:
            create_order_locator (tuple(By, str)): локатор кнопки "Заказать"
            order_data (dict[str, str]): словарь с данными
            firefox_driver (WebDriver): драйвер браузера Firefox
        """
        order_page = OrderPage(firefox_driver)
        order_page.go_to_url(Urls.MAIN_PAGE)
        order_page.begin_create_order(create_order_locator)
        order_page.create_order(order_data)

        assert order_page.check_order_is_success()