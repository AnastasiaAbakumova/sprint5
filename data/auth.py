from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators

def login(driver, config):
    driver.get(config["base_url"])
    driver.find_element(*LoginLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginLocators.NAME_INPUT).send_keys(config["username"])
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(config["password"])
    driver.find_element(*LoginLocators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.PROFILE_LINK)
    )

CREDENTIALS = {
    "base_url": "https://stellarburgers.nomoreparties.site",
    "username": "anastasiaabakumova25331@yandex.ru",
    "password": "@anAstas777"
}
