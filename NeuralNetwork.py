"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from ImageRead import ImageRead

if __name__ == '__main__':
    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    print training.name[1]

