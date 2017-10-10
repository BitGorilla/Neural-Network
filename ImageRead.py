"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from collections import namedtuple
from TableList import TableList

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
        """Table to have the name as key, and the array as value"""
        imageTable = TableList()
        string = "empty"
        valueArray = []

        """opens file to read"""
        image_file = open(file, 'r')

        try:
            for line in image_file:
                if line[0] == "#" or not line:
                    continue

                """saves the image name and the 20 lines of image values"""
                for x in range(21):
                    print "line is", x
                    print line
                    if x is 0:
                        string = line
                        print line
                        print "Name saved and is:",  string
                        line = next(image_file)
                    else:
                        valueArray.append(line.split())
                        line = next(image_file)
                imageTable.insert(string, valueArray)

        except StopIteration as ex:
            pass

        image_file.close()
        return imageTable
