import allure
from pages.base_page import BasePage
from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from data import URL


class MainPage(BasePage):
    BASE_URL = URL.MAIN_PAGE
    
    @allure.step('Перейти на страницу регистрации')
    def enter_route_addresses(self, address_from: str, address_to: str):
        self.open()
        self.is_loaded()
        self.set_text_to_element(GeneralLocators.INPUT_FROM, address_from)
        self.set_text_to_element(GeneralLocators.INPUT_TO, address_to)
        self.wait_for_drawing_route()
    
    @allure.step('Ожидание отрисовки маршрута и конечных точек')
    def wait_for_drawing_route(self):
        self.wait_for_visibility_all_elements(MainPageLocators.YMAPS_FROM_TO)
    
    @allure.step('Проверка добавления на карту точек ОТКУДА и КУДА')
    def is_adding_route_points(self) -> bool:
        elements = self.find_visible_elements(MainPageLocators.YMAPS_FROM_TO)
        
        conditions = [
            len(elements) == 2,
            all(element.is_displayed() for element in elements)
        ]
        return all(conditions)
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(GeneralLocators.INPUT_FROM),
            self.find_visible_element(GeneralLocators.INPUT_TO)
        ]
        return all(conditions)