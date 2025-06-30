import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from data import Urls, ORDER_DATA

@allure.title('Тестовые сценарии страницы заказов')
class TestOrderPage:
    "Тестовые сценарии для страницы заказов"

    @allure.title('Проверка регистрации заказа')
    @allure.description('')
    @pytest.mark.parametrize('locator, order_data', [
        (MainPageLocators.BUTTON_ORDER_UPPER, ORDER_DATA)
    ])
    def test_questions_and_answers(self, locator, order_data, driver):
        """Проверка блока вопросов и ответов на главной странице

        Args:
            index (int): номер (индекс) вопроса
            driver (WebDriver): драйвер браузера (Selenium)
        """
        order_page = OrderPage(driver)
        order_page.go_to_url(Urls.MAIN_PAGE)
        order_page.click_to_element(locator)

        order_page.create_order(order_data)

        assert True