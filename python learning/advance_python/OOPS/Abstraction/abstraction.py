#abstraction class and method 

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,l,b):

        self.l=l
        self.b=b

    def area(self):
        return self.l+self.b


    def perimeter(self):
        return 2*(self.l+self.b)


rect=Rectangle(3,4)
print(rect.area())
print(rect.perimeter)


