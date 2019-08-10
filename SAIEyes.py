import pyautogui


class SAIEyes:
    def get_current_screen(self):
        return pyautogui.screenshot('Eyes\current_vision.png')

    def get_pos_all_close_button(self):
        return pyautogui.locateAllOnScreen('Memory\close_button_window.png')

    def move_to(self, x, y, duration=5):
        return pyautogui.moveTo(x, y, duration)