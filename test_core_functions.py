import unittest
import SAIEyes

class TestCoreFunctions(unittest.TestCase):
    def test_0(self):
        res = 0
        pred = 0
        assert(pred == res)

    def test_SIAEyes_get_screen(self):
        saie = SAIEyes.SAIEyes()
        print(saie.get_current_screen())


if __name__ == '__main__':
    unittest.main()
