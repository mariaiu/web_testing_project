from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_ITEM), \
            "Product item is presented, but should not be"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), \
            "Cart is't empty, but should be"

