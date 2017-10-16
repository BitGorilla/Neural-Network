"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from ImageRead import ImageRead
from Test import Test
import math


def imageLoop(training, weights, mood):


    for x in range(200):
        xsad = 0
        xangry = 0
        xhappy = 0
        xmischievous = 0
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


        asad = activation(xsad)
        aangry = activation(xangry)
        ahappy = activation(xhappy)
        amischievous = activation(xmischievous)

        facit = mood.get("Image" + str(x + 1))
        for a in range(20):
            for b in range(20):
                ysad = calcOutput(facit, "sad")
                yangry = calcOutput(facit, "angry")
                yhappy = calcOutput(facit, "happy")
                ymischievous = calcOutput(facit, "mischievous")

                wsad = computeWDiff(ysad,asad, greyscale)
                whappy = computeWDiff(yhappy, ahappy, greyscale)
                wangry = computeWDiff(yangry, aangry, greyscale)
                wmischievous = computeWDiff(ymischievous, amischievous, greyscale)

                weights["sad"+str(a)+str(b)] += wsad
                weights["happy"+str(a)+str(b)] += whappy
                weights["angry"+str(a)+str(b)] += wangry
                weights["mischievous"+str(a)+str(b)] += wmischievous

        print weights["happy"+str(a)+str(b)]

def calcOutput(facit, mood):
    if facit == 1 and mood == "happy":
        return 1
    elif facit == 2 and mood == "sad":
        return 1
    elif facit == 3 and mood == "mischievous":
        return 1
    elif facit == 4 and mood == "angry":
        return 1
    return 0

def computeWDiff(y, a, x):
    e = y - a
    w = 0.05*e*int(x)
    return w

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


def activation(x):
    return math.tanh(x)




if __name__ == '__main__':
    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    weights = {}
    weights = imageRead.randomizeWeights()


    facit = imageRead.readfacit('training-facit.txt')

    imageLoop(training, weights, facit)

    test = Test()
    #test.test(facit, training, weights)