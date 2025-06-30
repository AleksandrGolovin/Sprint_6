from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    "Базовая страница для наследования остальными страницами типовых методов"
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        "Перейти на страницу по адресу"
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        "Найти элемент на странице"
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        "Кликнуть на элемент на странице"
        self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        "Передать текст в элемент ввода"
        self.find_element_with_wait(locator).send_keys(text)
    
    def get_text_from_element(self, locator):
        "Получить текст элемента"
        text = self.find_element_with_wait(locator).text
        return text

    def scroll_to_element(self, locator):
        "Пролистать страницу до элемента"
        element = self.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def format_locator(self, locator_unformatted, element_index):
        """Форматировать локатор по метке {index}

        Args:
            locator_unformatted (tuple (By, str)): локатор с меткой индекса элемента {index}
            element_index (int): индекс элемента

        Returns:
            tuple(By, str): форматированный локатор с индексом
        """
        method, locator = locator_unformatted
        locator: str = locator.format(index=element_index)
        return method, locator