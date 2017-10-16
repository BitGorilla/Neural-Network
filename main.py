from Test import Test
from ImageRead import ImageRead
from NeuralNetwork import NeuralNetwork
import random


def createRandomListFromDict(dict):
    templist = dict.keys()
    random.shuffle(templist)
    return templist


if __name__ == '__main__':
    network = NeuralNetwork()
    test = Test()

    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    facit = imageRead.readfacit('training-facit.txt')

    running = True
    while(running):
        weights = network.getWeights()
        keylist = createRandomListFromDict(training)
        network.imageLoop(training, facit, keylist)
        correctAnswers = test.test(facit, training, weights, keylist)

        print correctAnswers
        if correctAnswers > 40:
            print "done"
            running = False