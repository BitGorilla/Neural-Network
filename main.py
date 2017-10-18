from Test import Test
from ImageRead import ImageRead
from NeuralNetwork import NeuralNetwork
import random, sys


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

def main():
    if (len(sys.argv) > 1):
        file_training = sys.argv[1]
        file_facit = sys.argv[2]
        file_test = sys.argv[3]
    else:
        file_training = "training.txt"
        file_facit = "training-facit.txt"
        file_test = "test-images.txt"

    return file_training, file_facit, file_test

if __name__ == '__main__':
    network = NeuralNetwork()
    test = Test()

    training_images, training_facit, test_images = main()

    imageRead = ImageRead()
    training = imageRead.readImage(training_images)

    facit = imageRead.readfacit(training_facit)
    weights = randomizeWeights()

    running = True
    while(running):
        keylist = createRandomListFromDict(training)

        weights = network.imageLoop(training, facit, keylist, weights)
        correctAnswers = test.testtraining(facit, training, weights, keylist)

        print correctAnswers
        if correctAnswers > 80:
            print "Ready for Real Test, Let's go!"
            running = False

    if test_images != 0:
        test_dict = imageRead.readImage(test_images)
        test.realtest(test_dict, weights)
