import unittest

import SAIHands


class TestSAIHands(unittest.TestCase):

    def setUp(self):
        self.saih = SAIHands.SAIHands()

    def test_SAIHands_move_mouse_to_OK(self):
        p_old = self.saih.mouse_position()
        self.saih.move_mouse_to(10, 10, 0)
        p = self.saih.mouse_position()
        self.saih.move_mouse_to(p_old.x, p_old.y, 0)
        assert((10, 10) == (p.x, p.y))

    def test_SAIHands_move_mouse_to_NOK(self):
        p_old = self.saih.mouse_position()
        self.saih.move_mouse_to(p_old.x, p_old.y, 0)
        p = self.saih.mouse_position()
        self.saih.move_mouse_to(p_old.x, p_old.y, 0)
        assert((10, 10) != (p.x, p.y))


if __name__ == '__main__':
    unittest.main()
