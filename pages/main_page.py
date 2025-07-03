import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.general_locators import GeneralLocators


class MainPage(BasePage):
    @allure.step('Клик на вопрос')
    def click_to_question(self, index):
        locator_formatted = self.format_locator(MainPageLocators.QUESTION, index)
        self.scroll_to_element(MainPageLocators.QUESTION_FOR_SCROLL)
        self.click_to_element(locator_formatted)

    @allure.step('Получение текста вопроса')
    def get_question_text(self, index):
        locator_formatted = self.format_locator(MainPageLocators.QUESTION, index)
        return self.get_text_from_element(locator_formatted)

    @allure.step('Получение текста ответа')
    def get_answer_text(self, index):
        locator_formatted = self.format_locator(MainPageLocators.ANSWER, index)
        return self.get_text_from_element(locator_formatted)
    
    @allure.step('Проверка пары вопрос-ответ')
    def check_question_and_answer(self, index, question_input, answer_input):
        self.safe_submit_cookie_button(GeneralLocators.COOKIE_BUTTON_LOCATOR)
        question_text = self.get_question_text(index)
        self.click_to_question(index)
        answer_text = self.get_answer_text(index)
        result = question_text == question_input and answer_text == answer_input
        return result