#singel level:one parent one child
class Animal:
    def breathe(self):
        print("the breathin")

class Mammal(Animal):
    def feed_young(self):
        print("Feeding young..")

class Dog(Mammal):
    def bark(self):
        print("woof!")

d=Dog()

d.bark()
d.feed_young()
d.breathe()