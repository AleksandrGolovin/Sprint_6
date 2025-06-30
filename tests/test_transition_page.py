import allure
from pages.transition_page import TransitionPage
from data import Urls


@allure.title('Тестовые сценарии переходов между страницами')
class TestTransitionPage:
    "Тестовые сценарии для переходов между страницами"

    @allure.title('Тест перехода по клику на логотип Яндекса')
    @allure.description('Перейти на страницу создания заказа, кликнуть на логотип Яндекса, проверить, что произошел переход на Дзен')
    def test_transition_via_yandex_logo(self, chrome_driver):
        """Проверка перехода на Дзен по клику на логотип Яндекса

        Args:
            chrome_driver (WebDriver): драйвер браузера Chrome
        """
        transition_page = TransitionPage(chrome_driver)
        transition_page.go_to_url(Urls.ORDER_PAGE)
        
        assert transition_page.check_yandex_logo_transition()

    @allure.title('Тест перехода по клику на логотип Самоката')
    @allure.description('Перейти на страницу создания заказа, кликнуть на логотип Самоката, проверить, что произошел переход на главную страницу')
    def test_transition_via_scooter_logo(self, chrome_driver):
        """Проверка перехода на главную страницу по клику на логотип Самоката

        Args:
            chrome_driver (WebDriver): драйвер браузера Chrome
        """
        transition_page = TransitionPage(chrome_driver)
        transition_page.go_to_url(Urls.ORDER_PAGE)
        
        assert transition_page.check_scooter_logo_transition()

    