from .base_page import BasePage, get_one_price_from_string
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.should_be_promo_url()
        self.should_be_add_to_cart_button()
        self.click_add_product_to_cart_button()
        self.solve_quiz_and_get_code()
        self.should_be_same_product_names()
        self.should_be_same_cart_and_product_cost()

    def should_be_promo_url(self):
        assert 'promo=' in self.browser.current_url, "'promo=' is not presented in URL"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "'Add to cart' button is not presented"

    def click_add_product_to_cart_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_same_product_names(self):
        self.should_be_alert_product_name()
        self.should_be_main_product_name()
        self.check_same_product_names()

    def should_be_same_cart_and_product_cost(self):
        self.should_be_main_product_price()
        self.should_be_mini_cart_cost()
        self.should_be_alert_cart_cost()
        self.check_same_cart_and_product_cost()

    def should_be_alert_product_name(self):
        warning = "Alert with product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT), warning

    def should_be_main_product_name(self):
        warning = "Main product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), warning

    def check_same_product_names(self):
        main_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        warning = 'Product name in the cart and on the main field are different'
        assert main_product_name == alert_product_name, warning

    def should_be_main_product_price(self):
        warning = "Main product price is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), warning

    def should_be_mini_cart_cost(self):
        warning = "Mini cart cost is not presented"
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_BASKET_MINI), warning

    def should_be_alert_cart_cost(self):
        warning = "Alert cart cost is not presented"
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_ALERT), warning

    def check_same_cart_and_product_cost(self):
        main_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        main_product_price = get_one_price_from_string(main_product_price)
        alert_cart_cost = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_ALERT).text
        alert_cart_cost = get_one_price_from_string(alert_cart_cost)
        mini_cart_cost = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_BASKET_MINI).text
        mini_cart_cost = get_one_price_from_string(mini_cart_cost)

        warning = 'Product price, cost in the mini cart and in the alert field are different'
        assert main_product_price == alert_cart_cost == mini_cart_cost, warning

    def should_not_be_success_message(self):
        warning = "Success message is presented, but should not be"
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), warning

    def should_disappear_success_message(self):
        warning = "Success message is presented, but should disappear"
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), warning
