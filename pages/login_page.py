from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def input_data_to_register_form_and_click_button(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(str(email))
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(str(password))
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(str(password))
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def is_registration_passed(self):
        if self.is_element_present(*LoginPageLocators.REGISTER_PASSED):
            return True
        elif self.is_element_present(*LoginPageLocators.REGISTER_FAILED):
            return False
        else:
            assert False, "There is no reaction on registration actions, but it should be"

    def register_new_user(self, email, password):
        self.should_be_register_elements()
        self.input_data_to_register_form_and_click_button(email, password)
        return self.is_registration_passed()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'Login' is not presented in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"

    def should_be_register_confirm_password(self):
        warning = 'Confirm password field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), warning

    def should_be_register_elements(self):
        self.should_be_register_email()
        self.should_be_register_password()
        self.should_be_register_confirm_password()
        self.should_be_register_button()

    def should_be_register_email(self):
        warning = 'Name field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), warning

    def should_be_register_password(self):
        warning = 'Password field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), warning

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
