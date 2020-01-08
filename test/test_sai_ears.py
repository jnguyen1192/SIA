import unittest
import SAIEars

import filecmp
import os


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
        new_file_name = "actions.xml"
        test_file_name = "test_xml_actions.xml"
        # create a sample file result
        assert self.saie.create_actions_xml() == 0
        # check if the new file correspond to the sample file result
        assert filecmp.cmp(new_file_name, test_file_name)
        # clean the file created
        if os.path.isfile(new_file_name):
            os.remove(new_file_name)


if __name__ == '__main__':
    unittest.main()
