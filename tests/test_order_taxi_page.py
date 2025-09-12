import allure
import pytest
from data import ADDRESS_FROM, ADDRESS_TO, TARIFFS
from pages.main_page import MainPage
from pages.route_selection_page import RouteSelectionPage
from pages.order_taxi_page import OrderTaxiPage


@allure.title('Тестовые сценарии блока заказа такси')
class TestRouteSelectionPage:
    
    @allure.title('Проверка отображения блока заказа такси')
    @allure.description('Открыть главную страницу, ввести адреса ОТКУДА и КУДА, выбрать режим Быстрый, нажать кнопку Заказать такси, проверить, что появился блок заказа такси')
    def test_order_taxi_page_order_button_click_order_block_show_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)
        
        assert all(
            [
                order_taxi_page.is_loaded(),
                order_taxi_page.is_tariff_titles_match(),
                order_taxi_page.count_of_active_tariffs() == 1
            ]
        )
        
    @allure.title('Проверка описания тарифа в сплывающем окне информации требованиям ТЗ')
    @allure.description('Открыть главную страницу, ввести адреса ОТКУДА и КУДА, выбрать режим Быстрый, нажать кнопку Заказать такси, выбрать тариф, навестись на кнопку (i), получить описание и сравнить с ТЗ') 
    @pytest.mark.xfail(reason = "BUG: перепутаны описания тарифов Сонный и Разговорчивый")
    @pytest.mark.parametrize("tariff_name", TARIFFS.keys())
    def test_order_taxi_page_show_and_match_tariff_info_success(self, tariff_name, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)
        getted_tariff_description = order_taxi_page.get_tariff_information_by_name(tariff_name)
        
        assert getted_tariff_description == TARIFFS[tariff_name]
        
    @allure.title('Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси')
    @allure.description('Открыть главную страницу, ввести адреса ОТКУДА и КУДА, выбрать режим Быстрый, нажать кнопку Заказать такси, проверить наличие элементов') 
    def test_order_taxi_page_check_block_elements_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)
        
        assert order_taxi_page.is_block_elements_exists()
        
    