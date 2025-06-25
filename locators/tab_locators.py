from selenium.webdriver.common.by import By

class TabLocators:
    # Булки
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']/parent::div")
    BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']/parent::div")

    # Соусы
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']/parent::div")
    SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']/parent::div")

    # Начинки
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']/parent::div")
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']/parent::div")