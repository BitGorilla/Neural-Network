"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""

import random
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
                    #print "comment or empty line"
                    if i > 0:
                        #print "i>0, insert to dict"
                        imageDict[string] = valueArray
                        valueArray = []
                        #print "insert complete"
                    i = 0
                    continue

                """saves the image name and the 20 lines of image values"""
                if i is 0:
                    string = line
                    string = string.rstrip('\n')
                    #print "Name is", string
                    i += 1
                else:
                    #print "put line in valueArray"
                    valueArray.append(line.split())

                #print line

        except StopIteration as ex:
            pass

        image_file.close()

        return imageDict

    def readfacit(self, file):

        facit = {}
        facit_file = open(file, 'r')

        try:
            for line in facit_file:
               if line[0] == "#" or not line.strip():
                   linestring = line.split()
                   facit[linestring[0]] = linestring[1]

        except StopIteration as ex:
            pass
        facit_file.close()

        return facit

    def randomizeWeights(self):
        weightdict = {}
        """Loop through the dict and add a randomized weight"""
        for x in range(20):
            for y in range(20):
                weightdict['sad' + str(x) + str(y)] = random.uniform(0.4, 0.5)
                weightdict['happy' + str(x) + str(y)] = random.uniform(0.4, 0.5)
                weightdict['angry' + str(x) + str(y)] = random.uniform(0.4, 0.5)
                weightdict['mischievous' + str(x) + str(y)] = random.uniform(0.4, 0.5)
        count = 0
        for x in range(20):
            for y in range(20):
                if weightdict.get('sad' + str(x) + str(y)):
                    count += 1

        print count

        return weightdict



