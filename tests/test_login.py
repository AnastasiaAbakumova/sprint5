import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from data.auth import login


class TestLogin:

    def test_login_mainpage(self, driver, config):
        """Тест входа через кнопку 'Войти в аккаунт' на главной странице."""
        login(driver, config)  # используем общий хелпер

        # Проверяем, что появилась ссылка "Личный Кабинет"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.PROFILE_LINK)
        )
        assert driver.find_element(*LoginLocators.PROFILE_LINK).is_displayed()

    def test_login_mainpage_header(self, driver, config):
        """Тест входа через 'Личный кабинет' в шапке сайта."""
        driver.get(config["base_url"])
        driver.find_element(*LoginLocators.PROFILE_LINK).click()
        login(driver, config)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.PROFILE_LINK)
        )
        assert driver.find_element(*LoginLocators.PROFILE_LINK).is_displayed()

    def test_login_page_register(self, driver, config):
        """Тест входа через переход с регистрации."""
        driver.get(config["base_url"])
        driver.find_element(*LoginLocators.PROFILE_LINK).click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "//a[@href='/login']").click()

        login(driver, config)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.PROFILE_LINK)
        )
        assert driver.find_element(*LoginLocators.PROFILE_LINK).is_displayed()

    def test_login_forgot_password(self, driver, config):
        """Тест входа через переход с восстановления пароля."""
        driver.get(config["base_url"])
        driver.find_element(*LoginLocators.PROFILE_LINK).click()
        driver.find_element(By.XPATH, "//a[@href='/forgot-password']").click()
        driver.find_element(By.XPATH, "//a[@href='/login']").click()

        login(driver, config)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.PROFILE_LINK)
        )
        assert driver.find_element(*LoginLocators.PROFILE_LINK).is_displayed()
