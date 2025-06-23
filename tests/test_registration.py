import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.account_locators import AccountLocators

class TestRegistration:

    @pytest.fixture(autouse=True)
    def open_main(self, driver, config):
        """Открываем главную перед каждым тестом."""
        driver.get(config["base_url"])

    def test_successful_registration(self, driver, config):
        wait = WebDriverWait(driver, 10)

        # 1) Переходим в форму регистрации: Личный кабинет → Зарегистрироваться
        wait.until(EC.element_to_be_clickable(
            AccountLocators.ACCOUNT_LINK
        )).click()
        wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Зарегистрироваться")
        )).click()

        # 2) Ждём, что загрузится заголовок формы "Регистрация"
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Регистрация')]")
        ))

        # 3) Заполняем поля через XPATH по тексту лейблов
        driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input")\
            .send_keys("Анастасия")
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")\
            .send_keys(config["username"])
        driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")\
            .send_keys(config["password"])


        # 4) Сабмитим форму
        driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()

        # 5) Проверяем, что URL содержит '/login'
        assert wait.until(EC.url_contains("/login")), (
            f"Ожидали, что после регистрации URL будет содержать '/login', но получили: {driver.current_url}"
        )
