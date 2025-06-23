import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.tab_locators import TabLocators

class TestTabsNavigation:

    @pytest.fixture(autouse=True)
    def open_main(self, driver, config):
        """Открываем главную страницу перед тестами."""
        driver.get(config['base_url'])

    def test_tabs_switching(self, driver):
        wait = WebDriverWait(driver, 10)
        tabs = [TabLocators.BUNS, TabLocators.SAUCES, TabLocators.FILLINGS]

        for tab_locator, active_locator in tabs:
            # Кликаем по табу
            tab = wait.until(EC.presence_of_element_located(tab_locator))
            driver.execute_script("arguments[0].scrollIntoView(true);", tab)
            wait.until(EC.element_to_be_clickable(tab_locator))
            driver.execute_script("arguments[0].click();", tab)

            # Проверяем, что таб активировался
            active = wait.until(EC.presence_of_element_located(active_locator))
            assert active.is_displayed(), f"Таб {active_locator} не активен после клика"
