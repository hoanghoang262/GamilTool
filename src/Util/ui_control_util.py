import pyautogui


# SECTION - Exam
def getWindowSize():
    print(pyautogui.size())


def getMountPosition():
    print(pyautogui.position())


def pause(pause_time: float):
    pyautogui.PAUSE = pause_time


def mouse_move_to(move_to_X: int, move_to_Y: int, move_duration: float):
    pyautogui.moveTo(move_to_X, move_to_Y, duration=move_duration)


def move_mouse(move_to_X: int, move_to_Y: int, move_duration: float):
    pyautogui.moveRel(move_to_X, move_to_Y, duration=move_duration)
