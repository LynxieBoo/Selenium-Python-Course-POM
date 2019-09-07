import pytest
import random
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
urls[7] = pytest.param(
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    marks=pytest.mark.xfail
)


# @pytest.mark.parametrize('link', urls)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link=urls[0]):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=urls[0]):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link=urls[0]):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link=urls[0]):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link=urls[0]):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.go_to_cart_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_empty()


def generate_new_user():
    email_len = random.randint(7, 10)
    pwd_len = random.randint(10, 15)
    email_chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pwd_chars = email_chars + '+-/*!&$#?=@<>1234567890'
    email = ''.join(random.choices(email_chars, k=email_len)) + '@fakemail.com'
    password = ''.join(random.choices(pwd_chars, k=pwd_len))
    return email, password


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        while True:
            email, password = generate_new_user()
            if login_page.register_new_user(email, password):
                break
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link=urls[0]):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link=urls[0]):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
