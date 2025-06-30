import allure
from pages.base_page import BasePage
from locators.transition_page_locators import TransitionPageLocators
from locators.general_locators import GeneralLocators
from data import Urls


class TransitionPage(BasePage):
    @allure.step('Переход на другую страницу по клику на логотип')
    def transition_via_logo(self, locator):
        self.safe_submit_cookie_button(GeneralLocators.COOKIE_BUTTON_LOCATOR)
        self.click_to_element(locator)
        self.switch_to_last_tab()

    @allure.step('Проверка успешного перехода')
    def is_transition_success(self, dest_url, element_locator):
        self.wait_for_url(dest_url)
        element = self.find_element_with_wait(element_locator)
        return element.is_displayed()
    
    @allure.step('Переход по клику на логотип Яндекса и проверка успешности операции')
    def check_yandex_logo_transition(self):
        self.transition_via_logo(TransitionPageLocators.LOGO_YANDEX)
        return self.is_transition_success(Urls.DZEN_PAGE, TransitionPageLocators.BUTTON_DZEN_SEARCH)
    
    @allure.step('Переход по клику на логотип Самоката и проверка успешности операции')
    def check_scooter_logo_transition(self):
        self.transition_via_logo(TransitionPageLocators.LOGO_SCOOTER)
        return self.is_transition_success(Urls.MAIN_PAGE, TransitionPageLocators.IMG_MAIN_PAGE_SCOOTER)