import time
import unittest


class SpeedTest(unittest.TestCase):

    def test_speed_once(self, func, *args):
        beg = time.time()
        func(*args)
        end = time.time()
        return end - beg

    def test_speed_26_screenshot_in_one_second(self):
        """
        The goal is to mesurate how maximum can we take screen in less than a second
        """
        import threading
        import time

        import SAIEyes

        saie = SAIEyes.SAIEyes(eyes_dir="Speedtest", ctm_dir="Speedtest")

        def loop26():
            for i in range(26):
                name = "gross_"+str(i)
                cs = saie.get_current_screen(name+".png")
                saie.save_image_court_term_memory(cs, name + ".png")

        my_thread = threading.Thread(target=loop26)
        my_thread.start()

        my_thread.join()

    def test_speed(self, func, *args, nb_test=10):
        sum = 0
        for i in range(nb_test):
            sum += self.test_speed_once(func, *args)
        return sum/nb_test


if __name__ == '__main__':
    unittest.main()