import unittest

import SAIHands


class TestSAIHands(unittest.TestCase):

    def setUp(self):
        self.saih = SAIHands.SAIHands()

    def test_SAIHands_move_mouse_to_OK(self):
        x_old = self.saih.mouse_position().x
        y_old = self.saih.mouse_position().y
        self.saih.move_mouse_to(10, 10, 0)
        x = self.saih.mouse_position().x
        y = self.saih.mouse_position().y
        self.saih.move_mouse_to(x_old, y_old, 0)
        assert((10, 10) == (x, y))

    def test_SAIHands_move_mouse_to_NOK(self):
        # TODO implement
        pass


if __name__ == '__main__':
    unittest.main()
