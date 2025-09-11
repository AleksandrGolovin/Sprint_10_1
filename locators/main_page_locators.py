from selenium.webdriver.common.by import By


class MainPageLocators:
    YMAPS_FROM_TO = By.XPATH, ".//ymaps[contains(@id, 'id_')]"
    