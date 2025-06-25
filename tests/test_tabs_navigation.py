import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.tab_locators import TabLocators

@pytest.mark.parametrize("tab_locator, active_locator", [
    (TabLocators.BUNS_TAB, TabLocators.BUNS_TAB_ACTIVE),
    (TabLocators.SAUCES_TAB, TabLocators.SAUCES_TAB_ACTIVE),
    (TabLocators.FILLINGS_TAB, TabLocators.FILLINGS_TAB_ACTIVE),
])
class TestTabsNavigation:

    def test_tab_switching(self, driver, open_main, tab_locator, active_locator):
        wait = WebDriverWait(driver, 10)

        tab = wait.until(EC.presence_of_element_located(tab_locator))
        driver.execute_script("arguments[0].scrollIntoView(true);", tab)
        wait.until(EC.element_to_be_clickable(tab_locator))
        driver.execute_script("arguments[0].click();", tab)

        active = wait.until(EC.presence_of_element_located(active_locator))
        assert active.is_displayed(), f"Таб {active_locator} не активен после клика"
