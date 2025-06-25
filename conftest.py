import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.auth import CREDENTIALS
from data.auth import login

@pytest.fixture(scope="session")
def config():
    return CREDENTIALS

@pytest.fixture(scope="function")
def driver():
    options = Options()
    drv = webdriver.Chrome(options=options)
    drv.maximize_window()
    yield drv
    drv.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver, config):
    """Залогиненный водитель."""
    login(driver, config)
    return driver

@pytest.fixture(scope="function")
def open_main(driver, config):
    """Открываем главную перед каждым тестом."""
    driver.get(config["base_url"])