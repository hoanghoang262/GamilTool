"""This module provide funtion use in ChromeControler class"""


def add_list_of_experimental_options(chrome_options, experimental_options: dict):
    """This funtion take a list of experimental options and add it to webdriver setup"""
    experimental_option_list = experimental_options.items()
    for key, value in experimental_option_list:
        chrome_options.add_experimental_option(key, value)
