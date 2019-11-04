import tools.my_tools as mt
import SAIHands


class SAIBrain:
    """
    This class will manipulate data to learn things or manage memory
    """
    def __init__(self, nb_best_command=5, nb_time_rest_second=3600):
        """
        It will set the core of the SIA
        """
        self.nb_best_command = nb_best_command
        self.nb_time_rest_second = nb_time_rest_second
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
        all_polygon = []
        for index_i, i in enumerate(transform_image):
            for index_j, j in enumerate(i):
                if transform_image[i][j] == [255, 255, 255]:  # TODO use PIXEL_TRUE constant as [255, 255, 255]
                    all_polygon = self.get_new_shape(transform_image, i, j, all_polygon)
        return all_polygon

    def get_new_shape(self, transform_image, i, j, all_polygon):
        """
        Get the shape on the current pixel
        :param transform_image: the transform image with pixel true and false
        :param i: the x position
        :param j: the y position
        :param all_polygon: an array containg all the polygon
        :return: An update array containing different polygon
        """
        # TODO implement
        if self.is_in(mt.Point(i, j), all_polygon):  # Point(i, j).is_in(all_shape)
            return all_polygon
        return all_polygon.append(self.create_new_shape(transform_image, i, j))

    def create_new_shape(self, transform_image, i, j):
        """
        Select the corresponding shape with the nearest point available using the first point as (i, j)
        :param transform_image: the transform image with pixel true and false
        :param i: the x position
        :param j: the y position
        :return: the polygon on the position given
        """
        # TODO to implement
        # Create the array of pixel
        # Create a recursive function that will add the pixel using adjacent pixel on the previous array
        return 0

    def get_new_adjacent_pixel(self, transform_image, i, j):
        """
        Get the new adjacent pixel of the current shape
        TODO Correct using the shape
        :param transform_image: the transform image with pixel true and false
        :param i: the x position
        :param j: the y position
        :return: the new array of adjacent pixel as [(1, 2), (1, 3), ... ]
        """
        pixels = set(self.get_adjacent_pixel(transform_image, i, j))
        return pixels

    def get_adjacent_pixel(self, transform_image, i, j):
        # TODO implement
        return ""

    def is_in(self, point, all_polygon):
        """
        Test if a point is on one of the giving polygon
        :param point: the corresponding point (x, y)
        :param all_polygon: all the polygon given
        :return: True if the point is in one of the polygon else False
        """
        for polygon in all_polygon:
            if polygon.contains(point):
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
