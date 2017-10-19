"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
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
        imageDict = {}
        string = "empty"
        valueArray = []

        """opens file to read"""
        image_file = open(file, 'r')

        try:
            i = 0
            for line in image_file:
                if line[0] == "#" or not line.strip():
                    if i > 0:
                        imageDict[string] = valueArray
                        valueArray = []
                    i = 0
                    continue

                """saves the image name and the 20 lines of image values"""
                if i is 0:
                    string = line
                    string = string.rstrip('\n')
                    i += 1
                else:
                    valueArray.append(line.split())

        except StopIteration as ex:
            pass

        image_file.close()
        return imageDict

    def readfacit(self, file):

        facit = {}
        facit_file = open(file, 'r')

        try:
            for line in facit_file:
                if line[0] != "#" or not line.strip():
                    linestring = line.split()
                    facit[linestring[0]] = linestring[1].rstrip('\n')

        except StopIteration as ex:
            pass

        facit_file.close()
        return facit