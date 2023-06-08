"""This module provide funtion use in ChromeControler class"""
from selenium.webdriver.chrome.options import Options


def add_list_of_experimental_options(chrome_options: Options, options: dict):
    """This funtion take a list of experimental options and add it to webdriver setup"""
    # REVIEW - add exprimental options
    option_list = options["experimentals"].items()
    for key, value in option_list:
        chrome_options.add_experimental_option(key, value)
    # REVIEW - Add argument options
    for argument in options["arguments"]:
        chrome_options.add_argument(argument)
