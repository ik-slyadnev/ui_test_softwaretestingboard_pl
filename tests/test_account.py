import allure
import pytest
from utils.user_data import Users
from playwright.sync_api import expect


@allure.feature("Регистрация")
class TestRegistrationPage:
    @allure.story("Успешная регистрация")
    @pytest.mark.smoke
    def test_valid_registration(self, account_page):
        with allure.step("Открытие страницы регистрации"):
            account_page.open()
            # account_page.click_consent_button()

        with allure.step("Заполнение формы регистрации"):
            account_page.create_account(
                firstname=Users.firstname,
                lastname=Users.lastname,
                email=Users.email,
                password=Users.password,
            )

        with allure.step("Проверка успешного сообщения"):
            expect(account_page.success).to_be_visible()

    @allure.story("Ошибка при коротком пароле")
    @pytest.mark.regression
    def test_short_password(self, account_page):
        with allure.step("Открытие страницы регистрации"):
            account_page.open()
            # account_page.click_consent_button()

        with allure.step("Заполнение формы с коротким паролем"):
            account_page.create_account(
                firstname=Users.firstname,
                lastname=Users.lastname,
                email=Users.email,
                password="lol",
            )

        with allure.step("Проверка ошибки пароля"):
            expect(account_page.password_error).to_have_text(
                "Minimum length of this field must be equal or greater "
                "than 8 symbols. Leading and trailing spaces will be "
                "ignored."
            )

    @allure.story("Ошибка при пустом email")
    @pytest.mark.regression
    def test_empty_email(self, account_page):
        with allure.step("Открытие страницы регистрации"):
            account_page.open()
            # account_page.click_consent_button()

        with allure.step("Заполнение формы с пустым email"):
            account_page.create_account(
                firstname=Users.firstname,
                lastname=Users.lastname,
                email=" ",
                password=Users.password,
            )

        with allure.step("Проверка ошибки email"):
            expect(account_page.email_error).to_have_text(
                "This is a required field."
            )
