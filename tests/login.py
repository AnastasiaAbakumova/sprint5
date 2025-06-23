import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def perform_login(self, driver, config):
        driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys(config["username"])
        driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(config["password"])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    def test_login_mainpage(self, driver, config):
        driver.get(config["base_url"])

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        self.perform_login(driver, config)

        # Ждем появления элемента, доступного только после входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()

    def test_login_mainpage_header(self, driver, config):
        driver.get(config["base_url"])

        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        self.perform_login(driver, config)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()

    def test_login_page_register(self, driver, config):
        driver.get(config["base_url"])

        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        self.perform_login(driver, config)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()

    def test_login_forgot_password(self, driver, config):
        driver.get(config["base_url"])

        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        driver.find_element(By.XPATH, "//a[@href='/forgot-password']").click()
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        self.perform_login(driver, config)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()
