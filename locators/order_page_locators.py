from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_FIRSTNAME = By.XPATH, ".//input[@placeholder='* Имя']"
    INPUT_LASTNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"
    INPUT_ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    INPUT_METRO = By.XPATH, ".//input[@placeholder='* Станция метро']"
    BUTTON_METRO = By.XPATH, ".//div[@class='Order_Text__2broi' and text()='{data}']"
    INPUT_PHONE = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button[text()='Далее']"
    INPUT_DATE = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    DIV_CALENDAR_DAY = By.XPATH, ".//div[@class='react-datepicker__week']/div[contains(@class, 'react-datepicker__day--selected')]"
    DIV_PERIOD = By.XPATH, ".//div[@class='Dropdown-control']"
    DIV_PERIOD_DROPDOWN = By.XPATH, ".//div[@class='Dropdown-option' and text()='{data}']"
    INPUT_COLOR = By.ID, "{data}"
    INPUT_COMMENT = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    BUTTON_SUBMIT_ORDER = By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"
    BUTTON_YES = By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Да']"
    DIV_SUCCESS_LABEL = By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"