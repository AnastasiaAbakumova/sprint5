from selenium.webdriver.common.by import By

class TabLocators:
    BUNS = (
        (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']/parent::div"),
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']/parent::div"),
    )
    SAUCES = (
        (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']/parent::div"),
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']/parent::div"),
    )
    FILLINGS = (
        (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']/parent::div"),
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']/parent::div"),
    )
