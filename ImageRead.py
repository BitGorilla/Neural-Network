"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""

from collections import namedtuple

class ImageRead:

    def __init__(self):
        pass


    def readImage(self, file):
        Image = namedtuple('Image', 'values, mood')

        w,h = 20,20
        imageArray = [[0 for x in range(w)] for y in range(h)]

        image_file = open(file, 'r')

        i = 0
        image_file.readline(5)
        for line in image_file:
            valueArray = image_file.read().split()

            for j in range(20):
                imageArray[i][j] = valueArray[j]
            i += 1
            Image.values = valueArray


        file.close()
