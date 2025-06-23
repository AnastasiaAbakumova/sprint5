from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PROFILE_LINK = (By.XPATH, "//a[@href='/account']")
