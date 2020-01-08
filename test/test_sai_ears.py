import unittest
import SAIEars

import filecmp

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
        # TODO create a sample file result
        assert self.saie.create_actions_xml() == 0
        # TODO check if the new file correspond to the sample file result
        assert filecmp.cmp("actions.xml", "test_xml_actions.xml")
        # TODO clean the file created


if __name__ == '__main__':
    unittest.main()
