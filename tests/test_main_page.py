import pytest
import allure
from pages.main_page import MainPage
from data import Urls, QNA_DATA


@allure.title('Тестовые сценарии главной страницы')
class TestMainPage:
    "Тестовые сценарии для главной страницы"

    @allure.title('Проверка вопросов и ответов')
    @allure.description('Перейти на главную страницу, подтвердить использование cookie (если нужно), проверить пару вопрос-ответ')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_questions_and_answers(self, index, chrome_driver):
        """Проверка блока вопросов и ответов на главной странице

        Args:
            index (int): номер (индекс) вопроса
            chrome_driver (WebDriver): драйвер браузера Chrome
        """
        main_page = MainPage(chrome_driver)
        main_page.go_to_url(Urls.MAIN_PAGE)
        question, answer = QNA_DATA[index]

        assert main_page.check_question_and_answer(index, question, answer)