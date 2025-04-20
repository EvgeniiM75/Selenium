from selenium.webdriver.common.by import By

class Homepage:

    def __init__(self,driver):
        self.driver = driver
    def open(self):
        self.driver.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        gal_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        gal_s6.click()

    def click_monitor(self):
        monit = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monit.click()

    def check_products_count(self,count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count