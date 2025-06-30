from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


# Инициализировать драйвер Chrome
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("window-size=1400,800")
    driver_instance = webdriver.Chrome(options=chrome_options)
    yield driver_instance
    driver_instance.quit()