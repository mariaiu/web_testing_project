from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADDING_BUTTON)
        add_button.click()

    def should_be_add_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDING_MESSAGE), "Adding message is't presented"

    def should_be_right_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        adding_message = self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE).text
        assert product_name+" has been added to your basket." == adding_message, "Wrong product's name in the message"

    def should_be_cost_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), "Cost message is't presented"

    def should_be_right_cost_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert "Your basket total is now " + product_price == price_message, "Wrong price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING_MESSAGE), \
            "Adding message is presented, but should not be"

    def should_message_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_MESSAGE), \
            "Adding message is not disappeared, but should be "
