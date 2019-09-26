import pyautogui
import os
from PIL import Image, ImageDraw
import glob

import logging


class SAIEyes:
    def __init__(self, eyes_dir="Eyes", ltm_dir="LongTermMemory", ctm_dir="CourtTermMemory", level=logging.INFO):
        self.eyes_dir = eyes_dir
        self.ltm_dir = ltm_dir
        self.ctm_dir = ctm_dir
        # create dirs
        if not os.path.exists(os.path.join(os.getcwd(), self.eyes_dir)):
            os.makedirs(os.path.join(os.getcwd(), self.eyes_dir))
        if not os.path.exists(os.path.join(os.getcwd(), self.ltm_dir)):
            os.makedirs(os.path.join(os.getcwd(), self.ltm_dir))
        if not os.path.exists(os.path.join(os.getcwd(), self.ctm_dir)):
            os.makedirs(os.path.join(os.getcwd(), self.ctm_dir))

        logging.basicConfig(level=level)

    def get_current_screen(self, cur_screen="current_vision.png"):
        logging.info(os.path.join(os.getcwd(), self.eyes_dir, cur_screen))
        return pyautogui.screenshot(os.path.join(os.getcwd(), self.eyes_dir, cur_screen))

    def get_pos_all_close_button(self, cur_button="close_button_window.png"):
        logging.info(os.path.join(os.getcwd(), self.ltm_dir, cur_button))
        return pyautogui.locateAllOnScreen(os.path.join(os.getcwd(), self.ltm_dir, cur_button))

    def save_image_court_term_memory(self, img, title="test.png"):
        logging.info(os.path.join(os.getcwd(), self.ctm_dir, title))
        img.save(os.path.join(os.getcwd(), self.ctm_dir, title))

    def add_rectangle_on_image(self, img, _box):
        new_img = ImageDraw.Draw(img)
        x0, y0,x1, y1=_box
        new_img.rectangle([(x0, y0), (x1, y1)], outline="red")

    def save_image_with_rectangle_court_term_memory(self, _box, cur_screen="current_vision.png", title="test_rectangle.png"):
        logging.info(os.path.join(os.getcwd(), self.eyes_dir, cur_screen))
        img = Image.open(os.path.join(os.getcwd(), self.eyes_dir, cur_screen)).convert("RGBA")
        self.add_rectangle_on_image(img, _box)
        logging.info("New img to save")
        img.save(os.path.join(os.getcwd(), self.ctm_dir, title))

    def save_image_with_rectangles_court_term_memory(self, _boxes, cur_screen="current_vision.png", title="test_rectangles.png"):
        logging.info(os.path.join(os.getcwd(), self.eyes_dir, cur_screen))
        img = Image.open(os.path.join(os.getcwd(), self.eyes_dir, cur_screen)).convert("RGBA")
        for _box in _boxes:
            x, y, w, h = _box
            self.add_rectangle_on_image(img, (x, y, x+w, y+h))
        logging.info("New img to save")
        img.save(os.path.join(os.getcwd(), self.ctm_dir, title))

    def move_to(self, x, y, duration=5):
        return pyautogui.moveTo(x, y, duration)

    def clean_ctm(self):
        files = glob.glob(os.path.join(os.getcwd(), self.ctm_dir, '*'))
        for f in files:
            os.remove(f)

    def count_ctm_files(self):
        files = glob.glob(os.path.join(os.getcwd(), self.ctm_dir, '*'))
        return len(files)

    def open_eyes(self):
        """
        Take
        :return:
        """
