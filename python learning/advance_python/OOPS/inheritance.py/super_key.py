#to prevent the method overriding of 
# parent we use the 
# super key which the parent mthod


class Animal:
    def speak(self):
        print("the animal is speking")

    def display(self):
        print("this is a display function")


class Dog(Animal):
    def speak(self):
        super().speak()
        self.display()
        print("dog is barking")


d=Dog()
d.speak()