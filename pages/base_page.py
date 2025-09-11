import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
    Базовая страница для наследования остальными страницами типовых методов
    """
    BASE_URL = None
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открыть базовую страницу класса')
    def open(self):
        """Открыть базовую страницу"""
        if self.BASE_URL:
            self.go_to_url(self.BASE_URL)
        else:
            raise UnboundLocalError

    def go_to_url(self, url):
        """Перейти на страницу по адресу"""
        with allure.step(f'Перейти на страницу {url}'):
            self.driver.get(url)

    @allure.step('Найти все отображаемые элементы по локатору')
    def find_visible_elements(self, locator):
        self.wait.until(ec.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements
    
    @allure.step('Найти отображаемый элемент на странице')
    def find_visible_element(self, locator):
        """Найти visible-элемент на странице"""
        try:
            element = self.wait_for_visibility(locator)
            return element
        except:
            return None

    @allure.step('Найти неотображаемый элемент на странице')
    def find_invisible_element(self, locator):
        """Найти invisible-элемент на странице"""
        try:
            element = self.wait.until(ec.presence_of_element_located(locator))
            return element
        except:
            return None
    
    @allure.step('Ожидать отображения элемента')
    def wait_for_visibility(self, locator):
        """Ожидание отображение элемента"""
        return self.wait.until(ec.visibility_of_element_located(locator))
    
    @allure.step('Ожидать отображения всех элементов')
    def wait_for_visibility_all_elements(self, locator):
        """Ожидать отображения всех элементов"""
        self.wait.until(ec.visibility_of_all_elements_located(locator))
        
    @allure.step('Ожидать сокрытия элемента')
    def wait_for_invisibility(self, locator):
        """Ожидание сокрытия элемента"""
        return self.wait.until(ec.invisibility_of_element_located(locator))
    
    @allure.step('Перемотать страницу к элементу')
    def scroll_to_element(self, locator):
        """Пролистать страницу до элемента"""
        element = self.find_visible_element(locator)
        if element:
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
            except:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликнуть на элемент')
    def click_to_element(self, locator):
        """Кликнуть на элемент на странице"""
        element = self.wait.until(ec.element_to_be_clickable(locator))
        self.scroll_to_element(locator)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Передать текстовое значение элементу')
    def set_text_to_element(self, locator, text):
        """Передать текст в элемент ввода"""
        element = self.find_visible_element(locator)
        if element:
            element.send_keys(text)
    
    @allure.step('Получить текстовое значение элемента')
    def get_text_from_element(self, locator):
        """Получить текст элемента"""
        element = self.find_visible_element(locator)
        if element:
            text = element.text
            return text
        return None

    @allure.step('Прикрепить файл')
    def attach_file(self, locator, path):
        element = self.find_invisible_element(locator)
        if element:
            element.send_keys(str(path))
        else:
            raise AssertionError

    def _verify_page_loaded(self) -> bool:
        """Метод для проверки загрузки страницы (требует переопределения)"""
        return True

    @allure.step('Проверка, что страница открылась')
    def is_loaded(self):
        """Публичный метод для проверки загрузки страницы"""
        try:
            return self._verify_page_loaded()
        except:
            return False