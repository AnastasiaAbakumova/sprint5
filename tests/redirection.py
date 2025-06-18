import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_redirection_to_account_from_main(logged_in_driver):
    driver = logged_in_driver

    # Клик по кнопке "Личный Кабинет"
    driver.find_element(By.XPATH, "//a[@href='/account']").click()

    # Проверяем, что перешли на страницу профиля
    assert "/account" in driver.current_url


def test_redirection_Constructor(logged_in_driver):
    driver = logged_in_driver

    # Клик по кнопке "Личный Кабинет"
    driver.find_element(By.XPATH, "//a[@href='/account']").click()

    # Клик по кнопке "Конструктор"
    driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()

    # Проверяем, что перешли на страницу Конструктора
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_exit_account(logged_in_driver):
    driver = logged_in_driver

    # Клик по кнопке "Личный Кабинет"
    driver.find_element(By.XPATH, "//a[@href='/account']").click()

    # Явно ждем появления кнопки "Выход"
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
    )

    logout_button.click()

    # Ждём редирект на страницу логина
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    assert "/login" in driver.current_url