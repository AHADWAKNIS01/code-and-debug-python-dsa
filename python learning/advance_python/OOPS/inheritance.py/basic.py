#basic

class Animal:
    def __init__(self, name:str, age:int)->None:
        self.age=age
        self.name=name

    def speak(self):
        print(f"the {self.name} is speaking")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name}is barking")


d1=Dog("Abc",6)
d1.speak()
d1.sleep()
d1.bark()

print(d1.age)
print(d1.name)