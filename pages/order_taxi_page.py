import allure
from pages.base_page import BasePage
from locators.general_locators import GeneralLocators
from locators.order_taxi_page_locators import OrderTaxiPageLocators
from data import TARIFFS, AWAITING_BLOCK_TITLE, ADDRESS_FROM, ADDRESS_TO, DETAILS_BLOCK_INFORMATION_COST


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
        
    @allure.step('Проверка наличия элементов блока опций')
    def is_options_block_elements_exists(self):
        conditions = [
            self.find_visible_element(OrderTaxiPageLocators.DIV_PHONE),
            self.find_visible_element(OrderTaxiPageLocators.DIV_PAYMENT_METHOD),
            self.find_visible_element(OrderTaxiPageLocators.INPUT_COMMENT),
            self.find_visible_element(OrderTaxiPageLocators.DIV_REQUIREMENTS)
            ]
        return all(conditions)
    
    @allure.step('Развернуть блок с рекомендациями')
    def open_requirements_block(self):
        self.click_to_element(OrderTaxiPageLocators.DIV_REQUIREMENTS)
        
    @allure.step('Выбрать чекбокс ноутбука')
    def click_notebook_checkbox(self):
        self.click_to_element(OrderTaxiPageLocators.SPAN_NOTEBOOK_CHECKBOX)
    
    @allure.step('Нажать кнопку Ввести номер и заказать')
    def click_enter_number_and_order_button(self):
        self.click_to_element(OrderTaxiPageLocators.BUTTON_ENTER_NUMBER_AND_ORDER)
    
    @allure.step('Проверка наличия элементов блока ожидания заказа')
    def is_awaiting_block_elements_exists(self):
        conditions = [
            self.find_visible_element(OrderTaxiPageLocators.DIV_ORDER_BODY),
            self.get_text_from_element(OrderTaxiPageLocators.DIV_AWAITING_HEADER_TITLE) == AWAITING_BLOCK_TITLE,
            self.find_visible_element(OrderTaxiPageLocators.DIV_AWAITING_HEADER_TIME),
            self.find_visible_element(OrderTaxiPageLocators.BUTTON_DETAILS),
            self.find_visible_element(OrderTaxiPageLocators.BUTTON_CANCEL)
            ]
        return all(conditions)
    
    @allure.step('Ожидать появления блока деталей заказа')
    def awaiting_order_details_block(self):
        self.awaiting_for_text_changing(OrderTaxiPageLocators.DIV_AWAITING_HEADER_TIME, "00:00")
        time = self.get_text_from_element(OrderTaxiPageLocators.DIV_AWAITING_HEADER_TIME)
        if time:
            parts = time.split(':')
            minutes = int(parts[0])
            seconds = int(parts[1])
            self.awaiting_for_visibility_by_time(minutes * 60 + seconds, OrderTaxiPageLocators.DIV_CAR_NUMBER)
    
    @allure.step('Кликнуть на кнопку Детали')
    def click_order_details_button(self):
        self.click_to_element(OrderTaxiPageLocators.BUTTON_DETAILS)
        
    @allure.step('Кликнуть на кнопку Отмена')
    def click_order_cancel_button(self):
        self.click_to_element(OrderTaxiPageLocators.BUTTON_CANCEL)
    
    @allure.step('Проверка, что окно деталей заказа исчезло')
    def is_order_details_block_hide(self):
        try:
            self.wait_for_invisibility(OrderTaxiPageLocators.BUTTON_CANCEL)
            return True
        except:
            return False
    
    @allure.step('Проверка наличия элементов блока деталей заказа')
    def is_order_details_block_elements_exists(self, payment_method):
        conditions = [
            self.get_text_from_element(OrderTaxiPageLocators.DIV_DETAILS_FROM) == ADDRESS_FROM,
            self.get_text_from_element(OrderTaxiPageLocators.DIV_DETAILS_TO) == ADDRESS_TO,
            self.get_text_from_element(OrderTaxiPageLocators.DIV_DETAILS_PAYMENT_METHOD) == payment_method,
            DETAILS_BLOCK_INFORMATION_COST in self.get_text_from_element(OrderTaxiPageLocators.DIV_DETAILS_INFORMATION_COST) # type: ignore
        ]
        return all(conditions)
    
    @allure.step('Получить способ оплаты')
    def get_payment_method(self):
        return self.get_text_from_element(OrderTaxiPageLocators.DIV_PAYMENT_METHOD_TITLE)
    
    @allure.step('Получить способ оплаты')
    def get_order_cost(self):
        return self.get_text_from_element(OrderTaxiPageLocators.DIV_TCARD_ACTIVE_PRICE)
    
    @allure.step('Проверить, что стоимость заказа в Деталях заказа соответствует изначальной')
    def is_order_cost_equal(self, order_cost):
        details_order_cost = self.get_text_from_element(OrderTaxiPageLocators.DIV_DETAILS_INFORMATION_COST).replace('Стоимость - ', '').replace('₽', '') # type: ignore
        return details_order_cost == order_cost.replace(' ₽', '')
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(OrderTaxiPageLocators.DIV_ORDER_BLOCK_SHOW)
        ]
        return all(conditions)