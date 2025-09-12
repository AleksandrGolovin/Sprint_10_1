import allure
from pages.base_page import BasePage
from locators.general_locators import GeneralLocators
from locators.route_selection_page_locators import RouteSelectionPageLocators


class RouteSelectionPage(BasePage):
        
    @allure.step('Сравнение текстового сообщения результата с ожидаемым текстом')
    def is_results_equal(self, expected_results_text, expected_results_duration):
        conditions = [
            self.get_text_from_element(RouteSelectionPageLocators.DIV_RESULTS_TEXT) == expected_results_text,
            self.get_text_from_element(RouteSelectionPageLocators.DIV_RESULTS_DURATION) == expected_results_duration
        ]
        return all(conditions)
    
    def get_active_route_mode_name(self):
        return self.get_text_from_element(RouteSelectionPageLocators.DIV_ROUTE_MODE_ACTIVE)
    
    @allure.step('Проверка переключения таба режима на Оптимальный и изменения сообщений')
    def is_mode_switched_from_fast_to_optimal(self) -> bool:
        # На табе Быстрый
        self.switch_mode_to_fast()
        fast_text = self.get_text_from_element(RouteSelectionPageLocators.DIV_RESULTS_TEXT)
        fast_tab_name = self.get_text_from_element(RouteSelectionPageLocators.DIV_ROUTE_MODE_FAST)
        is_fast_tab_active = fast_tab_name == self.get_active_route_mode_name()
        # На табе Оптимальный
        self.switch_mode_to_optimal()
        optimal_text = self.get_text_from_element(RouteSelectionPageLocators.DIV_RESULTS_TEXT)
        optimal_tab_name = self.get_text_from_element(RouteSelectionPageLocators.DIV_ROUTE_MODE_OPTIMAL)
        is_optimal_tab_active = optimal_tab_name == self.get_active_route_mode_name()
        
        conditions = [
            is_optimal_tab_active,
            is_fast_tab_active,
            fast_text != optimal_text
        ]
        return all(conditions)
    
    @allure.step('Переключение таба на режим Оптимальный')
    def switch_mode_to_optimal(self):
        self.click_to_element(RouteSelectionPageLocators.DIV_ROUTE_MODE_OPTIMAL)
        
    @allure.step('Переключение таба на режим Быстрый')
    def switch_mode_to_fast(self):
        self.click_to_element(RouteSelectionPageLocators.DIV_ROUTE_MODE_FAST)
    
    @allure.step('Переключение таба на режим Свой')
    def switch_mode_to_personal(self):
        self.click_to_element(RouteSelectionPageLocators.DIV_ROUTE_MODE_PERSONAL)
        
    @allure.step('Переключение таба на режим Свой')
    def switch_type_to_drive(self):
        self.click_to_element(RouteSelectionPageLocators.DIV_TRANSPORT_TYPE_DRIVE)
    
    @allure.step('Получить спиосок всех отключенных табов типа передвижения')
    def get_enabled_transport_types_tabs(self):
        return self.find_visible_elements(RouteSelectionPageLocators.DIV_TRANSPORT_TYPES_ENABLED)
    
    @allure.step('Проверить, что все табы типа передвижения активны')
    def is_transport_types_tabs_enabled(self):
        enabled_tabs_count = len(self.get_enabled_transport_types_tabs())
        return enabled_tabs_count == 6

    @allure.step('Проверить, что появилась кнопка Заказать такси')
    def is_order_button_active(self):
        conditions = [
            self.find_visible_element(RouteSelectionPageLocators.BUTTON_ORDER_TAXI)
        ]
        return all(conditions)
    
    @allure.step('Начать оформлять заказ такси')
    def start_ordering_taxi(self):
        self.click_to_element(RouteSelectionPageLocators.BUTTON_ORDER_TAXI)
    
    @allure.step('Проверить, что появилась кнопка Забронировать')
    def is_book_button_active(self):
        conditions = [
            self.find_visible_element(RouteSelectionPageLocators.BUTTON_BOOK)
        ]
        return all(conditions)
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(RouteSelectionPageLocators.DIV_ROUTE_SELECTION_BLOCK)
        ]
        return all(conditions)