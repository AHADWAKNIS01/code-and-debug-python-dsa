#one parent->multiple child

class Animal:
    def __init__(self,name):
        self.name=name

    def breathe(self):
        print(f"{self.name} is breathing")

class dog(Animal):
    def bark(self):
        print("dog is barking")


class cat(Animal):
    def moo(self):
        print("moo!")


d=dog("rex")
c=cat("whiskers")
d.breathe()
c.breathe()
