# Python OOP - Inheritance

## Inheritance

Inheritance allows a child class to use the properties and methods of a parent class.

### Benefits:
- Code Reusability
- Reduces code duplication
- Creates a parent-child relationship


---

# Basic Inheritance

A child class inherits methods and attributes from a parent class.

### Syntax:

```python
class Parent:
    pass

class Child(Parent):
    pass
```

### Example:

```python
class Animal:
    def __init__(self, name:str, age:int)->None:
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


d1 = Dog("Abc", 6)

d1.speak()
d1.sleep()
d1.bark()

print(d1.age)
print(d1.name)
```

### Note:
- Dog class inherits `Animal` class.
- Dog can access parent methods (`speak`, `sleep`) and its own method (`bark`).


---

# Method Overriding

When a child class creates a method with the same name as the parent method, it is called **Method Overriding**.

The child method replaces the parent method.

Example:

```python
class Animal:

    def speak(self):
        print("The animal is speaking")


class Dog(Animal):

    def speak(self):
        print("Dog is barking")


d = Dog()

d.speak()
```

Output:

```
Dog is barking
```

### Note:
- Parent method does not run because child method overrides it.


---

# super() Keyword

`super()` is used to access the parent class methods and constructor.

It helps to call the parent implementation inside the child class.


## Using super() with Method

Example:

```python
class Animal:

    def speak(self):
        print("The animal is speaking")


class Dog(Animal):

    def speak(self):
        super().speak()
        print("Dog is barking")


d = Dog()

d.speak()
```

Output:

```
The animal is speaking
Dog is barking
```


---

# super() with __init__()

`super()` is used to call the parent constructor and initialize parent attributes.

Example:

```python
class Car:

    def __init__(self, brand):
        self.brand = brand


class Vehicle(Car):

    def __init__(self, fuel, brand):
        super().__init__(brand)
        self.fuel = fuel


    def display(self):
        print(f"You have {self.brand} and fuel type is {self.fuel}")


v = Vehicle("Petrol", "Maruti")

v.display()
```

Output:

```
You have Maruti and fuel type is Petrol
```


---

# Types of Inheritance


## 1. Single Level Inheritance

One parent class → One child class


Structure:

```
Animal
   |
  Dog
```


Example:

```python
class Animal:

    def breathe(self):
        print("Breathing")


class Dog(Animal):

    def bark(self):
        print("Woof!")


d = Dog()

d.breathe()
d.bark()
```


---

## 2. Multilevel Inheritance

A child class becomes a parent for another class.


Structure:

```
Animal
   |
 Mammal
   |
  Dog
```


Example:

```python
class Animal:

    def breathe(self):
        print("Breathing")


class Mammal(Animal):

    def feed_young(self):
        print("Feeding young")


class Dog(Mammal):

    def bark(self):
        print("Woof!")


d = Dog()

d.breathe()
d.feed_young()
d.bark()
```


---

## 3. Hierarchical Inheritance

One parent class has multiple child classes.


Structure:

```
          Animal
          /    \
       Dog      Cat
```


Example:

```python
class Animal:

    def breathe(self):
        print("Breathing")


class Dog(Animal):

    def bark(self):
        print("Dog barking")


class Cat(Animal):

    def meow(self):
        print("Cat meow")


d = Dog()
c = Cat()

d.breathe()
c.breathe()
```


---

## 4. Multiple Inheritance

One child class inherits from multiple parent classes.


Structure:

```
Dog + Cat
    |
 Combine
```


Example:

```python
class Dog:

    def hello(self):
        print("Dog")


class Cat:

    def hello(self):
        print("Cat")


class Combine(Dog, Cat):
    pass


d = Combine()

d.hello()
```


Output:

```
Dog
```


---

# MRO (Method Resolution Order)

MRO decides the order in which Python searches for methods in inheritance.

Example:

```python
print(Combine.__mro__)
```


For multiple inheritance:

```python
class Combine(Dog, Cat):
    pass
```

Python checks:

```
Combine → Dog → Cat → object
```


### Important:
- First matching method is executed.
- MRO follows the order of inheritance.


---

# Method Overloading

Python does not support traditional method overloading like Java or C++.

Example:

```python
class Calculator:

    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c
```

The second method replaces the first method.


## Alternative using Default Arguments

```python
def add(a,b,c=0):

    return a+b+c


print(add(2,3))

print(add(2,3,4))
```


Output:

```
5
9
```


## Alternative using *args

```python
def add(*numbers):

    return sum(numbers)


print(add(1,2))
print(add(1,2,3))
```


---

# Important Points

- Inheritance allows code reuse.
- Child class can access parent methods and attributes.
- Method overriding changes parent method behavior.
- `super()` calls parent methods and constructors.
- Python supports:
    - Single inheritance
    - Multilevel inheritance
    - Hierarchical inheritance
    - Multiple inheritance
- MRO decides method execution order.
- Python does not support true method overloading.