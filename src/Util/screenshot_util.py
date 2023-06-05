import pyautogui
import cv2
import numpy as np
import time
import PIL.ImageGrab

pathSave = "src\data\output"
filename = "name"
videoname = "output"


def screenshot():
    time.sleep(3)
    myScreenshot = pyautogui.screenshot()
    img = PIL.ImageGrab.grab()
    img.show()
    myScreenshot.save(f"{pathSave}\\{filename}.png")


def screenshotApp(app_name: str):
    # Get the position and size of the Word window
    window_pos = pyautogui.locateOnScreen("word_icon.png")
    window_size = pyautogui.size()


def video_shot():
    SCREEN_SIZE = (1920, 1080)
    fource = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(f"{pathSave}\\{videoname}.mp4", fource, 20.0, (SCREEN_SIZE))

    fps = 30
    prev = 0

    while True:
        time_elapsed = time.time() - prev
        img = pyautogui.screenshot()
        if time_elapsed > 1.0 / fps:
            prev = time.time()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        cv2.waitKey(10000)
