from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRMATION_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-lg.btn-primary")


class ProductPageLocators(object):
    ADDING_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDING_MESSAGE = (By.CSS_SELECTOR, ".alert-success.fade.in .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info.fade.in .alertinner p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    PRODUCT_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
