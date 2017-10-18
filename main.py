from Test import Test
from ImageRead import ImageRead
from NeuralNetwork import NeuralNetwork
import random


def createRandomListFromDict(dict):
    templist = dict.keys()
    random.shuffle(templist)
    return templist

def randomizeWeights():
    """Loop through the dict and add a randomized weight"""
    dict = {}
    for x in range(20):
        for y in range(20):
            dict['sad' + str(x) + str(y)] = random.uniform(0.4, 0.5)
            dict['happy' + str(x) + str(y)] = random.uniform(0.4, 0.5)
            dict['angry' + str(x) + str(y)] = random.uniform(0.4, 0.5)
            dict['mischievous' + str(x) + str(y)] = random.uniform(0.4, 0.5)
    return dict

if __name__ == '__main__':
    network = NeuralNetwork()
    test = Test()

    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    facit = imageRead.readfacit('training-facit.txt')
    weights = randomizeWeights()

    running = True
    while(running):
        keylist = createRandomListFromDict(training)
        print weights
        weights = network.imageLoop(training, facit, keylist, weights)
        correctAnswers = test.test(facit, training, weights, keylist)

        print correctAnswers
        if correctAnswers > 40:
            print "done"
            running = False