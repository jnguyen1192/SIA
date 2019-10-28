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

    def get_new_shape(self, old_image, new_image, threshold=10):
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
                    print(index_i, index_j)
                    bool_diff[index_i][index_j] = True
                    #print("Diff", j, "Old", index_i, index_j)
                else:
                    bool_diff[index_i][index_j] = False
        # TODO implement
        # Diff the two images to get a new shape
        import numpy as np
        return bool_diff
