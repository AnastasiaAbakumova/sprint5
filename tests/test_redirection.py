import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.account_locators import AccountLocators

class TestAccountFlow:

    def test_redirection_to_account_from_main(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)

        # Клик по "Личный Кабинет"
        driver.find_element(*AccountLocators.ACCOUNT_LINK).click()

        # Проверяем, что URL содержит /account
        assert "/account" in driver.current_url, (
            f"Ожидали '/account' в URL, получили: {driver.current_url}"
        )

    def test_redirection_to_constructor(self, logged_in_driver, config):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)

        # Переходим в профиль
        driver.find_element(*AccountLocators.ACCOUNT_LINK).click()

        # Ждём исчезновения оверлея (если он есть)
        wait.until(EC.invisibility_of_element_located(AccountLocators.MODAL_OVERLAY))

        # Клик по "Конструктор"
        driver.find_element(*AccountLocators.CONSTRUCTOR_LINK).click()

        # Проверяем, что вернулись на главную (base_url)
        expected = config["base_url"].rstrip("/")
        actual = driver.current_url.rstrip("/")
        assert actual == expected, (
            f"Ожидали URL главной {expected}, получили: {actual}"
        )

    def test_exit_account(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)

        # Переходим в профиль
        driver.find_element(*AccountLocators.ACCOUNT_LINK).click()

        # Ждём кнопку "Выход" и кликаем
        logout = wait.until(EC.element_to_be_clickable(AccountLocators.LOGOUT_BUTTON))
        logout.click()

        # Ждём редирект на страницу логина
        wait.until(EC.url_contains("/login"))

        assert "/login" in driver.current_url, (
            f"Ожидали '/login' в URL после выхода, получили: {driver.current_url}"
        )
