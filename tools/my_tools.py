import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime

from skimage.metrics._structural_similarity import structural_similarity as ssim
from shapely.geometry import Point, Polygon  # @source: https://gis.stackexchange.com/questions/62925/shapely-not-installing-correctly
# wget https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely/Shapely-1.6.4.post2-cp37-cp37m-win_amd64.whl
# PycharmProjects\SAI\venv_37_64\Scripts>python.exe -m pip install "C:\Users\johdu\Downloads\Shapely-1.6.4.post2-cp37-cp37m-win_amd64.whl"


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
    s = ssim(imageA, imageB, multichannel=True)

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


class Shape:
    def __init__(self, transform_image, pixels=[], new_pixels=[]):
        self.transform_image = transform_image
        self.pixels = pixels
        self.new_pixels = new_pixels

    def get_new_adjacent_pixel(self, y, x):
        """
        Get the new adjacent pixel of the current shape
        :param x: the x position
        :param y: the y position
        :return: an array with new pixels
        """
        pixels = self.get_adjacent_pixel(y, x)
        for pixel in pixels:
            if pixel in self.pixels or pixel in self.new_pixels:
                pixels.remove(pixel)
        return pixels

    def detect_shape(self, y, x):
        """
        Get the current shape
        TODO Correct using the shape
        :param x: the x position
        :param y: the y position
        :return: the new array of adjacent pixel as [(1, 2), (1, 3), ... ]
        """
        print("before", self.pixels)
        pixels = []
        if np.array_equal(self.transform_image[y][x], [255, 255, 255]):
            self.pixels.append((y, x))
            pixels = self.get_adjacent_pixel(y, x)
        # use get_adjacent_pixel
        if len(pixels) != 0:
            self.new_pixels = self.new_pixels + pixels
            i = 0
            while i < len(self.new_pixels):
            #for pixel in self.new_pixels:
            # check if those pixels are already use on pixels variable
                pixel = self.new_pixels[i]
                if pixel not in self.pixels:
                    self.pixels.append(pixel)
                    #self.new_pixels.remove(pixel)
                    # add them to new pixels list variable
                    new_pixels = self.get_new_adjacent_pixel(*pixel)
                    if len(new_pixels) != 0:
                        self.new_pixels = self.new_pixels + new_pixels
                #print(len(self.new_pixels))
                i += 1

    def get_adjacent_pixel(self, y, x):
        """
        Get the adjacent pixel only if they are True
        y position begins on top
        x position begins on left
        order : north > east > south > west
        :param x: the x position
        :param y: the y position
        :return: an array containing all the adjacent pixel as True position
        """
        adjacent_pixel = []
        # Get only True pixel around given (x, y) pixel
        height = self.transform_image.shape[0]
        width = self.transform_image.shape[1]
        # Test boundaries
        # Test north pixel
        # y - 1
        if not (y - 1 <= 0):
            if np.array_equal(self.transform_image[y - 1][x], [255, 255, 255]):
                adjacent_pixel.append((y - 1, x))

        # Test east pixel
        # x + 1
        if not (x + 1 >= width):
            if np.array_equal(self.transform_image[y][x + 1], [255, 255, 255]):
                adjacent_pixel.append((y, x + 1))

        # Test south pixel
        # y + 1
        if not(y + 1 >= height):
            if np.array_equal(self.transform_image[y+1][x], [255, 255, 255]):
                adjacent_pixel.append((y+1, x))

        # Test west pixel
        # x - 1
        if not (x - 1 <= 0):
            if np.array_equal(self.transform_image[y][x - 1], [255, 255, 255]):
                adjacent_pixel.append((y, x - 1))

        return adjacent_pixel

    def get_box(self):
        """
        This method is always used after get_shape function
        :return: an array with two points [(y_min, x_min), (y_max, x_max)] representing a box of the shape
        """
        min_y = sys.maxsize
        min_x = sys.maxsize
        max_y = -1
        max_x = -1
        # for each pixels
        for pixel in self.pixels:
            # get the min of y and x
            if pixel[0] < min_y:
                min_y = pixel[0]
            if pixel[1] < min_x:
                min_x = pixel[1]
            # get the max of y and x
            if pixel[0] > max_y:
                max_y = pixel[0]
            if pixel[1] > max_x:
                max_x = pixel[1]
        # return those two points
        return [(min_y, min_x), (max_y, max_x)]

    def extract_box(self, min_max):
        """
        This method will extract the box on a new matrix
        :param min_max: an array with two points [(y_min, x_min), (y_max, x_max)] representing a box of the shape
        :return: an ndarray with the new coordinates of the shape
        """
        # create the ndarray using minmax
        test_array = np.zeros(shape=(min_max[1][0] - min_max[0][0] + 1, min_max[1][1] - min_max[0][1] + 1, 4),
                              dtype=np.uint8)
        # use min pixel to get the new pixels values (difference)
        shift_array = [(p[0] - min_max[0][0], p[1] - min_max[0][1]) for p in self.pixels]
        # fulfill the new array with the shift array
        for pixel in shift_array:
            test_array[pixel[0]][pixel[1]] = [0, 0, 0, 255]
        return test_array

    def get_name(self, new_array):
        """
        Create the name of the current shape using the dimension and the current date, for example:
        height_width_%Y_%m_%d_%H:%M:%S.%f
        :return: the name with the correct format
        """
        # Get the shape of new array
        shape = new_array.shape
        #print(shape)
        # Get the current date with milliseconds
        today = datetime.datetime.now()
        # Return with the correct format
        return str(shape[0]) + "_" + str(shape[1]) + "_" + today.strftime("%Y%m%d%H%M%S%f")



