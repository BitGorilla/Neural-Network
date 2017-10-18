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

            """Getting which image we should check from the list of keys"""
            imagestring = keylist[x]
            """Going through each pixel and calculating"""
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

            """Checking correct mood for the image and assigning a new weight to
             every mood in each pixel"""
            facit = mood.get(keylist[x])

            for a in range(20):
                for b in range(20):
                    """The greyscale for the current pixel"""
                    greyscale = self.normalize(training.get(imagestring)[a][b])

                    """Assigning each mood 1 or 0 depending on which mood the 
                    picture represents"""
                    ysad = self.calcOutput(facit, "sad")
                    yangry = self.calcOutput(facit, "angry")
                    yhappy = self.calcOutput(facit, "happy")
                    ymischievous = self.calcOutput(facit, "mischievous")

                    """Calculating w for each mood"""
                    wsad = self.computeWDiff(ysad, asad, greyscale)
                    whappy = self.computeWDiff(yhappy, ahappy, greyscale)
                    wangry = self.computeWDiff(yangry, aangry, greyscale)
                    wmischievous = self.computeWDiff(ymischievous, amischievous, greyscale)

                    """Setting new weights to each mood in the pixel"""
                    weights["sad"+str(a)+str(b)] += wsad
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
        x = weights.get(string + str(i) + str(j)) * greyscale
        return x

    def activation(self, x):
        return 1 / (1 + np.exp(-x))
