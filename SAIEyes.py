import pyautogui


class SAIEyes:
    def get_current_screen(self):
        return pyautogui.screenshot('Eyes\current_vision.png')