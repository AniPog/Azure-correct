import pytest
from selenium import webdriver
import logging
import os


@pytest.fixture()
def driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument ('--headless')
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    except Exception as e:
        raise Exception(e)

def pytest_configure():
    logging.basicConfig(
                        level=logging.INFO,
                        datefmt='%d-%b-%Y %H:%M:%S',
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        encoding='utf-8',
                        filename= os.path.join(os.path.join(os.path.dirname(__file__),"logs.txt")),
                        filemode='a+'
                        )