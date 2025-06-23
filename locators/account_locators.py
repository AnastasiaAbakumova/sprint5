from selenium.webdriver.common.by import By

class AccountLocators:
    ACCOUNT_LINK       = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_LINK   = (By.XPATH, "//p[text()='Конструктор']")
    LOGOUT_BUTTON      = (By.XPATH, "//button[contains(text(), 'Выход')]")
