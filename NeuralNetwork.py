"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
import numpy as np

class NeuralNetwork:

    def __init__(self):
        pass


    def imageLoop(self, training, mood, keylist, weights):

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
                    greyscale = self.normalize(training.get(imagestring)[i][j])

                    xsad += self.calculatex(i, j, greyscale, "sad", weights)
                    xangry += self.calculatex(i, j, greyscale, "angry", weights)
                    xhappy += self.calculatex(i, j, greyscale, "happy", weights)
                    xmischievous += self.calculatex(i, j, greyscale,
                                                    "mischievous", weights)


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
                    #print "sad"+str(ysad) +" angry"+ str(yangry)+" happy"+str(yhappy)+" misch"+str(ymischievous)

                    wsad = self.computeWDiff(ysad, asad, greyscale)
                    whappy = self.computeWDiff(yhappy, ahappy, greyscale)
                    wangry = self.computeWDiff(yangry, aangry, greyscale)
                    wmischievous = self.computeWDiff(ymischievous, amischievous, greyscale)

                    #print "1 "+ str(weights["sad"+str(a)+str(b)])
                    weights["sad"+str(a)+str(b)] += wsad
                    #print "2 "+ str(weights["sad"+str(a)+str(b)])
                    weights["happy"+str(a)+str(b)] += whappy
                    weights["angry"+str(a)+str(b)] += wangry
                    weights["mischievous"+str(a)+str(b)] += wmischievous
        return weights


    def normalize(self,x):
        return float(x)/31

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

    def computeWDiff(self, y, a, x):
        e = y - a
        w = 0.05*e*float(x)
        return w

    def calculatex(self, i, j, greyscale, string, weights):
        x = weights.__getitem__(string+str(i)+str(j)) * greyscale
        return x

    def activation(self, x):
        return 1 / (1 + np.exp(-x))




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