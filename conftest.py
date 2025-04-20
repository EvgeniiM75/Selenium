from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    options = Options()                      # Для невидимого запуска браузера
    options.add_argument('--headless')       #  Для невидимого запуска браузера
    driver=webdriver.Chrome(options=options) # Для невидимого запуска браузера
    #driver = webdriver.Chrome()               # Предусловие
    driver.maximize_window()
    driver.implicitly_wait(3) # Ждем загрузки элементов
    yield driver
    driver.close()            # Постусловие
