import allure
from pages.base_page import BasePage
from locators.general_locators import GeneralLocators
from locators.route_selection_page_locators import RouteSelectionPageLocators


class RouteSelectionPage(BasePage):
        
    # @allure.step('Перейти на страницу регистрации')
    # def enter_route_addresses(self, address_from: str, address_to: str):
    #     self.open()
    #     self.is_loaded()
    #     self.set_text_to_element(GeneralLocators.INPUT_FROM, address_from)
    #     self.set_text_to_element(GeneralLocators.INPUT_TO, address_to)
    
    # @allure.step('Проверка добавления на карту точек ОТКУДА и КУДА')
    # def is_adding_route_points(self) -> bool:
    #     elements = self.find_visible_elements(MainPageLocators.YMAPS_FROM_TO)
        
    #     conditions = [
    #         len(elements) == 2,
    #         all(element.is_displayed() for element in elements)
    #     ]
    #     return all(conditions)
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(RouteSelectionPageLocators.DIV_ROUTE_SELECTION_BLOCK)
        ]
        return all(conditions)