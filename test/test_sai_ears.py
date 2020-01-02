import unittest
import SAIEars


class TestSAIBrain(unittest.TestCase):

    def setUp(self):
        self.saie = SAIEars.SAIEars()
        self.polygons_test_is_in = [(1, 6), (1, 5), (4, 5), (4, 6)]

    def test_SAIEars_get_command_case_ok(self):
        # TODO implement
        assert (True==True)


if __name__ == '__main__':
    unittest.main()
