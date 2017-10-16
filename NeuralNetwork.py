"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
import random
import numpy as np

class NeuralNetwork:

    weights = {}

    def __init__(self):
        self.randomizeWeights()
        pass


    def imageLoop(self, training, mood, keylist):

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
                    greyscale = self.normalize(float(training.get(imagestring)[i][j]))

                    xsad = self.calculatexsad(i, j, greyscale, xsad)
                    xangry = self.calculatexangry(i, j, greyscale, xangry)
                    xhappy = self.calculatexhappy(i, j, greyscale, xhappy)
                    xmischievous = self.calculatexmischievous(i, j, greyscale, xmischievous)


            asad = self.activation(xsad)
            aangry = self.activation(xangry)
            ahappy = self.activation(xhappy)
            amischievous = self.activation(xmischievous)

            facit = mood.get(keylist[x])
            for a in range(20):
                for b in range(20):
                    ysad = self.calcOutput(facit, "sad")
                    yangry = self.calcOutput(facit, "angry")
                    yhappy = self.calcOutput(facit, "happy")
                    ymischievous = self.calcOutput(facit, "mischievous")

                    wsad = self.computeWDiff(ysad,asad, greyscale)
                    whappy = self.computeWDiff(yhappy, ahappy, greyscale)
                    wangry = self.computeWDiff(yangry, aangry, greyscale)
                    wmischievous = self.computeWDiff(ymischievous, amischievous, greyscale)

                    self.weights["sad"+str(a)+str(b)] += wsad
                    self.weights["happy"+str(a)+str(b)] += whappy
                    self.weights["angry"+str(a)+str(b)] += wangry
                    self.weights["mischievous"+str(a)+str(b)] += wmischievous


    def normalize(self,x):
        return x/31

    def calcOutput(self,facit, mood):
        if facit == '1' and mood == "happy":
            return 1
        elif facit == '2' and mood == "sad":
            return 1
        elif facit == '3' and mood == "mischievous":
            return 1
        elif facit == '4' and mood == "angry":
            return 1
        else:
            return 0

    def computeWDiff(self,y, a, x):
        e = y - a
        w = 0.05*e*int(x)
        return w

    def calculatexsad(self, i, j, greyscale, xsad):
        xsad = xsad + (
            self.weights.get("sad" + str(i) + str(j)) * int(greyscale))
        return xsad

    def calculatexangry(self, i, j, greyscale, xangry):
        xangry = xangry + (
            self.weights.get("angry" + str(i) + str(j)) * int(greyscale))
        return xangry

    def calculatexhappy(self, i, j, greyscale, xhappy):
        xhappy = xhappy + (
            self.weights.get("happy" + str(i) + str(j)) * int(greyscale))
        return xhappy

    def calculatexmischievous(self, i, j, greyscale, xmischievous):
        xmischievous = xmischievous + (
            self.weights.get("mischievous" + str(i) + str(j)) * int(greyscale))
        return xmischievous


    def activation(self,x):
        return 1 / (1 + np.exp(-x))


    def randomizeWeights(self):
        """Loop through the dict and add a randomized weight"""
        for x in range(20):
            for y in range(20):
                self.weights['sad' + str(x) + str(y)] = random.uniform(0.4, 0.5)
                self.weights['happy' + str(x) + str(y)] = random.uniform(0.4, 0.5)
                self.weights['angry' + str(x) + str(y)] = random.uniform(0.4, 0.5)
                self.weights['mischievous' + str(x) + str(y)] = random.uniform(0.4, 0.5)
        count = 0
        for x in range(20):
            for y in range(20):
                if self.weights.get('sad' + str(x) + str(y)):
                    count += 1

    def getWeights(self):
        return self.weights

    """if __name__ == '__main__':
        test = Test()
        imageRead = ImageRead()
        training = imageRead.readImage('training.txt')

        weights = {}
        weights = imageRead.randomizeWeights()


        facit = imageRead.readfacit('training-facit.txt')

        bad = True
        rounds = 0
        while(bad and rounds < 20):
            keylist = createRandomListFromDict(training)
            imageLoop(training, weights, facit, keylist)
            correctAnswers = test.test(facit, training, weights, keylist)
            print correctAnswers
            if correctAnswers > 40:
                bad = False
                print "done"
            rounds += 1"""