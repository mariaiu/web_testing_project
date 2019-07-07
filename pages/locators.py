from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADDING_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDING_MESSAGE = (By.CSS_SELECTOR, ".alert-success.fade.in .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info.fade.in .alertinner p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
