import unittest
import SAIBrain
import tools.my_tools as mt

import cv2
import os


class TestSAIBrain(unittest.TestCase):

    def setUp(self):
        self.current_dir = os.getcwd()
        self.saib = SAIBrain.SAIBrain()

    def test_SAIBrain_create_db_case_ok(self):
        # TODO implement
        assert (True==True)

    def test_SAIBrain_create_db_case_nok(self):
        # TODO implement
        assert (False==False)

    def test_SAIBrain_create_db_case_ok(self):
        # TODO implement
        assert (True==True)

    def test_SAIBrain_create_db_case_nok(self):
        # TODO implement
        assert (False==False)

    def test_SAIBrain_rest_case_ok(self):
        # TODO implement
        assert (True==True)

    def test_SAIBrain_rest_case_nok(self):
        # TODO implement
        assert (False==False)

    def test_SAIBrain_find_new_command_case_ok(self):
        # TODO implement
        assert (True==True)

    def test_SAIBrain_find_new_command_case_nok(self):
        # TODO implement
        assert (False==False)

    """ Optionnal methods"""
    def test_SAIBrain_is_command_exist_case_true(self):
        # TODO implement
        assert (True==True)

    def test_SAIBrain_is_command_exist_case_false(self):
        # TODO implement
        assert (False==False)

    def test_SAIBrain_manage_memory_case_ok(self):
        # TODO implement
        assert (True==True)

    def test_SAIBrain_manage_memory_case_nok(self):
        # TODO implement
        assert (False==False)

    def generic_test_SAIBrain_is_diff_old_image_new_image(self, name_new_image, name_old_image):
        old_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", name_new_image)
        new_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", name_old_image)
        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)
        mt.compare_images(old_image, new_image, "old_image vs. new_image")

    def test_SAIBrain_is_diff_old_image_new_image_case_different_time_ok(self):
        # TODO Create another test images for this function
        self.generic_test_SAIBrain_is_diff_old_image_new_image("old_image_1.png", "new_image_1.png")
        """
        old_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", "old_image_1.png")
        new_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", "new_image_1.png")
        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)
        mt.compare_images(old_image, new_image, "old_image vs. new_image")
        """
        assert (True==True)

    def test_SAIBrain_is_diff_old_image_new_image_case_same_images_ok(self):
        # TODO implement
        assert (True==True)

    def test_SAIBrain_is_diff_old_image_new_image_case_different_images_ok(self):
        # TODO implement
        assert (True==True)


if __name__ == '__main__':
    unittest.main()
