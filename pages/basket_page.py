from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_empty(self):
        self.should_be_empty_text()
        self.should_be_no_product_items()

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.IS_EMPTY), "Text about empty basket is not found"

    def should_be_no_product_items(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_ITEMS), "Cart items are found, but should not be"
