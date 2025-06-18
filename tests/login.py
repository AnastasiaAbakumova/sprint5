import pytest
from selenium.webdriver.common.by import By
import time


def perform_login(driver, config):
    """
    Хелпер для логина: вводит логин/пароль и нажимает кнопку.
    Предполагает, что уже открыта страница логина.
    """
    driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys(config["username"])
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(config["password"])
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    

def test_login_mainpage(driver, config):
    driver.get(config["base_url"])

    # Клик по кнопке "Войти в аккаунт" на главной
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    perform_login(driver, config)
    time.sleep(3)


def test_login_mainpage_header(driver, config):
    driver.get(config["base_url"])

    # Клик по кнопке "Личный Кабинет" на главной
    driver.find_element(By.XPATH, "//a[@href='/account']").click()
    perform_login(driver, config)
    time.sleep(3)

def test_login_page_register(driver, config):
    driver.get(config["base_url"])

    # Клик по кнопке "Личный Кабинет" на главной
    driver.find_element(By.XPATH, "//a[@href='/account']").click()
    # Клика по ссылке «Зарегистрироваться»
    driver.find_element(By.XPATH, "//a[@href='/register']").click()
    # Клика по ссылке «Войти»
    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    perform_login(driver, config)
    time.sleep(3)

def test_login_forgot_password(driver, config):
    driver.get(config["base_url"])

    # Клик по кнопке "Личный Кабинет" на главной
    driver.find_element(By.XPATH, "//a[@href='/account']").click()
    # Клика по ссылке «Восстановить пароль»
    driver.find_element(By.XPATH, "//a[@href='/forgot-password']").click()
    # Клика по ссылке «Войти»
    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    perform_login(driver, config)
    time.sleep(3)