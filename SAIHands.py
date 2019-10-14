import pyautogui


class SAIHands:
    """
    This class is used to use mouse, keyboard or another type of control
    First we will only use mouse and keyboard
    """
    def move_mouse_to(self, x, y, duration=5):
        """
        The mouse will move in the point we choose
        :param x: x axis
        :param y: y axis
        :param duration: time to move to the point
        :return: 0 if it works else -1
        """
        try:
            pyautogui.moveTo(x, y, duration)
        except Exception as e:
            print("move_mouse_to :", e)
            return -1
        return 0


