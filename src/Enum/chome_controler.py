"""Sumary: This module provides num variant for CHROME CONTROLER"""

# REVIEW -  Set the path to the ChromeDriver executable
CHROME_DRIVER_PATH = r"/home/hoanghoang262/Documents/chromedriver_linux64/chromedriver"

# REVIEW -  Chrome option param
CHROME_OPTIONS_PARAM = {
    # NOTE - This option make chrome dont auto close when test done
    "detach": True
}

# REVIEW -  Chrome start path
CHROME_START_PATH = "https://fap.fpt.edu.vn"
