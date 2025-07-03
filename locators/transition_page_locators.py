from selenium.webdriver.common.by import By


class TransitionPageLocators:
    LOGO_SCOOTER = By.XPATH, ".//img[@alt='Scooter']"
    LOGO_YANDEX = By.XPATH, ".//img[@alt='Yandex']"
    IMG_MAIN_PAGE_SCOOTER = By.XPATH, ".//img[@alt='Scooter blueprint']"
    BUTTON_DZEN_SEARCH = By.XPATH, ".//button[@type='submit' and text()='Найти']"