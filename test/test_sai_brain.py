import unittest
import SAIBrain

import cv2
import os


class TestSAIBrain(unittest.TestCase):

    def setUp(self):
        self.current_dir = os.getcwd()
        self.saib = SAIBrain.SAIBrain()
        self.polygons_test_is_in = [SAIBrain.mt.Polygon([(1, 6),
                                                         (1, 5),
                                                         (4, 5),
                                                         (4, 6)]),
                                    SAIBrain.mt.Polygon([(5, 6),
                                                         (5, 2),
                                                         (7, 2),
                                                         (7, 6)]),
                                    SAIBrain.mt.Polygon([(1, 2),
                                                         (1, 1),
                                                         (2, 1),
                                                         (2, 2)]),
                                    SAIBrain.mt.Polygon([(3, 4),
                                                         (3, 1),
                                                         (4, 1),
                                                         (4, 4)])
                                    ]

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
        # Create a random behavior for:
        #       - mouse movement : x, y,
        #       - mouse click : click, double_click,
        #       - mouse hold-release(with movement): x, y
        # Use a depth of 1
        # TODO refactor the random mouse movement into a function on SAIBrain
        # TODO Mouse movement
        import random
        # x and y
        # get window width and height
        from win32api import GetSystemMetrics
        # 1080, 1920
        # 864, 1536
        #import tkinter
        import pyautogui
        import random

        x_rand = random.randint(0, pyautogui.size().width)
        y_rand = random.randint(0, pyautogui.size().height)

        pyautogui.moveTo(x_rand, y_rand)

        print("Width =", GetSystemMetrics(0))
        print("Height =", GetSystemMetrics(1))

        # TODO test the random mouse movement using old and new mouse position
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

    def test_SAIBrain_is_diff_old_image_new_image_case_different_time_ok(self):
        """
        Test if the function works with different time images
        """
        # Result : MSE = 2.02
        self.generic_test_SAIBrain_is_diff_old_image_new_image("old_image_1.png", "new_image_1.png", False)

    def test_SAIBrain_is_diff_old_image_new_image_case_same_images_ok(self):
        """
        Test if the function works with same images
        """
        # Result : MSE = 0.0
        self.generic_test_SAIBrain_is_diff_old_image_new_image("old_image_2.png", "new_image_2.png", True)

    def test_SAIBrain_is_diff_old_image_new_image_case_different_images_ok(self):
        """
        Test if the function works with different images
        """
        # Result : MSE = 9.63
        self.generic_test_SAIBrain_is_diff_old_image_new_image("old_image_3.png", "new_image_3.png", False)

    def generic_test_SAIBrain_is_diff_old_image_new_image(self, name_new_image, name_old_image, pred):
        old_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", name_new_image)
        new_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", name_old_image)
        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)
        res = self.saib.is_diff_old_image_new_image(old_image, new_image)
        assert(pred == res)

    def test_SAIBrain_get_new_shape_case_ok(self):
        """
        Test if the function works with different time images
        """
        old_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", "old_image_4.png")
        new_image_path = os.path.join(self.current_dir, "is_diff_old_image_new_image", "new_image_4.png")

        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)

        res = self.saib.get_transform_image(old_image, new_image)

        import matplotlib.pyplot as plt
        import numpy as np
        from pprint import pprint
        pprint(res)
        pprint(res[251][0])
        plt.imshow(res)
        plt.savefig("new_shape_1.png")
        # TODO only where there was a difference get the new image pixels
        # TODO Create an array with True and False using res
        plt.show()
        #np_zero = np.zeros(3)
        """
        for index_i, i in enumerate(res):
            for index_j, j in enumerate(i):
                if not np.array_equal(j, np_zero):
                    print("Diff", j, "Old", index_i, index_j)
        """
        # TODO Correct the new array using [[...]...]
        #print("---------------------------")
        #print([j if np.array_equal(j, np_zero) else j for j in [i for i in res]])
        #print("---------------------------")
        #pprint(res.shape)
        # TODO Try to use res[i][j]
        #pprint([True if i != 0.0 else False for i in res])
        # TODO Get the shape position width and height using the True from res
        #print("Get the shape position", res[0][0])
        #print("Test the shape position", np.array_equal(res[251][0], np_zero))


        # TODO Extract this sub array into a new res

        # TODO We need to save this shape into a new little image with it position on the big image

    def test_SAIBrain_contains_OK(self):
        """
        Test if the function contains works
        """
        # to implement
        point = SAIBrain.mt.Point(2, 2)
        polygon = SAIBrain.mt.Polygon([(0, 0),
                                       (0, 3),
                                       (3, 3),
                                       (3, 0)])
        assert(polygon.contains(point))

    def test_SAIBrain_contains_NOK(self):
        """
        Test if the function contains works
        """
        # to implement
        point = SAIBrain.mt.Point(4, 4)
        polygon = SAIBrain.mt.Polygon([(0, 0),
                                       (0, 3),
                                       (3, 3),
                                       (3, 0)])
        assert(not polygon.contains(point))

    def test_SAIBrain_is_in_OK(self):
        """
        Test if the function is_in works
        """
        point = SAIBrain.mt.Point(6, 4)
        assert(self.saib.is_in(point, self.polygons_test_is_in))

    def test_SAIBrain_is_in_NOK(self):
        """
        Test if the function is_in works
        """
        point = SAIBrain.mt.Point(2, 3)
        assert(not self.saib.is_in(point, self.polygons_test_is_in))

    def test_SAIBrain_mt_shape_get_adjacent_pixel(self):
        """
        Test if the function get_adjacent_pixel from my_tools works
        """
        # open image
        old_image_path = os.path.join(self.current_dir, "test_shape", "old_get_adjacent_pixel.png")
        new_image_path = os.path.join(self.current_dir, "test_shape", "new_get_adjacent_pixel.png")

        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)


        # transform image
        tr_img = self.saib.get_transform_image(old_image, new_image)
        # TODO create shape object
        for i_i, i in enumerate(tr_img):
            for i_j, j in enumerate(i):
                if not SAIBrain.mt.np.array_equal(tr_img[i_i][i_j], [0, 0, 0]):
                    print("new pixel", i_i, i_j)

        # TODO test get adjacent pixel

    def test_SAIBrain_mt_shape_get_adjacent_pixel_OK(self):
        """
        Test if the function get_adjacent_pixel from my_tools works
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 1 0 0 0
        0 0 1 1 1 0 0
        0 0 0 1 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 1 1 1 0 0
        0 0 0 0 0 0 0
        point(x,y)
        point(3,4)

        point(3,5)
        point(4,4)
        point(3,3)
        point(2,4)
        """
        # TODO implement
        x = 4
        y = 3
        # open image
        old_image_path = os.path.join(self.current_dir, "test_shape", "old_get_adjacent_pixel.png")
        new_image_path = os.path.join(self.current_dir, "test_shape", "new_get_adjacent_pixel.png")

        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)


        # transform image
        tr_img = self.saib.get_transform_image(old_image, new_image)
        my_shape = SAIBrain.mt.Shape(tr_img)
        #print(len(my_shape.get_adjacent_pixel(4, 2)))
        for p in my_shape.get_adjacent_pixel(4, 3):
            print(p.y, p.x)

    def test_SAIBrain_mt_shape_get_adjacent_pixel_NOK(self):
        """
        Test if the function get_adjacent_pixel from my_tools works
        """
        # TODO implement

    def generic_test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries(self, first_point, points_to_predict, cardinal_point):
        """
        Test if the function works with east boundaries with following parameters :
        east image
        (2, 1) : (2, 2) + (1, 1)
        :param first_point: the point as (y, x)
        :param points_to_predict: the points to predicts as [(y1, x1), (...) ...]
        :param cardinal_point: the cardinal point (east, south, west, north)
        """
        # open image
        old_image_path = os.path.join(self.current_dir, "test_shape", "old_boundaries_" + cardinal_point + ".png")
        new_image_path = os.path.join(self.current_dir, "test_shape", "new_boundaries_" + cardinal_point + ".png")

        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)

        # transform image
        tr_img = self.saib.get_transform_image(old_image, new_image)
        my_shape = SAIBrain.mt.Shape(tr_img)

        # test if result of get_adjacent_pixel works correctly
        for i_p, p in enumerate(my_shape.get_adjacent_pixel(*first_point)):
            assert(points_to_predict[i_p] == p)

    def test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries_east_OK(self):
        """
        Test if the function works with east boundaries with following parameters :
        east image
        (1, 2) : (2, 2) + (1, 1)
        """
        first_point = (1, 2)
        points_to_predict = [(2, 2), (1, 1)]
        self.generic_test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries(first_point, points_to_predict, "east")

    def test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries_south_OK(self):
        """
        Test if the function works with east boundaries with following parameters :
        south image
        (2, 2) : (1, 2) + (2, 1)
        """
        first_point = (2, 2)
        points_to_predict = [(1, 2), (2, 1)]
        self.generic_test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries(first_point, points_to_predict, "south")

    def test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries_west_OK(self):
        """
        Test if the function works with east boundaries with following parameters :
        west image
        (2, 0) : (1, 0) + (2, 1)
        """
        first_point = (2, 0)
        points_to_predict = [(1, 0), (2, 1)]
        self.generic_test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries(first_point, points_to_predict, "west")

    def test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries_north_OK(self):
        """
        Test if the function works with east boundaries with following parameters :
        north image
        (0, 1) : (0, 2) + (1, 1)
        """
        first_point = (0, 1)
        points_to_predict = [(0, 2), (1, 1)]
        self.generic_test_SAIBrain_mt_shape_get_adjacent_pixel_boundaries(first_point, points_to_predict, "north")

    def generic_test_SAIBrain_mt_shape_get_new_adjacent_pixel_boundaries(self, pixel, pixels, new_pixels_to_predict, cardinal_point):
        """
        Test if the function works with east boundaries with following parameters :
        east image
        (2, 1) : (2, 2) + (1, 1)
        :param pixel: the point as (y, x)
        :param pixels: the point as (y, x)
        :param new_pixels_to_predict: the points to predicts as [(y1, x1), (...) ...]
        :param cardinal_point: the cardinal point (east, south, west, north)
        """
        # open image
        old_image_path = os.path.join(self.current_dir, "test_shape", "old_get_new_adjacent_pixel.png")
        new_image_path = os.path.join(self.current_dir, "test_shape", "new_get_new_adjacent_pixel_" + cardinal_point + ".png")

        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)

        # transform image
        tr_img = self.saib.get_transform_image(old_image, new_image)
        my_shape = SAIBrain.mt.Shape(tr_img, pixels)

        # test if result of get_adjacent_pixel works correctly
        for i_p, p in enumerate(my_shape.get_new_adjacent_pixel(*pixel)):
            assert(new_pixels_to_predict[i_p] == p)

    def test_SAIBrain_mt_shape_get_new_adjacent_pixel_north_OK(self):
        """
        Test if the function works and add the new pixel with the north case
        init : [(0, 0), (0, 1)
        new : [(0, 2), (1, 1)
        """
        pixel = (0, 1)
        pixels = [(0, 0), (0, 1)]
        new_pixels_to_predict = [(0, 2), (1, 1)]
        self.generic_test_SAIBrain_mt_shape_get_new_adjacent_pixel_boundaries(pixel, pixels, new_pixels_to_predict, "north")

    def test_SAIBrain_mt_shape_get_new_adjacent_pixel_east_OK(self):
        """
        Test if the function works and add the new pixel with the east case
        init : [(0, 3), (1, 2)
        new : [(2, 2), (1, 1)
        """
        pixel = (1, 2)
        pixels = [(0, 3), (1, 2)]
        new_pixels_to_predict = [(2, 2), (1, 1)]
        self.generic_test_SAIBrain_mt_shape_get_new_adjacent_pixel_boundaries(pixel, pixels, new_pixels_to_predict, "east")

    def test_SAIBrain_mt_shape_get_new_adjacent_pixel_south_OK(self):
        """
        Test if the function works and add the new pixel with the south case
        init : [(0, 0), (0, 1)
        new : [(0, 2), (1, 1)
        """
        pixel = (2, 1)
        pixels = [(1, 1), (2, 1)]
        new_pixels_to_predict = [(2, 2), (2, 0)]
        self.generic_test_SAIBrain_mt_shape_get_new_adjacent_pixel_boundaries(pixel, pixels, new_pixels_to_predict, "south")

    def test_SAIBrain_mt_shape_get_new_adjacent_pixel_west_OK(self):
        """
        Test if the function works and add the new pixel with the west case
        init : [(0, 0), (1, 0)
        new : [(1, 1), (2, 1)
        """
        pixel = (1, 0)
        pixels = [(0, 0), (1, 0)]
        new_pixels_to_predict = [(1, 1), (2, 0)]
        self.generic_test_SAIBrain_mt_shape_get_new_adjacent_pixel_boundaries(pixel, pixels, new_pixels_to_predict, "west")

    def generic_test_SAIBrain_mt_shape_get_shape(self, pixel, pixels_to_predict, cardinal_point):
        """
        Generic function to test function get_shape with following parameters :
        east image
        (2, 1) : (2, 2) + (1, 1)
        :param pixel: the point as (y, x)
        :param pixels_to_predict: the points to predicts as [(y1, x1), (...) ...]
        :param cardinal_point: the cardinal point (east, south, west, north)
        """
        # open image
        old_image_path = os.path.join(self.current_dir, "test_shape", "old_get_shape_" + cardinal_point + ".png")
        new_image_path = os.path.join(self.current_dir, "test_shape", "new_get_shape_" + cardinal_point + ".png")

        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)

        # transform image
        tr_img = self.saib.get_transform_image(old_image, new_image)
        my_shape = SAIBrain.mt.Shape(tr_img)
        # test if result of get_adjacent_pixel works correctly
        for i_p, p in enumerate(my_shape.get_shape(*pixel)):
            assert(pixels_to_predict[i_p] == p)

    def test_SAIBrain_mt_shape_get_shape_west_OK(self):
        """
        Test if the function get shape works with the west case
        mat=[0, 0, 0, 0, 0, 0,
             0, 1, 1, 1, 1, 0,
             0, 0, 1, 0, 1, 0,
             0, 0, 1, 1, 1, 0,
             0, 0, 0, 0, 0, 0]
        Here, we want to get 1 on the previous matrix.
        init : (1, 1)
        predict : [(1, 1), (1, 2), (1, 3), (2, 2), (1, 4), (3, 2), (2, 4), (3, 3), (3, 4)]
        """
        pixel = (1, 1)
        pixels_to_predict = [(1, 1), (1, 2), (1, 3), (2, 2), (1, 4), (3, 2), (2, 4), (3, 3), (3, 4)]
        self.generic_test_SAIBrain_mt_shape_get_shape(pixel, pixels_to_predict, "west")

    def test_SAIBrain_mt_shape_get_shape_north_OK(self):
        """
        Test if the function get shape works with the north case
        mat=[0, 0, 0, 0, 0,
             0, 0, 0, 1, 0,
             0, 1, 1, 1, 0,
             0, 1, 0, 1, 0,
             0, 1, 1, 1, 0,
             0, 0, 0, 0, 0]
        Here, we want to get 1 on the previous matrix.
        init : (1, 3)
        predict : [(1, 3), (2, 3), (3, 3), (2, 2), (4, 3), (2, 1), (4, 2), (3, 1), (4, 1)]
        """
        pixel = (1, 3)
        pixels_to_predict = [(1, 3), (2, 3), (3, 3), (2, 2), (4, 3), (2, 1), (4, 2), (3, 1), (4, 1)]
        self.generic_test_SAIBrain_mt_shape_get_shape(pixel, pixels_to_predict, "north")

    def test_SAIBrain_mt_shape_get_shape_east_OK(self):
        """
        Test if the function get shape works with the west case
        mat=[0, 0, 0, 0, 0, 0,
             0, 1, 1, 1, 0, 0,
             0, 1, 0, 1, 0, 0,
             0, 1, 1, 1, 1, 0,
             0, 0, 0, 0, 0, 0]
        Here, we want to get 1 on the previous matrix.
        init : (1, 1)
        predict : [(1, 2), (1, 3), (2, 2), (1, 4), (3, 2), (2, 4), (3, 3), (3, 4)]
        """
        pixel = (1, 1)
        pixels_to_predict = [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (3, 3), (3, 4)]
        self.generic_test_SAIBrain_mt_shape_get_shape(pixel, pixels_to_predict, "east")

    def test_SAIBrain_mt_shape_get_shape_south_OK(self):
        """
        Test if the function get shape works with the south case
        mat=[0, 0, 0, 0, 0,
             0, 1, 1, 1, 0,
             0, 1, 0, 1, 0,
             0, 1, 1, 1, 0,
             0, 1, 0, 0, 0,
             0, 0, 0, 0, 0]
        Here, we want to get 1 on the previous matrix.
        init : (1, 1)
        predict : [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (4, 1), (3, 3)]
        """
        pixel = (1, 1)
        pixels_to_predict = [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (4, 1), (3, 3)]
        self.generic_test_SAIBrain_mt_shape_get_shape(pixel, pixels_to_predict, "south")

    def test_SAIBrain_create_shape_north_OK(self):
        """
        Test if the function create shape works with the north case
        """
        # TODO to implement
        # create an image using matplotlib using transparency with pixel (0, 0, 0, 0) and (0, 0, 0, 255)
        # get the shape
        # open image
        old_image_path = os.path.join(self.current_dir, "test_shape", "old_get_shape_north.png")
        new_image_path = os.path.join(self.current_dir, "test_shape", "new_get_shape_north.png")

        old_image = cv2.imread(old_image_path)
        new_image = cv2.imread(new_image_path)

        # transform image
        tr_img = self.saib.get_transform_image(old_image, new_image)

        s = SAIBrain.mt.Shape(tr_img)
        pixels = s.get_shape(1, 3)

        # create an image called test_SAIBrain_create_shape_north_OK_3x4_1 which the small crop image with transparency
        # TODO use function to get min y and x from pixels

        # TODO substract all pixels with the previous new point

        # TODO create an image with the new pixels using transparency


        from pprint import pprint
        pprint(pixels)

        # create an image using paint with the correct predict of shape using https://www.photopea.com/
        # open image
        pred_image_path = os.path.join(self.current_dir, "test_shape", "new_create_shape_north_transparent_OK.png")
        pred_image = cv2.imread(pred_image_path, cv2.IMREAD_UNCHANGED)
        pprint(pred_image)


        # check if the function return the good shape and create the correct image
        pass

    def test_SAIBrain_create_shape_NOK(self):
        """
        Test if the function create shape works with the empty case
        """
        # TODO to implement
        pass




if __name__ == '__main__':
    unittest.main()
