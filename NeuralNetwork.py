"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from ImageRead import ImageRead


def loopDict(training):

    for x in range(200):
        string = "Image" + str(x+1)

        for i in range(20):
            for j in range(20):
                if training.get(string)[i][j] > 8:
                    """activate"""


if __name__ == '__main__':
    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    loopDict(training)