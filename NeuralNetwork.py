"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjolund
Fredrik Ostlund
2017-10-04
"""
from ImageRead import ImageRead
from TableList import TableList

if __name__ == '__main__':
    training = TableList
    imageRead = ImageRead()
    training = imageRead.readImage('training.txt')

    print training.lookup("Image1")