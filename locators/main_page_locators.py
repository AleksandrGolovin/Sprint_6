from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{index}'
    ANSWER_LOCATOR = By.ID, 'accordion__panel-{index}'
    QUESTION_LOCATOR_TO_SCROLL = By.ID, 'accordion__heading-7'