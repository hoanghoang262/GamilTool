"""Sumary: Provider ChromeControler class"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Enum.chome_controler_enum import (
    CHROME_EXECUTABLE_PATH,
    CHROME_START_PATH,
    CHROME_OPTIONS_PARAM,
)
from Util.chrome_controler_utils import add_list_of_experimental_options
import sys


class ChromeControler:
    """CHROME_CONTROLER is a class provide feature to auto control chrome web browser"""

    def __init__(self) -> None:
        self.driver = None

    def open_start_window(self):
        """Open chrome start window"""
        # REVIEW - setup chrome option
        chrome_options: Options = Options()
        add_list_of_experimental_options(chrome_options, CHROME_OPTIONS_PARAM)

        # REVIEW - Create chrome driver to control chrome
        self.driver = webdriver.Chrome(
            executable_path=CHROME_EXECUTABLE_PATH, options=chrome_options
        )

        # Wait until the profile has changed

        # REVIEW - Open chrome i forward it to start URL
        self.driver.get(CHROME_START_PATH)

    def close_Chrome(self):
        self.driver.quit()
        sys.exit()
