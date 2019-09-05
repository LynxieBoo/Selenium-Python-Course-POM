from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[contains(@class, "basket")]')
    PRODUCT_NAME_ALERT = (By.XPATH, '//div[@class="alertinner " ]/strong[1]')
    TOTAL_PRICE_ALERT = (By.XPATH, '//div[@class="alertinner "]/p[1]')
    TOTAL_PRICE_BASKET_MINI = (By.XPATH, '//div[contains(@class,"basket-mini")]')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"product_main")]/p[@class="price_color"]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
