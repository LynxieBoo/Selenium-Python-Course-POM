from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_PASSWORD = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
    REGISTER_FAILED = (By.XPATH, '//div[@class="alert alert-danger"]')
    REGISTER_PASSED = (By.XPATH, '//div[contains(@class,"alert-success")]')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[contains(@class, "basket")]')
    PRODUCT_NAME_ALERT = (By.XPATH, '//div[@class="alertinner " ]/strong[1]')
    TOTAL_PRICE_ALERT = (By.XPATH, '//div[@class="alertinner "]/p[1]')
    TOTAL_PRICE_BASKET_MINI = (By.XPATH, '//div[contains(@class,"basket-mini")]')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"product_main")]/p[@class="price_color"]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains (@class,"alert-success")][1]')


class BasketPageLocators:
    IS_EMPTY = (By.XPATH, '//*[contains(text(),"Your basket is empty")]')
    CART_ITEMS = (By.XPATH, '//div[@class="basket-items"]')
