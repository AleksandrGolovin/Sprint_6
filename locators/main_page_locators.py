from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = By.ID, 'accordion__heading-{data}'
    ANSWER = By.ID, 'accordion__panel-{data}'
    QUESTION_FOR_SCROLL = By.ID, 'accordion__heading-7'
    BUTTON_ORDER_UPPER = By.XPATH, ".//button[@class='Button_Button__ra12g']"
    BUTTON_ORDER_LOWER = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"