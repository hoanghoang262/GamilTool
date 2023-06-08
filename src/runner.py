"""Sumary: run file"""
from module.chrome_controler import ChromeControler


def runner():
    """Main run class"""
    chrome_controler = ChromeControler()
    chrome_controler.open_start_window()
    chrome_controler.close_Chrome()


if __name__ == "__main__":
    runner()
