
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):        #ABC meata class cha upayog ekhad perticular function saglayyankade aasav aasa aadesh deto
    @abstractmethod  #print area function saglayyankade aasav aasa aadesh detay
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

