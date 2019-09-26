import unittest


class TestSAIEyes(unittest.TestCase):

    def setUp(self):
        import sys
        sys.platform = 'win32'
        import SAIEyes
        print("sys.platform ", sys.platform)
        self.saie = SAIEyes.SAIEyes()

    def test_SAIEyes_get_screen(self):
        print(self.saie.get_current_screen())

    def test_SAIEyes_locate_screen(self):
        all_close_button = list(self.saie.get_pos_all_close_button())
        for close_button in all_close_button:
            x, y, width, height = close_button
            print(close_button)
            self.saie.move_to(x + width/2, y + height/2)

    def test_SAIEyes_crop_locate_screen(self):
        all_close_button_generator = self.saie.get_pos_all_close_button()  # 0.052 s
        screen = self.saie.get_current_screen()  # 0.198 s
        try:
            x, y, w, h = next(all_close_button_generator)
            cropped_example = screen.crop((x, y, x+w, y+h))
            self.saie.save_image_court_term_memory(cropped_example)
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_rectangle_locate_screen(self):
        all_close_button_generator = self.saie.get_pos_all_close_button()  # 0.052 s
        screen = self.saie.get_current_screen()  # 0.198 s
        try:
            self.saie.clean_ctm()
            x, y, w, h = next(all_close_button_generator)
            self.saie.save_image_with_rectangle_court_term_memory((x, y, x+w, y+h))
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_rectangles_locate_screen(self):
        all_close_button_generator = self.saie.get_pos_all_close_button()  # 0.052 s
        screen = self.saie.get_current_screen()  # 0.198 s
        try:
            self.saie.clean_ctm()
            self.saie.save_image_with_rectangles_court_term_memory(all_close_button_generator)
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_clean_ctm(self):
        self.saie.clean_ctm()
        assert self.saie.count_ctm_files() == 0


if __name__ == '__main__':
    unittest.main()
