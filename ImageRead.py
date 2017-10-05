"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
import sys
from collections import namedtuple

class ImageRead:

    def __init__(self):
        pass


    def readImage(self, file):
        Image = namedtuple('Face', 'name, values, mood')

        w,h = 20,20
        imageArray = [[0 for x in range(w)] for y in range(h)]

        """https://stackoverflow.com/questions/9578580/skip-first-couple-of-lines-while-reading-lines-in-python-file"""
        image_file = open(file, 'r')
        image_file = image_file.readlines()[6:]

        i = 0
        for line in image_file:
            Image.name = line
            print(Image.name)
            next(image_file)
            row = line.split()
            print row

            for j in range(20):
                imageArray[i][j] = row[j]
            i += 1
            Image.values = imageArray
            next(image_file)

        file.close()
        return Image
