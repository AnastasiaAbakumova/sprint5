import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@ pytest.fixture(scope="session")
def config():
    """
    Фикстура конфигурации: возвращает параметры для логина и пароля.
    Можно легко расширить для чтения из файла или переменных окружения.
    """
    return {
        "base_url": "https://stellarburgers.nomoreparties.site",
        "username": "anastasiaabakumova25331@yandex.ru",
        "password": "@anAstas777"
    }

@ pytest.fixture(scope="function")
def driver():
    options = Options()
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()



@pytest.fixture(scope="function")
def logged_in_driver(driver, config):
    driver.get(config["base_url"])
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    
    # Вводим логин и пароль
    driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys(config["username"])
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(config["password"])
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    # Ждём, пока загрузится личный кабинет (например, появится ссылка "Личный Кабинет")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/account']"))
    )
    
    yield driver  # возвращаем залогиненный драйвер