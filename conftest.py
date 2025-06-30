from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


# Инициализировать драйвер Chrome
@pytest.fixture
def chrome_driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("window-size=1400,800")
    driver_instance = webdriver.Chrome(options=chrome_options)
    yield driver_instance
    driver_instance.quit()

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