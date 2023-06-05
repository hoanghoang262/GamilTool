"""Sumary: Provider ChromeControler class"""

from selenium import webdriver
from Enum.chome_controler import (
    CHROME_DRIVER_PATH,
    CHROME_START_PATH,
    CHROME_OPTIONS_PARAM,
)
from Util.chrome_controler import add_list_of_experimental_options


class ChromeControler:
    """CHROME_CONTROLER is a class provide feature to auto control chrome web browser"""

    def __init__(self) -> None:
        self.driver = None

    def open_start_window(self):
        """Open chrome start window"""
        # REVIEW - setup chrome option
        chrome_options = webdriver.ChromeOptions()
        add_list_of_experimental_options(chrome_options, CHROME_OPTIONS_PARAM)

        # REVIEW - Create chrome driver to control chrome
        self.driver = webdriver.Chrome(
            executable_path=CHROME_DRIVER_PATH, options=chrome_options
        )

        # REVIEW - Open chrome i forward it to start URL
        self.driver.get(CHROME_START_PATH)
