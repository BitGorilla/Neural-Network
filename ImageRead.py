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
        Image = namedtuple('Face', 'name values mood')
        valueArray = []
        trainingArray = []

        image_file = open(file, 'r')
        next(image_file)
        next(image_file)
        next(image_file)
        next(image_file)
        next(image_file)

        try:
            for line in image_file:
                Image.name = line
                print line
                line = next(image_file)

                for x in range(20):
                    print(x)
                    valueArray.append(line.split())
                    print line
                    line = next(image_file)

                Image.values = valueArray
                trainingArray.append(Image)
        except StopIteration as ex:
            pass

        image_file.close()
        return trainingArray
