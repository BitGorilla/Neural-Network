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
            i = 0
            for line in image_file:
                if line[0] == "#" or not line.strip():
                    print "comment or empty line"
                    if i > 0:
                        print "i>0, insert to table"
                        imageTable.insert(string, valueArray)
                        print "insert complete"
                    i = 0
                    continue

                """saves the image name and the 20 lines of image values"""
                if i is 0:
                    string = line
                    print "Name is", string
                    i += 1
                else:
                    print "put line in valueArray"
                    valueArray.append(line.split())

                print line

        except StopIteration as ex:
            pass

        image_file.close()
        return imageTable