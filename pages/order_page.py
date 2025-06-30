import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.general_locators import GeneralLocators


class OrderPage(BasePage):
    @allure.step('Сокрытие сообщения о куки и начало создания заказа по кнопке "Заказать"')
    def begin_create_order(self, locator):
        self.safe_submit_cookie_button(GeneralLocators.COOKIE_BUTTON_LOCATOR)
        self.click_to_element(locator)

    @allure.step('Заполнение полей на первой странице создания заказа')
    def set_fields_first_page(self, data):
        self.set_text_to_element(OrderPageLocators.INPUT_FIRSTNAME, data['first_name'])
        self.set_text_to_element(OrderPageLocators.INPUT_LASTNAME, data['last_name'])
        self.set_text_to_element(OrderPageLocators.INPUT_ADDRESS, data['address'])
        self.click_to_element(OrderPageLocators.INPUT_METRO)
        station_locator = self.format_locator(OrderPageLocators.BUTTON_METRO, data['station'])
        self.click_to_element(station_locator)
        self.set_text_to_element(OrderPageLocators.INPUT_PHONE, data['phone'])
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение полей на второй странице создания заказа')
    def set_fields_second_page(self, data):
        self.set_text_to_element(OrderPageLocators.INPUT_DATE, data['date'])
        self.click_to_element(OrderPageLocators.DIV_CALENDAR_DAY)
        self.click_to_element(OrderPageLocators.DIV_PERIOD)
        period_locator = self.format_locator(OrderPageLocators.DIV_PERIOD_DROPDOWN, data['period'])
        self.click_to_element(period_locator)
        color_locator = self.format_locator(OrderPageLocators.INPUT_COLOR, data['color'])
        self.click_to_element(color_locator)
        self.set_text_to_element(OrderPageLocators.INPUT_COMMENT, data['comment'])
        self.click_to_element(OrderPageLocators.BUTTON_SUBMIT_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_YES)

    @allure.step('Создание заказа')
    def create_order(self, data):
        self.set_fields_first_page(data)
        self.set_fields_second_page(data)

    @allure.step('Проверка успешности создания заказа')
    def check_order_is_success(self):
        label_text = self.get_text_from_element(OrderPageLocators.DIV_SUCCESS_LABEL)
        return "Заказ оформлен" in label_text
