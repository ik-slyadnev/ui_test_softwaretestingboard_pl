import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Коллекции")
class TestCollectionsPage:
    @allure.story("Отображение товаров")
    @pytest.mark.smoke
    def test_products_display(self, collections_page):
        with allure.step("Открытие страницы коллекции"):
            collections_page.open()
            # collections_page.click_consent_button()

        with allure.step("Проверка наличия товаров"):
            products_count = collections_page.get_products_count()
            assert products_count > 0, "На странице нет товаров"

    @allure.story("Проверка выпадающего списка сортировки")
    @pytest.mark.regression
    def test_sort_dropdown_presence(self, collections_page):
        with allure.step("Открытие страницы коллекции"):
            collections_page.open()
            # collections_page.click_consent_button()

        with allure.step("Проверка видимости сортировки"):
            expect(collections_page.sorter).to_be_visible()

    @allure.story("Проверка заголовка страницы")
    @pytest.mark.regression
    def test_page_title(self, collections_page):
        with allure.step("Открытие страницы коллекции"):
            collections_page.open()
            # collections_page.click_consent_button()

        with allure.step("Проверка текста заголовка"):
            expect(collections_page.title).to_have_text("Eco Friendly")
