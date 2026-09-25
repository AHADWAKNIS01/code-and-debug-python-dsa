#one parent->multiple child

class Animal:
    def __init__(self,name):
        self.name=name

    def breathe(self):
        print(f"{self.name} is breathing")

class dog(Animal):
    def hello(self):
        print("dog is barking")


class cat(Animal):
    def hello(self):
        print("moo!")


class combine(dog,cat):
    pass




d=combine("tom")
d.hello()
print(combine.__mro__)

#mro method of resoltuion order(mro)
