from selenium.webdriver.common.by import By

class AccountLocators:
    ACCOUNT_LINK       = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_LINK   = (By.XPATH, "//p[text()='Конструктор']")
    LOGOUT_BUTTON      = (By.XPATH, "//button[contains(text(), 'Выход')]")
    MODAL_OVERLAY      = (By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")
    
    # Для регистрации
    REGISTER_LINK      = (By.LINK_TEXT, "Зарегистрироваться")
    REGISTER_HEADER    = (By.XPATH, "//h2[contains(text(), 'Регистрация')]")
    NAME_INPUT         = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT        = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT     = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON    = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
