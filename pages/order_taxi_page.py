import allure
from pages.base_page import BasePage
from locators.general_locators import GeneralLocators
from locators.order_taxi_page_locators import OrderTaxiPageLocators
from data import TARIFFS


class OrderTaxiPage(BasePage):
    
    @allure.step('Проверка соответствия названий тарифов по ТЗ')
    def is_tariff_titles_match(self) -> bool:
        elements = self.find_visible_elements(OrderTaxiPageLocators.DIV_TARIFF_TITLES)
        return all([element.text in TARIFFS.keys() for element in elements])
    
    @allure.step('Получение количества активных тарифов')
    def count_of_active_tariffs(self):
        return len(self.find_visible_elements(OrderTaxiPageLocators.DIV_TCARD_ACTIVE))
    
    @allure.step('Получить информацию по тарифу')
    def get_tariff_information_by_name(self, tariff_name):
        elements = self.find_visible_elements(OrderTaxiPageLocators.DIV_TARIFF_TITLES)
        for element in elements:
            if element.text == tariff_name:
                element.click()
                break
        
        self.move_to_element(OrderTaxiPageLocators.BUTTON_TARIFF_INFO)
        return self.get_text_from_element(OrderTaxiPageLocators.DIV_ACTIVE_TARIFF_DESCRIPTION)
        
    @allure.step('Сравнение текстового сообщения результата с ожидаемым текстом')
    def is_block_elements_exists(self):
        conditions = [
            self.find_visible_element(OrderTaxiPageLocators.DIV_PHONE),
            self.find_visible_element(OrderTaxiPageLocators.DIV_PAYMENT_METHOD),
            self.find_visible_element(OrderTaxiPageLocators.INPUT_COMMENT),
            self.find_visible_element(OrderTaxiPageLocators.DIV_REQUIREMENTS)
            ]
        return all(conditions)
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(OrderTaxiPageLocators.DIV_ORDER_BLOCK_SHOW)
        ]
        return all(conditions)