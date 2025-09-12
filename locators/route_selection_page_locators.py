from selenium.webdriver.common.by import By


class RouteSelectionPageLocators:
    DIV_ROUTE_SELECTION_BLOCK = By.XPATH, ".//div[contains(@class, 'type-picker shown')]"
    DIV_RESULTS_TEXT = By.XPATH, ".//div[@class='results-text']/div[@class='text']"
    DIV_RESULTS_DURATION = By.XPATH, ".//div[@class='results-text']/div[@class='duration']"
    DIV_ROUTE_MODE_OPTIMAL = By.XPATH, ".//div[@class='modes-container']/div[text()='Оптимальный']"
    DIV_ROUTE_MODE_FAST = By.XPATH, ".//div[@class='modes-container']/div[text()='Быстрый']"
    DIV_ROUTE_MODE_PERSONAL = By.XPATH, ".//div[@class='modes-container']/div[text()='Свой']"
    DIV_ROUTE_MODE_ACTIVE = By.XPATH, ".//div[@class='modes-container']/div[@class='mode active']"
    DIV_TRANSPORT_TYPES_ENABLED = By.XPATH, ".//div[@class='types-container']/div[not(contains(@class, 'disabled'))]"
    DIV_TRANSPORT_TYPE_DRIVE = By.XPATH, ".//div[@class='types-container']/div[contains(@class, 'type drive')]"
    BUTTON_ORDER_TAXI = By.XPATH, ".//button[text()='Вызвать такси']"
    BUTTON_BOOK = By.XPATH, ".//button[text()='Забронировать']"