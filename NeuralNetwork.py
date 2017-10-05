"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from ImageRead import ImageRead

if __name__ == '__main__':
    training = []
    imageRead = ImageRead()
    training.append(imageRead.readImage('training.txt'))

    print training[1].name

