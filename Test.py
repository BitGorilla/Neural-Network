"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""

import math

class Test:

    def __init__(self):
        pass

    def test(self, facit, images, weights):
        correctAnswers = 0


        for x in range(100):
            sadsum = 0
            happysum = 0
            angrysum = 0
            mischievoussum = 0

            for y in range(20):
                for z in range(20):
                    greyscale = int(images.get("Image"+str(x+1))[y][z])

                    sadsum += weights.get("sad"+str(y)+str(z)) * greyscale
                    happysum += weights.get("happy"+str(y)+str(z)) * greyscale
                    angrysum += weights.get("angry"+str(y)+str(z)) * greyscale
                    mischievoussum += weights.get("mischievous"+str(y)+str(z)) * greyscale

            sadvote = self.activation(sadsum)
            happyvote = self.activation(happysum)
            angryvote = self.activation(angrysum)
            mischievousvote = self.activation(mischievoussum)

            answer = self.vote(happyvote, sadvote, mischievousvote, angryvote)
            facitanswer = facit.get("Image"+str(x+1))

            if int(facitanswer) == answer:
                correctAnswers += 1

        print "%d" %correctAnswers

    def activation(self, sum):
        return math.tanh(sum)

    def vote(self, a,b,c,d):
        vote = 1

        if b > a:
            vote = 2
        if c > b and c > a:
            vote = 3
        if d > c and d > b and d > a:
            vote = 4

        return vote