import allure
import pytest
from data import ADDRESS_FROM, ADDRESS_TO
from pages.main_page import MainPage
from pages.route_selection_page import RouteSelectionPage


@allure.title('Тестовые сценарии блока выбора маршрута после ввода адресов')
class TestRouteSelectionPage:
    
    @allure.title('Проверка отображения блока выбора маршрута после ввода адресов ОТКУДА и КУДА')
    @allure.description('Открыть главную страницу, ввести адреса ОТКУДА и КУДА, проверить, что появился блок выбора маршрута')
    @pytest.mark.parametrize('address_from, address_to', 
        [
            (ADDRESS_FROM, ADDRESS_TO),
            (ADDRESS_FROM, ADDRESS_FROM)
        ]
    )
    def test_route_selection_page_route_selection_block_show_success(self, address_from, address_to, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(address_from, address_to)
        main_page.wait_for_drawing_route()
        
        route_selection_page = RouteSelectionPage(driver)
        
        assert route_selection_page.is_loaded()