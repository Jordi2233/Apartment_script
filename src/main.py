#!/usr/bin/env python3
import os
import time
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Browser:

    def __init__(self) -> None:
        self.browser = self.create_driver()

    def create_driver(self) -> webdriver.Chrome:
        path = os.popen("which chromedriver").read().strip()
        service = ChromeService(executable_path=path)
        return webdriver.Chrome(service=service)


    def find_elements(self) -> list:
        self.browser.get('https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/wroclaw/q-mieszkanie/?search%5Bfilter_float_price:to%5D=2500&search%5Bfilter_enum_furniture%5D%5B0%5D=yes')
        return self.browser.find_elements(By.CLASS_NAME, 'css-10b0gli')

def main():
    os.system('clear')
    prices = list(map(lambda x: x.text, Browser().find_elements()))
    print(colored(f'Prices: {prices}', 'green'))


if __name__ == '__main__':
    main()


# https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/wroclaw/?search%5Border%5D=filter_float_price:asc
