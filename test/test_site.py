from selenium import webdriver

import pytest
import time
from pages.product import ProductPage
from pages.homepage import Homepage


def test_open_s6(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')

def test_open_monitor(driver):
    homepage = Homepage(driver)
    homepage.open()
    # driver.get('https://demoblaze.com/')
    homepage.click_monitor()
    # monit=driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    # monit.click()
    time.sleep(3)
    homepage.check_products_count(2)
    # monitors = driver.find_elements(By.CSS_SELECTOR,'.card')
    # assert len(monitors) == 2