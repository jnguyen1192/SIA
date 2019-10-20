import unittest
import SAIBrain


class TestSAIBrain(unittest.TestCase):

    def setUp(self):
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

    def test_SAIBrain_is_diff_old_image_new_image_case_ok(self):
        # TODO refactor those functions into SAIBrain class
        # Create a tools file that contains functions useful mse for example
        # Use the good function for ssim
        # Use the good path for windows
        from skimage.measure import structural_similarity as ssim
        import matplotlib.pyplot as plt
        import numpy as np
        import cv2

        def mse(imageA, imageB):
            # the 'Mean Squared Error' between the two images is the
            # sum of the squared difference between the two images;
            # NOTE: the two images must have the same dimension
            err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
            err /= float(imageA.shape[0] * imageA.shape[1])

            # return the MSE, the lower the error, the more "similar"
            # the two images are
            return err

        def compare_images(imageA, imageB, title):
            # compute the mean squared error and structural similarity
            # index for the images
            m = mse(imageA, imageB)
            s = ssim(imageA, imageB)

            # setup the figure
            fig = plt.figure(title)
            plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

            # show first image
            ax = fig.add_subplot(1, 2, 1)
            plt.imshow(imageA, cmap=plt.cm.gray)
            plt.axis("off")

            # show the second image
            ax = fig.add_subplot(1, 2, 2)
            plt.imshow(imageB, cmap=plt.cm.gray)
            plt.axis("off")

            # show the images
            plt.show()

        old_image = cv2.imread("is_diff_image_new_image/old_image.png")
        new_image = cv2.imread("is_diff_image_new_image/new_image.png")
        compare_images(old_image, new_image, "old_image vs. new_image")


        assert (True==True)

    def test_SAIBrain_is_diff_old_image_new_image_case_nok(self):
        # TODO implement
        assert (False==False)


if __name__ == '__main__':
    unittest.main()
