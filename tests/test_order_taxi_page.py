import allure
import pytest
from data import ADDRESS_FROM, ADDRESS_TO, TARIFFS
from pages.main_page import MainPage
from pages.route_selection_page import RouteSelectionPage
from pages.order_taxi_page import OrderTaxiPage


@allure.title('Тестовые сценарии блока заказа такси')
class TestRouteSelectionPage:
    
    @allure.title('Проверка отображения блока заказа такси')
    @allure.description('Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный')
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
    @allure.description('При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ') 
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
        
    @allure.title('Проверка наличия элементов блока опций заказа')
    @allure.description('Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси') 
    def test_order_taxi_page_check_block_elements_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)
        
        assert order_taxi_page.is_options_block_elements_exists()
    
    @allure.title('Проверка наличия элементов блока ожидания заказа')
    @allure.description('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины (проверить элементы по ТЗ)') 
    def test_order_taxi_page_click_enter_number_and_order_button_show_awaiting_block_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)
        order_taxi_page.open_requirements_block()
        order_taxi_page.click_notebook_checkbox()
        order_taxi_page.click_enter_number_and_order_button()
        
        assert order_taxi_page.is_awaiting_block_elements_exists()
    
    @allure.title('Проверка наличия элементов блока деталей заказа')
    @allure.description('Дождаться окончания таймера поиска машины - Отображается окно совершенного заказа (проверить элементы по ТЗ)') 
    def test_order_taxi_page_click_enter_number_and_order_button_show_details_block_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)
        order_taxi_page.open_requirements_block()
        order_taxi_page.click_notebook_checkbox()
        payment_method = order_taxi_page.get_payment_method()
        order_taxi_page.click_enter_number_and_order_button()
        order_taxi_page.awaiting_order_details_block()
        order_taxi_page.click_order_details_button()
        
        assert order_taxi_page.is_order_details_block_elements_exists(payment_method)
    
    @allure.title('Проверка стоимости заказа в деталях заказа')
    @allure.description('Нажать кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа') 
    def test_order_taxi_page_order_cost_equal_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)
        order_cost = order_taxi_page.get_order_cost()
        order_taxi_page.click_enter_number_and_order_button()
        order_taxi_page.awaiting_order_details_block()
        order_taxi_page.click_order_details_button()
        
        assert order_taxi_page.is_order_cost_equal(order_cost)
        
    @allure.title('Проверка нажатия кнопки Отмена')
    @allure.description('Нажать кнопку Отмена - Окно закрывается') 
    @pytest.mark.xfail(reason="BUG: кнопка 'Отменить' блока деталей заказа не реагирует на нажатие")
    def test_order_taxi_page_cancel_order_details_block_hide_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route_addresses(ADDRESS_FROM, ADDRESS_TO)
        route_selection_page = RouteSelectionPage(driver)
        route_selection_page.switch_mode_to_fast()
        route_selection_page.start_ordering_taxi()
        
        order_taxi_page = OrderTaxiPage(driver)

        order_taxi_page.click_enter_number_and_order_button()
        order_taxi_page.awaiting_order_details_block()
        order_taxi_page.click_order_cancel_button()
        
        assert order_taxi_page.is_order_details_block_hide()