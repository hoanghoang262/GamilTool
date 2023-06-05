"""Sumary: run file"""
from module.chrome_controler import ChromeControler


def runner():
    """Main run class"""
    chrome_controler = ChromeControler()
    chrome_controler.open_start_window()


if __name__ == "__main__":
    runner()
