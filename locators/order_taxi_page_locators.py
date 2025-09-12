from selenium.webdriver.common.by import By


class OrderTaxiPageLocators:
    DIV_ORDER_BLOCK_SHOW = By.XPATH, ".//div[contains(@class, 'tariff-picker shown')]"
    DIV_TCARD_ACTIVE = By.XPATH, ".//div[@class='tcard active']"
    DIV_TARIFF_TITLES = By.XPATH, ".//div[@class='tcard-title']"
    DIV_TCARD_ACTIVE_PRICE = By.XPATH, ".//div[@class='tcard active']/div[@class='tcard-price']"
    
    BUTTON_TARIFF_INFO = By.XPATH, ".//div[contains(@class, 'tcard active')]/button"
    DIV_ACTIVE_TARIFF_DESCRIPTION = By.XPATH, ".//div[contains(@class, 'tcard active')]/div[contains(@class, 'show')]//div[@class='i-dPrefix']"
    
    DIV_PHONE = By.CLASS_NAME, "np-text"
    DIV_PAYMENT_METHOD = By.CLASS_NAME, "pp-text"
    DIV_PAYMENT_METHOD_TITLE = By.CLASS_NAME, "pp-value-text"
    INPUT_COMMENT = By.ID, "comment"
    DIV_REQUIREMENTS = By.CLASS_NAME, "reqs-head"
    BUTTON_ENTER_NUMBER_AND_ORDER = By.XPATH, ".//button[@class='smart-button']"
    SPAN_NOTEBOOK_CHECKBOX = By.XPATH, ".//div[(@class='r-sw-label') and (text()='Столик для ноутбука')]/following::span[@class='slider round']"
    
    DIV_ORDER_BODY = By.XPATH, ".//div[@class='order-body']"
    BUTTON_DETAILS = By.XPATH, ".//div[text()='Детали']/preceding-sibling::button"
    BUTTON_CANCEL = By.XPATH, ".//div[text()='Отменить']/preceding-sibling::button"
    
    DIV_AWAITING_HEADER_TITLE = By.CLASS_NAME, "order-header-title"
    DIV_AWAITING_HEADER_TIME = By.CLASS_NAME, "order-header-time"
    
    DIV_DETAILS_FROM = By.XPATH, ".//div[text()='Адрес подачи']/preceding-sibling::div"
    DIV_DETAILS_TO = By.XPATH, ".//div[text()='Адрес назначения']/preceding-sibling::div"
    DIV_DETAILS_PAYMENT_METHOD = By.XPATH, ".//div[text()='Способ оплаты']/preceding-sibling::div"
    DIV_CAR_NUMBER = By.CLASS_NAME, "number"
    DIV_DETAILS_INFORMATION_COST = By.XPATH, ".//div[text()='Еще про поездку']/following-sibling::div"