import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ChromeOptions


@allure.step('Фикстура: инициализация драйвера браузера Chrome')
@pytest.fixture
def driver():
    # Настройки Chrome
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1400,800")
    driver_instance = webdriver.Chrome(options=chrome_options)
    
    yield driver_instance
    
    # Завершение работы драйвера
    driver_instance.quit()