from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_registration():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    try:
        # 1. Клик на кнопку "Личный Кабинет"
        account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/account']"))
        )
        account_button.click()
        
        # 2. Клик на кнопку "Зарегистрироваться"
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        )
        register_button.click()
        
        # 3. Ожидание загрузки формы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Регистрация')]"))
        )
        
        # 4. Заполнение формы (используем XPath по тексту лейблов)
        name_field = driver.find_element(By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
        email_field = driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
        password_field = driver.find_element(By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
        
        # Ввод тестовых данных
        name_field.send_keys("Анастасия")
        email_field.send_keys("anastasiaabakumova25331@yandex.ru")
        password_field.send_keys("@anAstas777")
        time.sleep(1)
        submit_button.click()
        
        # 5. Проверка успешной регистрации
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        print("✅ Регистрация прошла успешно")
        
        
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    test_registration()