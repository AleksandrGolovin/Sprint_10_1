import allure
import pytest
from data import ADDRESS_FROM, ADDRESS_TO
from pages.main_page import MainPage


@allure.title('Тестовые сценарии главной страницы')
class TestMainPage:
    
    @allure.title('Проверка отображения точек маршрута на карте при вводе адресов ОТКУДА и КУДА')
    @allure.description('Открыть главную страницу, ввести адреса ОТКУДА и КУДА, проверить, что появились точки на карте')
    @pytest.mark.parametrize('address_from, address_to', 
        [
            (ADDRESS_FROM, ADDRESS_TO),
            (ADDRESS_TO, ADDRESS_FROM),
        ]
    )
    def test_main_page_input_from_to_route_show_success(self, address_from, address_to, driver):
        main_page = MainPage(driver)
        
        main_page.enter_route_addresses(address_from, address_to)
        
        assert main_page.is_adding_route_points()