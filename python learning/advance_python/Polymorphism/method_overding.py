
#polymorphism:-
class shape:
    def area(self):
        return 0

class rectangle(shape):
    def area(self,w,h):
        self.w,self.h=w,h

    def area(self):
        return self.w * self.h


class Circle(shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14 * self.r**2

shapes =[rectangle(3,4),Circle(3),rectangle(3,)]
for s in shapes:
    print(s.area())


    