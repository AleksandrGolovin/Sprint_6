from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


# Инициализировать драйвер Firefox
@pytest.fixture
def firefox_driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--private")
    firefox_options.add_argument("--width=1400")
    firefox_options.add_argument("--height=800")
    driver_instance = webdriver.Firefox(options=firefox_options)
    yield driver_instance
    driver_instance.quit()