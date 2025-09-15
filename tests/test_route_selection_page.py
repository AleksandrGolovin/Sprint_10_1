import allure
import pytest
from data import ADDRESS_FROM, ADDRESS_TO, SAME_FROM_TO_RESULTS_DURATION, SAME_FROM_TO_RESULTS_TEXT
from pages.main_page import MainPage
from pages.route_selection_page import RouteSelectionPage


@allure.title('Тестовые сценарии блока выбора маршрута после ввода адресов')
class TestRouteSelectionPage:
    
    @allure.title('Проверка отображения блока выбора маршрута после ввода адресов ОТКУДА и КУДА')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута')
    @pytest.mark.parametrize('address_from, address_to', 
        [
            (ADDRESS_FROM, ADDRESS_TO),
            (ADDRESS_FROM, ADDRESS_FROM)
        ]
    )
    def test_route_selection_page_input_from_to_route_selection_block_show_success(self, address_from, address_to, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(address_from, address_to)
        route_selection_page = RouteSelectionPage(driver)
        
        assert route_selection_page.is_loaded()

    @allure.title('Проверка отображения текста "Авто Бесплатно В пути 0 мин." в блоке выбора маршрута после ввода одинаковых адресов ОТКУДА и КУДА')
    @allure.description('При вводе одинакового адреса в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин."')
    def test_route_selection_page_input_same_from_to_zero_time_show_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_FROM)
        
        route_selection_page = RouteSelectionPage(driver)
        
        assert route_selection_page.is_results_equal(expected_results_text=SAME_FROM_TO_RESULTS_TEXT, expected_results_duration=SAME_FROM_TO_RESULTS_DURATION)
    
    @allure.title('Проверка смены активного таба на Оптимальный и пересчета времени и стоимости маршрута')
    @allure.description('При переключении между видами маршрута (Оптимальный/Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута')
    def test_route_selection_page_switch_mode_fast_to_optimal_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        
        route_selection_page = RouteSelectionPage(driver)
        
        assert route_selection_page.is_mode_switched_from_fast_to_optimal()
    
    @allure.title('Проверка смены активного таба на Свой и включение табов типа Машина, Пешком, Такси, Велосипед, Самокат, Драйв')
    @allure.description('При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)')
    def test_route_selection_page_switch_mode_to_personal_transport_types_active_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_personal()
        
        assert route_selection_page.is_transport_types_tabs_enabled()
    
    @allure.title('Проверка появления кнопки Вызвать такси при выборе режима Быстрый')
    @allure.description('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_route_selection_page_switch_mode_to_fast_order_button_active_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        
        assert route_selection_page.is_order_button_active()
    
    @allure.title('Проверка появления кнопки Забронировать при выборе режима Свой и типа Драйв')
    @allure.description('При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать')
    def test_route_selection_page_switch_mode_to_personal_type_drive_book_button_active_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_personal()
        route_selection_page.switch_type_to_drive()
        
        assert route_selection_page.is_book_button_active()