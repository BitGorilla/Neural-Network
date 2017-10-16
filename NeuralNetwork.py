"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from ImageRead import ImageRead
from Test import Test
from random import shuffle
import math
from decimal import Decimal
import numpy as np



def imageLoop(training, weights, mood, keylist):

    trainingpart = len(training)/3*2

    for x in range(trainingpart):
        xsad = 0
        xangry = 0
        xhappy = 0
        xmischievous = 0
        #Titta pa varje pixel
        imagestring = keylist[x]
        for i in range(20):
            for j in range(20):
                greyscale = normalize(int(training.get(imagestring)[i][j]))

                xsad = calculatexsad(i, j, greyscale, xsad)
                xangry = calculatexangry(i, j, greyscale, xangry)
                xhappy = calculatexhappy(i, j, greyscale, xhappy)
                xmischievous = calculatexmischievous(i, j, greyscale, xmischievous)


        asad = activation(xsad)
        aangry = activation(xangry)
        ahappy = activation(xhappy)
        amischievous = activation(xmischievous)

        facit = mood.get(keylist[x])
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

        #print weights["happy"+str(a)+str(b)]

def normalize(x):
    return x/31

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
    return 1 / (1 + np.exp(-x))

def createRandomListFromDict(dict):
    templist = dict.keys()
    shuffle(templist)
    return templist


if __name__ == '__main__':
    test = Test()
    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    weights = {}
    weights = imageRead.randomizeWeights()


    facit = imageRead.readfacit('training-facit.txt')

    bad = True
    while(bad):
        keylist = createRandomListFromDict(training)
        imageLoop(training, weights, facit, keylist)
        correctAnswers = test.test(facit, training, weights, keylist)
        print correctAnswers
        if  correctAnswers > 40:
            bad = False
            print "done"