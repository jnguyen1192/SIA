import numpy as np
import matplotlib.pyplot as plt

from skimage.metrics._structural_similarity import structural_similarity as ssim
from shapely.geometry import Point, Polygon  # @source: https://gis.stackexchange.com/questions/62925/shapely-not-installing-correctly
# wget https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely/Shapely%E2%80%911.6.4.post2%E2%80%91cp37%E2%80%91cp37m%E2%80%91win32.whl
# PycharmProjects\SAI\venv\Scripts>python.exe -m pip install C:\Users\johdu\Downloads\Shapely-1.6.4.post2-cp37-cp37m-win32.whl


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
    #def __init__(self, transform_image, i, j, pixels=[], new_pixels=[]):
        self.transform_image = transform_image
        #self.i = i
        #self.j = j
        self.pixels = pixels
        self.new_pixels = new_pixels

    def get_new_adjacent_pixel(self, x, y):
        """
        Get the new adjacent pixel of the current shape
        TODO Correct using the shape
        :param x: the x position
        :param y: the y position
        :return: the new array of adjacent pixel as [(1, 2), (1, 3), ... ]
        """
        # use get_adjacent_pixel
        # check if those pixels are already use on pixels variable
        # if it is true
        #       do nothing
        # else
        #       add them to new pixels list variable
        # while new pixels list contains point loop the previous statements
        pixels = set(self.get_adjacent_pixel(x, y))
        return pixels

    def get_adjacent_pixel(self, y, x):
        """
        Get the adjacent pixel only if they are True
        y position begins on top
        x position begins on left
        :param x: the x position
        :param y: the y position
        :return: an array containing all the adjacent pixel as True position
        """
        # TODO implement
        adjacent_pixel = []
        # Get only True pixel around given (x, y) pixel
        # test boundaries
        # test north pixel
        #print(self.transform_image[y+1][x])
        #print(self.transform_image[y][x + 1])
        #print(self.transform_image[y - 1][x])
        #print(self.transform_image[y][x - 1])
        height = self.transform_image.shape[0]
        width = self.transform_image.shape[1]
        # y + 1
        if not(y + 1 >= height):
            if np.array_equal(self.transform_image[y+1][x], [255, 255, 255]):
                print("north")
                adjacent_pixel.append(Point(y+1, x))
        #print("height", self.transform_image.shape[0])
        #print("width", self.transform_image.shape[1])
        # test boundaries
        # test east pixel
        # x + 1
        if not (x + 1 >= width):
            if np.array_equal(self.transform_image[y][x + 1], [255, 255, 255]):
                print("east")
                adjacent_pixel.append(Point(y, x + 1))

        # test boundaries
        # test south pixel
        # y - 1
        if not (y - 1 <= 0):
            if np.array_equal(self.transform_image[y - 1][x], [255, 255, 255]):
                print("south")
                adjacent_pixel.append(Point(y - 1, x))

        # test boundaries
        # test west pixel
        # x - 1
        if not (x - 1 <= 0):
            if np.array_equal(self.transform_image[y][x - 1], [255, 255, 255]):
                print("west")
                adjacent_pixel.append(Point(y, x - 1))

        #print(len(adjacent_pixel))
        #from pprint import pprint
        #pprint(self.transform_image)

        return adjacent_pixel




