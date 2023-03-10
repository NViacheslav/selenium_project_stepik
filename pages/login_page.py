from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.resource = "login"
        assert self.resource in self.browser.current_url, f"expected '{self.resource}' to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"
    
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "password"
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)
        password_conf_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_INPUT)
        password_conf_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
