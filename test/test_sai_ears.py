import unittest
import SAIEars


class TestSAIEars(unittest.TestCase):

    def setUp(self):
        self.saie = SAIEars.SAIEars()

    def test_SAIEars_get_command_case_ok(self):
        print(self.saie.get_command())
        # TODO implement

        assert (True==True)

    def test_create_actions_xml(self):
        """
        Test if the file action.xml is correctly created
        """
        # TODO implement


if __name__ == '__main__':
    unittest.main()
