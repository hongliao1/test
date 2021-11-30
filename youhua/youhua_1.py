import logging

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def browser(value='Chrome'):
    try:
        return getattr(webdriver, value)()
    except Exception as i:
        print(i)
        return webdriver.Chrome()


class DataBase():
    url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = browser()
        else:
            self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def max_window(self, txt):
        self.driver.maximize_window()

    def min_window(self):
        self.driver.minimize_window()

    def open(self):
        self.driver.get(self.url)

    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator, tuple):
            element = self.driver.find_element(*locator)
        else:
            element = self.driver.find_element(locator, value)
        return element

    def find_and_get_text(self, locator, value: str = None):
        # element: WebElement
        if isinstance(locator, tuple):
            element_text = self.driver.find_element(*locator).text
        else:
            element_text = self.driver.find_element(locator, value)

        return element_text

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if 'click' == step['operation']:
                self.find(step['by'], step['location']).click()
            if 'input' == step['operation']:
                self.find(step['by'], step['location']).send_keys(step['input'])
