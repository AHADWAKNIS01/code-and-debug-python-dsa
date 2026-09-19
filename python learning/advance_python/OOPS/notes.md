# Object-Oriented Programming (OOP)

OOP organizes code using **classes and objects**.

### Why OOP?

* Combines **data + behavior**
* Reusable and organized code
* Easier to maintain large projects
* Models real-world entities

---

# 1. Classes & Objects

### Class

A **class** is a blueprint for creating objects.

```python
class Student:
    pass
```

### Object

An **object** is an instance of a class.

```python
s1 = Student()
s2 = Student()
```

**Class → Blueprint**
**Object → Instance**

---

**class and object creation**
```python
class Student:
    roll_no=0
    name=""
    age=0

#object or instance created as s1
s1=Student()
s1.roll_no=7
print(s1.roll_no)
s2=Student
s2.roll_no=7
print(s2.roll_no)
```

**using the function**

# `self`

`self` refers to the **current object who is calling**.

```python
class Student:
    def show(self):
        print(self)

s1 = Student()
s1.show()
```

For `s1.show()`, `self` refers to `s1`.

---

# `__init__()`

`__init__()` runs automatically when an object is created.

Used to initialize object attributes.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ahad", 20)
```

* `self.name` → instance attribute
* `self.age` → instance attribute

---

# Instance Attributes

Attributes that belong to a **specific object**.

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Ahad")
s2 = Student("Rahul")
```

```text
s1.name → Ahad
s2.name → Rahul
```

Each object has its **own data**.

---

# Methods

Methods are functions defined inside a class.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Ahad", [80, 90, 85])

print(s1.average())
```

**Attributes → Data**
**Methods → Behavior**

---

# 2. Class Variables vs Instance Variables

### Instance Variable

Belongs to a specific object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

### Class Variable

Shared by all objects.

```python
class Student:
    school = "Rizvi College"

    def __init__(self, name):
        self.name = name
```

```python
s1 = Student("Ahad")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)
```

### Important

```text
Instance variable → unique for each object
Class variable    → shared by all objects
```

Avoid mutable class variables like:

```python
class Team:
    members = []
```

Use:

```python
class Team:
    def __init__(self):
        self.members = []
```

---

# 3. Types of Methods

## Instance Method

Works with object data.

Uses `self`.

```python
class Student:
    def show(self):
        print(self.name)
```

---

## Class Method

Works with class-level data.

Uses `@classmethod` and `cls`.

```python
class Student:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

```text
self → current object
cls  → current class
```

---

## Static Method

Does not need object or class data.

Uses `@staticmethod`.

```python
class MathUtils:

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathUtils.is_even(10))
```

### Quick Comparison

| Method   | First Parameter | Used For          |
| -------- | --------------- | ----------------- |
| Instance | `self`          | Object data       |
| Class    | `cls`           | Class data        |
| Static   | None            | Utility functions |

---

# 4. Four Pillars of OOP

## 1. Encapsulation

**Bundling data and methods together** and controlling access to data.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
```

`__balance` is treated as a private attribute.

---

## 2. Inheritance

A child class **reuses** properties and methods of a parent class.

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```

```text
Animal → Parent class
Dog    → Child class
```

---

## 3. Polymorphism

**One interface, many forms.**

Different classes can use the same method name with different behavior.

```python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")
```

Both have `speak()`, but behavior is different.

---

## 4. Abstraction

**Hiding implementation details** and showing only essential functionality.

Usually implemented using **abstract classes** and `ABC`.

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

---

# 5. `@property`

Allows a method to be accessed like an attribute.

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks
```

```python
s = Student(90)
print(s.marks)
```

---

# 6. Dunder Methods

Special methods with double underscores.

Examples:

```text
__init__  → initializes object
__str__   → string representation
__eq__    → equality comparison
__add__   → + operator
```

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

---

# 7. Multiple Inheritance & MRO

A class can inherit from multiple classes.

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

**MRO (Method Resolution Order)** determines the order Python searches for methods.

```python
print(C.mro())
```

---

# OOP Quick Revision

```text
Class       → Blueprint
Object      → Instance
self        → Current object
__init__    → Initialize object
Attribute   → Object data
Method      → Object behavior

Encapsulation → Control/hide data
Inheritance   → Reuse parent code
Polymorphism  → Same interface, different behavior
Abstraction   → Hide implementation details

Instance Method → self
Class Method    → cls
Static Method   → No self/cls
```
# Class Methods + Static Methods

## Class Method

Used when working with **class-level data**.

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
```

* `@classmethod` → decorator
* `cls` → current class
* Can access/modify class variables

---

## Static Method

Used for a **utility function** that doesn't need object/class data.

```python
class StringUtils:

    @staticmethod
    def reverse_string(s):
        return s[::-1]
```

* No `self`
* No `cls`
* Does not use object/class state

---

# Encapsulation

**Encapsulation = bundling data + methods together and controlling access to data.**

Benefits:

* Prevents accidental modification
* Allows validation
* Hides internal implementation

---

# Access Levels

### Public

Normal attribute. Accessible anywhere.

```python
self.name = name
```

### Protected

Single `_` → intended for internal use.

```python
self._balance = balance
```

Python does **not strictly prevent** access.

### Private

Double `__` → name mangling.

```python
self.__balance = balance
```

Python internally changes it roughly to:

```text
_ClassName__balance
```

Used mainly to avoid accidental access/name conflicts.

---

# Getters & Setters

Traditional approach:

```python
class Person:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
```

Python generally prefers `@property`.

---

# `@property`

Makes a method behave like an attribute.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

```python
p = Person(20)
print(p.age)
```

---

# `@property` + Setter

Used when you need **validation** while setting a value.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

```python
p = Person(20)

p.age = 25       # allowed
p.age = -5       # ValueError
```

---

# Read-Only Property

If no setter is provided, the property is read-only.

```python
@property
def age(self):
    return self._age
```

```text
p.age = 25  → AttributeError
```

---

# Property Deleter

Used to control deletion.

```python
@age.deleter
def age(self):
    del self._age
```

```python
del p.age
```

---

# Quick Revision

```text
Public       → name
Protected    → _name
Private      → __name

@property           → getter
@property.setter    → setter
@property.deleter   → deleter

Instance method → self → object data
Class method    → cls  → class data
Static method   → none → utility function
```

## Important Rule

**Start with normal public attributes.**

Use `@property` when you need:

* Validation
* Computed values
* Controlled access
* Side effects



# 3. Inheritance

**Inheritance = child class reuses attributes and methods of a parent class.**

```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Woof")

d = Dog()
d.eat()   # inherited
d.bark()  # own method
```

```text
Parent → Animal
Child  → Dog
```

Use inheritance for a true **"is-a"** relationship.

---

## Method Overriding

Child provides its own version of a parent method.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")
```

Child method gets priority.

---

## `super()`

Used to call the parent's method.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
```

### `super()` in `__init__`

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
```

`super()` → reuse parent logic.

---

# Types of Inheritance

### 1. Single

```text
A → B
```

One parent → one child.

### 2. Multilevel

```text
A → B → C
```

Grandparent → Parent → Child.

### 3. Hierarchical

```text
    A
   / \
  B   C
```

One parent → multiple children.

### 4. Multiple

```text
A   B
 \ /
  C
```

One child → multiple parents.

```python
class Duck(Flyer, Swimmer):
    pass
```

---

# MRO (Method Resolution Order)

MRO determines the order Python searches for methods.

```python
print(Duck.mro())
```

Example:

```text
D → B → C → A → object
```

Useful especially with **multiple inheritance**.

---

# `isinstance()` and `issubclass()`

### `isinstance()`

Checks whether an object belongs to a class or its subclass.

```python
isinstance(dog, Dog)
isinstance(dog, Animal)
```

### `issubclass()`

Checks whether one class inherits from another.

```python
issubclass(Dog, Animal)
```

---

# 4. Polymorphism

**Polymorphism = same interface, different behavior.**

```python
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Same call:

```text
animal.speak()
```

Different behavior.

### Types

* Method overriding
* Duck typing
* Operator overloading

---

# Duck Typing

Python focuses on **what an object can do**, not its class.

```python
class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("I'm quacking")

def make_quack(obj):
    obj.quack()
```

If the object has `quack()`, it works.

**"If it behaves like a duck, treat it like a duck."**

---

# Dunder Methods
---
**Dunder = Double Underscore methods.**

Special methods used by Python automatically.

| Method         | Purpose                  |
| -------------- | ------------------------ |
| `__init__`     | Object initialization    |
| `__str__`      | User-friendly string     |
| `__repr__`     | Developer representation |
| `__eq__`       | `==`                     |
| `__lt__`       | `<`                      |
| `__gt__`       | `>`                      |
| `__add__`      | `+`                      |
| `__sub__`      | `-`                      |
| `__mul__`      | `*`                      |
| `__len__`      | `len()`                  |
| `__getitem__`  | `obj[index]`             |
| `__contains__` | `in`                     |
| `__call__`     | `obj()`                  |

---

## `__str__` and `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
```
---
```text
__str__  → readable for users
__repr__ → useful for developers/debugging
```

---

## Operator Overloading

Allows operators to work with custom objects.

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)
```

Now:

```python
a + b
```

calls:

```python
a.__add__(b)
```

---

## Container Dunders

```python
__len__       → len(obj)
__getitem__   → obj[index]
__contains__  → item in obj
__setitem__   → obj[index] = value
__delitem__   → del obj[index]
```

---

## `__call__`

Makes an object callable like a function.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)

print(double(10))  # 20
```

---

# 5. Abstraction

**Abstraction = hiding how something works and exposing what it does.**

```text
Abstraction → Hide HOW
              Show WHAT
```

Example:

```python
shape.area()
```

You use `area()` without worrying about its internal calculation.

---

# Abstract Classes

Use `ABC` and `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

A class with abstract methods **cannot be instantiated** directly.

```python
Shape()  # TypeError
```

Child classes must implement the abstract methods.

```python
class Rectangle(Shape):
    def area(self):
        return 10
```

Now:

```python
r = Rectangle()
```

is allowed.

---

# Abstraction vs Encapsulation

```text
Abstraction
→ Hides HOW something works
→ Focuses on interface
→ ABC, abstractmethod

Encapsulation
→ Controls access to DATA
→ Focuses on protection
→ _, __, @property
```

### Easy Memory Trick

**Abstraction = HOW is hidden**

**Encapsulation = DATA is controlled**

---

# 4 Pillars of OOP

| Pillar        | Meaning                            |
| ------------- | ---------------------------------- |
| Encapsulation | Bundle + control data              |
| Inheritance   | Reuse parent code                  |
| Polymorphism  | Same interface, different behavior |
| Abstraction   | Hide implementation details        |

---

# OOP Best Practices

* Use **PascalCase** for class names.
* Use `self` in instance methods.
* Initialize attributes in `__init__`.
* Use `@property` when validation is needed.
* Use `super()` to reuse parent logic.
* Prefer **composition** for "has-a" relationships.
* Use inheritance for true **"is-a"** relationships.
* Keep classes focused on one responsibility.
* Use abstract classes when a clear contract is required.
* Add `__str__` / `__repr__` when useful for debugging.

---

# Common OOP Mistakes

```text
1. Forgetting self
2. Using mutable class variables accidentally
3. Overusing inheritance
4. Writing unnecessary getters/setters
5. Making everything private
6. Forgetting super().__init__()
7. Confusing == with is
8. Creating huge "God" classes
9. Not implementing useful __str__/__repr__
10. Using inheritance only for code sharing
```

---

# OOP Final Cheat Sheet

```text
Class       → Blueprint
Object      → Instance
self        → Current object
__init__    → Initialize object

Encapsulation → Control DATA
Inheritance   → Reuse CODE
Polymorphism  → Different BEHAVIOR
Abstraction   → Hide HOW

Instance Method → self
Class Method    → cls
Static Method   → No self/cls

super()       → Parent method
MRO           → Method search order
isinstance()  → Object relationship
issubclass()  → Class relationship

@property     → Controlled attribute
__str__       → User-friendly string
__repr__      → Developer representation
__eq__        → ==
__add__       → +
__len__       → len()
__getitem__   → []
__call__      → obj()
```
---
