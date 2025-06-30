import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.general_locators import GeneralLocators


class OrderPage(BasePage):
    def set_fields_first_page(self, data):
        self.set_text_to_element(OrderPageLocators.INPUT_FIRSTNAME, data['first_name'])
        self.set_text_to_element(OrderPageLocators.INPUT_LASTNAME, data['last_name'])
        self.set_text_to_element(OrderPageLocators.INPUT_ADDRESS, data['address'])
        self.click_to_element(OrderPageLocators.INPUT_METRO)
        station_locator = self.format_locator(OrderPageLocators.BUTTON_METRO, data['station'])
        self.click_to_element(station_locator)
        self.set_text_to_element(OrderPageLocators.INPUT_PHONE, data['phone'])
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    def set_fields_second_page(self, data):
        self.set_text_to_element(OrderPageLocators.INPUT_DATE, data['date'])
        self.click_to_element(OrderPageLocators.DIV_CALENDAR_DAY)
        self.click_to_element(OrderPageLocators.DIV_PERIOD)
        period_locator = self.format_locator(OrderPageLocators.DIV_PERIOD_DROPDOWN, data['period'])
        self.click_to_element(period_locator)

    def create_order(self, data):
        self.safe_submit_cookie_button(GeneralLocators.COOKIE_BUTTON_LOCATOR)
        self.set_fields_first_page(data)
        self.set_fields_second_page(data)
