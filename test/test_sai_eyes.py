import unittest
import SAIEyes
import Xlib

class TestSAIEyes(unittest.TestCase):
    def test_SAIEyes_get_screen(self):
        saie = SAIEyes.SAIEyes()
        print(saie.get_current_screen())

    def test_SAIEyes_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button = list(saie.get_pos_all_close_button())
        for close_button in all_close_button:
            x, y, width, height = close_button
            print(close_button)
            saie.move_to(x + width/2, y + height/2)

    def test_SAIEyes_crop_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button_generator = saie.get_pos_all_close_button()  # 0.052 s
        screen = saie.get_current_screen()  # 0.198 s
        try:
            x, y, w, h = next(all_close_button_generator)
            cropped_example = screen.crop((x, y, x+w, y+h))
            saie.save_image_court_term_memory(cropped_example)
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_rectangle_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button_generator = saie.get_pos_all_close_button()  # 0.052 s
        screen = saie.get_current_screen()  # 0.198 s
        try:
            saie.clean_ctm()
            x, y, w, h = next(all_close_button_generator)
            saie.save_image_with_rectangle_court_term_memory((x, y, x+w, y+h))
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_rectangles_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button_generator = saie.get_pos_all_close_button()  # 0.052 s
        screen = saie.get_current_screen()  # 0.198 s
        try:
            saie.clean_ctm()
            saie.save_image_with_rectangles_court_term_memory(all_close_button_generator)
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_clean_ctm(self):
        saie = SAIEyes.SAIEyes()
        saie.clean_ctm()
        assert saie.count_ctm_files() == 0


if __name__ == '__main__':
    unittest.main()
