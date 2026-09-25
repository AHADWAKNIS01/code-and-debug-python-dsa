
#in this the parent method doesnt run to overiding
class Animals:
    def speak(self):
        print("the animal is speaking")


class Dog(Animals):
    def speak(self):
        print("Dog is braking")


d= Dog()
d.speak()

#and add the method overloading in short as it is not there in python