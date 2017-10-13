"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from ImageRead import ImageRead


def imageLoop(training, weights):
    xsad = 0
    xangry = 0
    xhappy = 0
    xmischievous = 0

    for x in range(200):
        string = "Image" + str(x+1)
        #Titta pa varje pixel
        imagestring = "Image" + str(x + 1)
        for i in range(20):
            for j in range(20):
                greyscale = training.get(imagestring)[i][j]

                xsad = calculatexsad(i, j, greyscale, xsad)
                xangry = calculatexangry(i, j, greyscale, xangry)
                xhappy = calculatexhappy(i, j, greyscale, xhappy)
                xmischievous = calculatexmischievous(i, j, greyscale, xmischievous)

    print xsad
    print xangry
    print xhappy
    print xmischievous

def calculatexsad(i, j, greyscale, xsad):
    xsad = xsad + (
        weights.get("sad" + str(i) + str(j)) * int(greyscale))
    return xsad

def calculatexangry(i, j, greyscale, xangry):
    xangry = xangry + (
        weights.get("angry" + str(i) + str(j)) * int(greyscale))
    return xangry

def calculatexhappy(i, j, greyscale, xhappy):
    xhappy = xhappy + (
        weights.get("happy" + str(i) + str(j)) * int(greyscale))
    return xhappy

def calculatexmischievous(i, j, greyscale, xmischievous):
    xmischievous = xmischievous + (
        weights.get("mischievous" + str(i) + str(j)) * int(greyscale))
    return xmischievous



"""def activation(x):
    a = tanh(x)"""


if __name__ == '__main__':
    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    weights = {}
    weights = imageRead.randomizeWeights()
    imageLoop(training, weights)

