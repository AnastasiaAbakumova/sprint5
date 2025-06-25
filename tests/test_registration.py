import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.account_locators import AccountLocators

class TestRegistration:

    def test_successful_registration(self, driver, config, open_main):
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(
            AccountLocators.ACCOUNT_LINK
        )).click()

        wait.until(EC.element_to_be_clickable(
            AccountLocators.REGISTER_LINK
        )).click()

        wait.until(EC.visibility_of_element_located(
            AccountLocators.REGISTER_HEADER
        ))

        driver.find_element(*AccountLocators.NAME_INPUT).send_keys("Анастасия")
        driver.find_element(*AccountLocators.EMAIL_INPUT).send_keys(config["username"])
        driver.find_element(*AccountLocators.PASSWORD_INPUT).send_keys(config["password"])

        driver.find_element(*AccountLocators.REGISTER_BUTTON).click()

        assert wait.until(EC.url_contains("/login")), (
            f"Ожидали, что после регистрации URL будет содержать '/login', но получили: {driver.current_url}"
        )