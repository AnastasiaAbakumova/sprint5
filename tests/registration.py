import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:

    @pytest.fixture(autouse=True)
    def open_main(self, driver, config):
        """Открываем главную до каждого теста этого класса."""
        driver.get(config["base_url"])

    def test_successful_registration(self, driver, config):
        wait = WebDriverWait(driver, 10)

        # 1) Нажимаем "Личный Кабинет"
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/account']"))).click()

        # 2) Нажимаем "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()

        # 3) Убедимся, что форма регистрации загрузилась
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Регистрация')]")
        ))

        # 4) Заполняем поля
        driver.find_element(By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")\
              .send_keys("Анастасия")
        driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")\
              .send_keys(config["username"])
        driver.find_element(By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")\
              .send_keys(config["password"])

        # 5) Сабмитим форму
        driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()

        # 6) Проверяем, что после регистрации нас перебросило на страницу логина
        assert wait.until(EC.url_contains("/login")), \
            "Ожидалось, что после успешной регистрации URL будет содержать '/login'"
