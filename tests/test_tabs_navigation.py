import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://stellarburgers.nomoreparties.site")

    tabs = ["Булки", "Соусы", "Начинки"]

    for tab_name in tabs:
        tab = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='{tab_name}']/parent::div")))

        driver.execute_script("arguments[0].scrollIntoView(true);", tab)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='{tab_name}']/parent::div")))

        driver.execute_script("arguments[0].click();", tab)

        # Ждем появления активной вкладки
        active_tab = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='{tab_name}']/parent::div")))

        print(f"Активная вкладка сейчас: {tab_name}")

        time.sleep(2)  # пауза 2 секунды чтобы визуально увидеть переключение

    print("Тест пройден: переходы между вкладками работают корректно.")

finally:
    driver.quit()
