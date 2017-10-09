"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from collections import namedtuple

class ImageRead:

    """
    Constructs a new "ImageRead" object
    :return: returns nothing

    """
    def __init__(self):
        pass

    """
    Opens a textfile and reads the lines to an array
    :param file: The text file to read from
    :returns: an array for the Neural Network to train from
    """
    def readImage(self, file):
        """namedtuple to save images in, aswell as arrays to keep data"""
        Image = namedtuple('Face', 'name values mood')
        valueArray = []
        trainingArray = []

        """opens file to read"""
        image_file = open(file, 'r')

        try:
            for line in image_file:
                if line[0] == "#" or not line:
                    continue

                """saves the image name and the 20 lines of image values"""
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
