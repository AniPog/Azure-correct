import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helper import Helper

def test_auto(driver):
    search_input = (By.ID, "searchInp")
    results_count_span = (By.XPATH, "//button[@id='research-btn']//span")
    url = "https://auto.am/"
    car_brand = "KIA"
    search_auto_am = Helper(driver)
    possible_options = (By.XPATH, "//p[@class='inactiveAC']")

    # Navigate to the website
    search_auto_am.navigate_to_auto_am(url)
    logging.info("Navigated to {}".format(url))

    # Search for the car brand
    search_auto_am.search_car_brand(car_brand,search_input, possible_options)
    logging.info("Searching for car brand: {}".format(car_brand))

    # Wait for search results
    search_auto_am.wait_for_search_results(results_count_span)
    assert results_count_span!= "0"
    logging.info("Waiting for search results")


# TODO, keep test case file name no only test, instead like test_blabla
#Nel, code is correct, good for you