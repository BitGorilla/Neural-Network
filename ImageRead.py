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

        try:
            for line in image_file:
                if line[0] == "#" or not line:
                    continue


                for x in range(21):
                    if x == 0:
                        Image.name = line
                        line = next(image_file)
                    else:
                        valueArray.append(line.split())
                        line = next(image_file)
                    print line
                Image.values = valueArray
                trainingArray.append(Image)
        except StopIteration as ex:
            pass

        image_file.close()
        return trainingArray
