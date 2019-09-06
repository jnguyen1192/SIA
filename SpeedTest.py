import time


class SpeedTest:
    def test_speed_once(self, func, *args):
        beg = time.time()
        func(*args)
        end = time.time()
        return end - beg

    def test_speed(self, func, *args, nb_test=10):
        sum = 0
        for i in range(nb_test):
            sum += self.test_speed_once(func, *args)
        return sum/nb_test