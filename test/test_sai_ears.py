import unittest
import SAIEars


class TestSAIEars(unittest.TestCase):

    def setUp(self):
        self.saie = SAIEars.SAIEars()

    def test_SAIEars_get_command_case_ok(self):
        print(self.saie.get_command())
        # TODO implement

        assert (True==True)


if __name__ == '__main__':
    unittest.main()
