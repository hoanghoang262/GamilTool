"""Sumary: This module provides num variant for CHROME CONTROLER"""

# REVIEW -  Set the path to the ChromeDriver executable this use for execute driver not use any more
# STUB - Ubuntu path
# CHROME_DRIVER_PATH = r"/home/hoanghoang262/Documents/chromedriver_linux64/chromedriver"
# STUB - Window path
# CHROME_DRIVER_PATH = (
#     r"C:\Users\hoang\Documents\ChomeDriver\ChromeDriver_113\chromedriver.exe"
# )

# REVIEW - Execute path
CHROME_EXECUTABLE_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# REVIEW - Set up chome user data and profile path for window
CHROME_USER_DATA_PATH = r"C:\Users\hoang\AppData\Local\Google\Chrome\User Data"
CHROME_PROFILE_PATH = r"Profile 1"

# REVIEW -  Chrome option param
CHROME_OPTIONS_PARAM = {
    "experimentals": {
        # STUB - This option make chrome dont auto close when test done
        "detach": True
    },
    "arguments": [
        rf"--user-data-dir={CHROME_USER_DATA_PATH}",
        rf"--profile-directory={CHROME_PROFILE_PATH}",
    ],
}

# REVIEW -  Chrome start path
CHROME_START_PATH = "https://fap.fpt.edu.vn"
