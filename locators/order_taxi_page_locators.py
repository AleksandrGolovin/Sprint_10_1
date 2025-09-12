from selenium.webdriver.common.by import By


class OrderTaxiPageLocators:
    DIV_ORDER_BLOCK_SHOW = By.XPATH, ".//div[contains(@class, 'tariff-picker shown')]"
    DIV_TCARD_ACTIVE = By.XPATH, ".//div[@class='tcard active']"
    DIV_TARIFF_TITLES = By.XPATH, ".//div[@class='tcard-title']"
    
    BUTTON_TARIFF_INFO = By.XPATH, ".//div[contains(@class, 'tcard active')]/button"
    DIV_ACTIVE_TARIFF_DESCRIPTION = By.XPATH, ".//div[contains(@class, 'tcard active')]/div[contains(@class, 'show')]//div[@class='i-dPrefix']"
    
    DIV_PHONE = By.CLASS_NAME, "np-text"
    DIV_PAYMENT_METHOD = By.CLASS_NAME, "pp-text"
    INPUT_COMMENT = By.ID, "comment"
    DIV_REQUIREMENTS = By.CLASS_NAME, "reqs-head"