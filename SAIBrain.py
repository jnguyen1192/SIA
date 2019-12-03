import tools.my_tools as mt
import SAIHands

import os
import cv2


class SAIBrain:
    """
    This class will manipulate data to learn things or manage memory
    """
    def __init__(self, nb_best_command=5, nb_time_rest_second=3600, mtm_dir="MidTermMemory"):
        """
        It will set the core of the SIA
        """
        self.nb_best_command = nb_best_command
        self.nb_time_rest_second = nb_time_rest_second
        self.mtm_dir = mtm_dir
        self.saih = SAIHands.SAIHands()
    """
    
    Db creation methods
    
    """
    def create_db(self):
        """
        Create the db containing commands
        :return:
        """
        try:
            # TODO implement
            # TODO create container with database

            return 0
        except Exception:
            return -1

    def create_container_db(self):
        """
        Create the container db containing commands
        :return:
        """
        try:
            # TODO build the image
            # TODO run the container using the previous image with postgres
            return 0
        except Exception:
            return -1

    def rest(self):
        """
        It will rest and manage the memory
        :return: 0 if it works else -1
        """
        try:
            # TODO implement
            return 0
        except Exception:
            return -1

    def find_new_command(self):
        """
        It will search a new command
        :return: 0 if it works else -1
        """
        try:
            # TODO implement
            # TODO get the new shape obtain with the new command
            return 0
        except Exception:
            return -1

    """ Optionnal methods"""
    def is_command_exist(self, command):
        """
        It will check if the command looks like another command
        :return: True if it works else False
        """
        # TODO implement
        return False

    def manage_memory(self):
        """
        It will compress every image used to get only interesting data
        :return: 0 if it works else -1
        """
        try:
            # TODO implement
            return 0
        except Exception:
            return -1

    def is_diff_old_image_new_image(self, old_image, new_image):
        """
        Compare if the two images are different or not
        :param old_image: the previous image as ndarray
        :param new_image: the current image as ndarray
        :return: True if they are different else False
        """
        if mt.mse(old_image, new_image) != 0:
            return False
        return True

    def get_all_shape_from_image(self, transform_image):
        """
        Get all the shape from the transform image
        :param transform_image: the transform image with pixel true and false
        :return: An array containing different shape
        """
        browsed_pixels = []
        for index_i, i in enumerate(transform_image):
            for index_j, j in enumerate(i):
                if transform_image[i][j] == [255, 255, 255]:  # TODO use PIXEL_TRUE constant as [255, 255, 255]
                    browsed_pixels = self.get_new_shape(transform_image, i, j, browsed_pixels)
        return browsed_pixels

    def get_new_shape(self, transform_image, i, j, all_polygon):
        """
        Get the shape on the current pixel
        :param transform_image: the transform image with pixel true and false
        :param i: the x position
        :param j: the y position
        :param browsed_pixels: an array containg all pixels browsed
        :return: An update array containing different polygon
        """
        # TODO implement
        if self.is_in(mt.Point(i, j), all_polygon):  # Point(i, j).is_in(all_shape)
            return all_polygon
        return all_polygon.append(self.create_new_shape(transform_image, i, j))

    def create_new_shape(self, transform_image, y, x):
        """
        Select the corresponding shape with the nearest point available using the first point as (i, j)
        :param transform_image: the transform image with pixel true and false
        :param y: the y position
        :param x: the x position
        :return: the browsed_pixels on the position given
        """
        # TODO to implement
        # Use the class shape to create a new shape
        s = mt.Shape(transform_image)
        s.detect_shape(y, x)
        # use function to get min y and x from pixels
        min_max_pixels = s.get_box()
        # This image will be compose of the shape as pixel (255, 255, 255, 255) and (0, 0, 0, 0)
        new_array = s.extract_box(min_max_pixels)
        # get the name of the shape
        name = s.get_name(new_array)
        # This shape will be on a new image in the directory mid term memory
        # This image will have a special name using height_width_number:
        #   - height : the height of the image
        #   - width : the width of the image
        #   - number : the number of the image in the corresponding cluster (height, width)
        image_path = os.path.join(self.mtm_dir, name + ".png")
        cv2.imwrite(image_path, new_array)
        # TODO return browsed pixels
        return []  # the browsed_pixels on the position given

    def is_in(self, point, browsed_pixels):
        """
        Test if a point is on one of the giving polygon
        :param point: the corresponding point (y, x)
        :param browsed_pixels: all the browsed pixels given
        :return: True if the point is in one of the browsed pixels else False
        """
        for p in browsed_pixels:
            if p == point:
                print(p, point)
                return True
        return False

    def get_transform_image(self, old_image, new_image, threshold=10):
        """
        Get the shape obtains between 2 images as an array and x, y and height an width
        :param old_image: the previous image as ndarray
        :param new_image: the current image as ndarray
        :return: the new shape
        """
        np_zero = mt.np.zeros(3)

        bool_diff = old_image.copy()
        diff = old_image - new_image
        for index_i, i in enumerate(diff):
            for index_j, j in enumerate(i):
                if not mt.np.array_equal(j, np_zero):
                    bool_diff[index_i][index_j] = [255, 255, 255]
                    #print("Diff", j, "Old", index_i, index_j)
                else:
                    bool_diff[index_i][index_j] = [0, 0, 0]  # TODO use PIXEL_FALSE constant as [0, 0, 0]
        # TODO implement
        # Diff the two images to get a new shape
        import numpy as np
        return bool_diff
