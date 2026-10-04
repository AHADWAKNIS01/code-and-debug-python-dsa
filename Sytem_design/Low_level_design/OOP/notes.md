# Object-Oriented Programming (OOP) — Complete Notes

---

# 1. Introduction to OOP

## What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around **objects and classes** rather than writing one long sequence of instructions.

An object represents something that has:

- **Data** → properties/attributes
- **Behavior** → methods/functions

### Simple Example

A `Student` object can have:

**Data:**
- name
- age
- gender

**Behavior:**
- display information
- update information

Instead of keeping all the data and functions separately, OOP groups related data and behavior together inside a class.

---

## Why Was OOP Introduced?

In procedural programming, we generally write instructions step-by-step.

For example, a banking application may contain:

1. Create staff
2. Create customer
3. Create account
4. Create transaction
5. Login
6. Logout
7. Transfer money
8. Generate reports

As the application becomes larger, managing all these instructions and functions becomes difficult.

### Problems with large procedural programs

- Code becomes difficult to understand.
- Debugging becomes harder.
- Code repetition increases.
- Maintaining the application becomes difficult.
- Adding new features can affect existing code.
- Related data and functions may be scattered throughout the program.

### How OOP Helps

OOP organizes related code into **classes and objects**.

This makes applications:

- More structured
- Easier to understand
- Easier to maintain
- Easier to debug
- Easier to extend
- More reusable

---

# 2. Real-World Objects

OOP is based on the idea that we can represent real-world entities as objects.

### Examples

| Real-World Entity | Possible Object |
|---|---|
| Student | `student1` |
| Car | `car1` |
| Bank Account | `account1` |
| Employee | `employee1` |
| Product | `product1` |
| Dog | `dog1` |

Each object can have its own data and behavior.

### Example: Car

A car can have:

**Attributes:**
- color
- model
- speed
- brand

**Methods:**
- start()
- stop()
- accelerate()
- brake()

OOP allows us to represent this real-world concept in code.

---

# 3. Four Main Pillars of OOP

The four major pillars of Object-Oriented Programming are:

1. **Encapsulation**
2. **Inheritance**
3. **Polymorphism**
4. **Abstraction**

### ⭐ Interview Point

Remember:

> **EIPA = Encapsulation, Inheritance, Polymorphism, Abstraction**

These four concepts form the foundation of OOP.

---

# 4. Class and Object

## 4.1 What is a Class?

A **class** is a blueprint, template, or design used to create objects.

It defines:

- What data an object can have
- What behavior an object can perform

A class itself is not the actual real-world entity. It is the design used to create entities.

### Example

A `Car` class is like a blueprint for manufacturing cars.

```python
class Car:
    color = ""
    brand = ""
    speed = 0
```

The class defines what information a car object can have.

---

# 5. What is an Object?

An **object** is an actual instance of a class.

When we create an object from a class, memory is allocated for that object and it can contain its own data.

### Example

```python
class Car:
    color = ""
    brand = ""

car1 = Car()
car2 = Car()
```

Here:

- `Car` → class
- `car1` → object
- `car2` → object

Both objects are created from the same class, but they can contain different values.

### Real-World Analogy

**Class → Blueprint**

**Object → Actual product created from the blueprint**

For example:

```text
Car Class
   ↓
   ├── car1
   ├── car2
   └── car3
```

All three objects follow the structure defined by the `Car` class.

---

# 6. Class vs Object

| Class | Object |
|---|---|
| Blueprint/template | Actual instance |
| Defines structure | Contains actual data |
| Used to create objects | Created from a class |
| Logical definition | Actual entity in memory |
| Example: `Car` | Example: `car1` |

### ⭐ Interview Question

**Q: What is the difference between a class and an object?**

**Answer:**

A class is a blueprint or template that defines the attributes and methods of an entity, while an object is an actual instance of that class containing its own data.

---

# 7. Creating a Class in Python

Python uses the `class` keyword to define a class.

```python
class Student:
    name = ""
    age = 0
    gender = ""
```

Here:

- `Student` is the class name.
- `name`, `age`, and `gender` are attributes.

---

# 8. Creating an Object

To create an object:

```python
S1 = Student()
```

Here:

- `Student()` creates an object.
- `S1` stores a reference to that object.

We can create multiple objects:

```python
S1 = Student()
S2 = Student()
S3 = Student()
```

Each object is a separate instance of the `Student` class.

---

# 9. Accessing Attributes

The **dot (`.`) operator** is used to access attributes and methods.

```python
print(S1.name)
print(S1.age)
print(S1.gender)
```

We can also modify values:

```python
S1.name = "Ahad"
S1.age = 20
S1.gender = "Male"
```

Then:

```python
print(S1.name)
print(S1.age)
print(S1.gender)
```

Output:

```text
Ahad
20
Male
```

---

# 10. Methods in a Class

A function defined inside a class is called a **method**.

Example:

```python
class Student:

    def display(self):
        print("Student information")
```

`display()` is a method of the `Student` class.

We can call it using an object:

```python
S1 = Student()
S1.display()
```

---

# 11. The `self` Keyword

## What is `self`?

`self` refers to the **current object/instance** that is calling the method.

It allows us to access the attributes and methods belonging to that particular object.

Example:

```python
class Student:

    def display(self):
        print(f"My name is {self.name}")
```

Suppose:

```python
S1 = Student()
S1.name = "Ahad"

S2 = Student()
S2.name = "Rahul"

S1.display()
S2.display()
```

Output:

```text
My name is Ahad
My name is Rahul
```

When:

```python
S1.display()
```

`self` refers to `S1`.

When:

```python
S2.display()
```

`self` refers to `S2`.

### Important

`self` is not a special keyword like `class` or `def`. It is the conventional name used for the current instance.

You technically can use another name, but **you should always use `self`** because it is the standard Python convention.

---

# 12. Why Do We Use `self`?

Suppose two students have different names.

```python
S1.name = "Ahad"
S2.name = "Rahul"
```

When `S1.display()` is called, Python needs to know which object's `name` should be accessed.

`self` provides that reference.

```python
self.name
```

means:

> Access the `name` attribute belonging to the current object.

### ⭐ Interview Point

`self` allows each object to access and modify **its own instance attributes**.

---

# 13. Setting Information Using a Method

Instead of manually assigning every attribute:

```python
S1.name = "Ahad"
S1.age = 20
S1.gender = "Male"
```

we can create a method:

```python
class Student:

    def set_info(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
```

Create an object:

```python
S1 = Student()

S1.set_info("Ahad", 20, "Male")
S1.display()
```

Output:

```text
Name: Ahad
Age: 20
Gender: Male
```

---

# 14. Instance Attributes

Attributes created using `self` are generally **instance attributes**.

Example:

```python
class Student:

    def set_info(self, name, age):
        self.name = name
        self.age = age
```

Here:

```python
self.name
self.age
```

belong to the particular object.

For example:

```python
S1 = Student()
S1.set_info("Ahad", 20)

S2 = Student()
S2.set_info("Rahul", 21)
```

The objects contain different values:

```text
S1 → name = Ahad,  age = 20
S2 → name = Rahul, age = 21
```

---

# 15. Type Annotations

Python supports **type annotations**.

They tell developers what type of data is expected.

Example:

```python
def set_info(self, name: str, age: int, gender: str) -> None:
    self.name = name
    self.age = age
    self.gender = gender
```

Here:

```python
name: str
```

means `name` is expected to be a string.

```python
age: int
```

means `age` is expected to be an integer.

```python
gender: str
```

means `gender` is expected to be a string.

```python
-> None
```

means the function is expected to return nothing.

---

## Important Point About Type Annotations

Python generally **does not enforce type annotations at runtime**.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

The annotation says `a` and `b` are expected to be integers, but Python does not automatically prevent other types from being passed.

### ⭐ Interview Point

> Type annotations improve readability, documentation, IDE support, and static type checking, but Python's normal runtime does not enforce them automatically.

---

# 16. Constructor / `__init__()`

## What is `__init__()`?

`__init__()` is a special method in Python that is automatically called when an object is created.

It is commonly called the **constructor** in beginner-level Python discussions, although technically `__new__()` is responsible for creating the object and `__init__()` initializes it.

For interviews, it is safe to say:

> `__init__()` is the initializer method that automatically runs when an object is created.

---

# 17. Why Do We Use `__init__()`?

Without `__init__()`:

```python
class Student:
    pass

S1 = Student()

S1.name = "Ahad"
S1.age = 20
```

We have to manually assign values after creating the object.

Using `__init__()`:

```python
class Student:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
```

Now:

```python
S1 = Student("Ahad", 20, "Male")
```

The values are automatically initialized when the object is created.

---

# 18. Complete `__init__()` Example

```python
class Student:

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


S1 = Student("Ahad", 20, "Male")

S1.display()
```

Output:

```text
Name: Ahad
Age: 20
Gender: Male
```

---

# 19. How `__init__()` Works

When we write:

```python
S1 = Student("Ahad", 20, "Male")
```

Python creates the object and initializes it by calling:

```python
__init__(S1, "Ahad", 20, "Male")
```

Conceptually, `self` refers to `S1`.

Therefore:

```python
self.name = name
```

becomes:

```python
S1.name = "Ahad"
```

Similarly:

```python
self.age = age
```

becomes:

```python
S1.age = 20
```

---

# 20. Inheritance

## What is Inheritance?

**Inheritance** is an OOP feature where one class can acquire the attributes and methods of another class.

The existing class is called the:

- Parent class
- Base class
- Superclass

The new class is called the:

- Child class
- Derived class
- Subclass

---

# 21. Why Use Inheritance?

Inheritance mainly helps with:

- Code reuse
- Reducing code duplication
- Creating relationships between classes
- Extending existing functionality

### Real-World Example

Suppose we have an `Animal` class.

All animals may have common behaviors such as:

- eat()
- sleep()

A `Dog` is an animal, so instead of rewriting `eat()` and `sleep()` inside `Dog`, we can inherit them from `Animal`.

Then `Dog` can add its own behavior:

- bark()

---

# 22. Basic Inheritance Example

```python
class Animal:

    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")


class Dog(Animal):

    def bark(self):
        print("Barking...")
```

Create a Dog object:

```python
dog = Dog()

dog.eat()
dog.sleep()
dog.bark()
```

Output:

```text
Eating...
Sleeping...
Barking...
```

The `Dog` class automatically gets:

```text
eat()
sleep()
```

from `Animal`.

It also has its own:

```text
bark()
```

---

# 23. Syntax of Inheritance

```python
class ChildClass(ParentClass):
    # child class code
```

Example:

```python
class Dog(Animal):
    pass
```

Here:

```text
Animal → Parent class
Dog    → Child class
```

---

# 24. Advantages of Inheritance

### 1. Code Reusability

Common functionality can be written once in the parent class.

### 2. Less Code Duplication

Child classes can reuse existing methods.

### 3. Easy Extension

A child class can add new methods or override existing methods.

### 4. Better Organization

It represents natural relationships between entities.

Example:

```text
Animal
  ↓
 ├── Dog
 ├── Cat
 └── Horse
```

---

# 25. `super()`

## What is `super()`?

`super()` is used to access functionality from the parent class.

It is commonly used when a child class needs to call the parent class's `__init__()` method.

Example:

```python
class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
```

Create object:

```python
dog = Dog("Tommy", 3, "Labrador")
```

Here:

```python
super().__init__(name, age)
```

calls the parent's initializer.

The parent initializes:

```python
self.name
self.age
```

The child initializes:

```python
self.breed
```

---

# 26. Why Use `super()`?

Without `super()`:

```python
class Dog(Animal):

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
```

We may have to duplicate the parent's initialization logic.

With `super()`:

```python
class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
```

The parent handles its own initialization.

### ⭐ Interview Point

> `super()` provides a convenient way to access methods of a parent class, especially the parent initializer.

---

# 27. Encapsulation

## What is Encapsulation?

**Encapsulation** means bundling data and methods together inside a class and controlling how the internal data is accessed or modified.

It helps protect an object's internal state.

### Simple Example

A bank account has:

```text
balance
```

We generally don't want anyone to directly modify the balance without validation.

Instead of allowing:

```python
account.balance = -100000
```

we can control access through methods.

---

# 28. Access Levels in Python

Python commonly uses naming conventions to indicate different levels of access:

1. Public
2. Protected
3. Private

---

# 29. Public Members

Public members can be accessed from outside the class.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Ahad"
```

Access:

```python
student = Student()

print(student.name)
```

`name` is public.

---

# 30. Protected Members

A protected member is conventionally indicated using a **single underscore (`_`)**.

Example:

```python
class Student:

    def __init__(self):
        self._name = "Ahad"
```

The underscore means:

> This member is intended for internal use or use by subclasses.

However, Python does **not** strictly prevent outside access.

You can technically do:

```python
student._name
```

### Important

Protected in Python is primarily a **convention**, not strict access control.

---

# 31. Private Members

Private members are conventionally created using **double underscores (`__`)**.

Example:

```python
class Bank:

    def __init__(self, balance):
        self.__balance = balance
```

Now `__balance` is intended to be accessed only through the class interface.

Direct access:

```python
bank.__balance
```

will normally result in an `AttributeError`.

---

# 32. Name Mangling

Python implements double-underscore private attributes using **name mangling**.

For example:

```python
self.__balance
```

inside class `Bank` is internally transformed approximately into:

```python
self._Bank__balance
```

This means Python does not provide absolute/private security in the same way as some languages.

It mainly prevents accidental access and naming conflicts.

### ⭐ Interview Point

> Python's `__private` members use name mangling; they are not absolutely inaccessible.

---

# 33. Getters and Setters

Getters and setters are methods used to control access to data.

### Getter

A getter is used to **retrieve/read** a value.

### Setter

A setter is used to **modify/update** a value.

---

# 34. Getter Example

```python
class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

Usage:

```python
bank = Bank(10000)

print(bank.get_balance())
```

Output:

```text
10000
```

The private variable is accessed through a public method.

---

# 35. Setter Example

A setter can validate data before modifying it.

```python
class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")
```

Usage:

```python
bank = Bank(10000)

bank.set_balance(15000)

print(bank.get_balance())
```

Output:

```text
15000
```

If:

```python
bank.set_balance(-5000)
```

the setter can reject the invalid value.

### Why is this Encapsulation?

Because the internal variable:

```python
__balance
```

is protected from uncontrolled modification and access happens through controlled methods.

---

# 36. Abstraction

## What is Abstraction?

**Abstraction** means hiding unnecessary implementation details and exposing only the essential functionality to the user.

In simple words:

> Show **what** an object does, while hiding **how** it does it.

---

# 37. Real-World Example of Abstraction

Consider an ATM.

You can perform:

- Withdraw money
- Deposit money
- Check balance

You don't need to know the internal implementation:

- How the bank server processes the request
- How authentication is performed
- How the transaction is recorded
- How the database is updated

You simply use the required functionality.

That is abstraction.

---

# 38. Abstraction in Python

Python provides the `abc` module for creating **Abstract Base Classes (ABCs)**.

We can use:

```python
from abc import ABC, abstractmethod
```

---

# 39. Abstract Class

An **abstract class** is a class intended to serve as a blueprint for subclasses.

It generally contains one or more abstract methods.

An abstract class containing abstract methods **cannot be instantiated directly**.

Example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Here:

```python
Shape
```

is an abstract class.

---

# 40. Abstract Method

An **abstract method** is a method declared in an abstract class that must be implemented by a concrete subclass.

Example:

```python
@abstractmethod
def area(self):
    pass
```

The parent class says:

> Every concrete Shape must provide an `area()` implementation.

It does not provide the actual implementation.

---

# 41. Implementing an Abstract Class

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
```

Now:

```python
rectangle = Rectangle(10, 5)

print(rectangle.area())
```

Output:

```text
50
```

The `Rectangle` class implements the required `area()` method.

---

# 42. What Happens If We Don't Implement the Abstract Method?

Suppose:

```python
class Circle(Shape):
    pass
```

Since `Circle` does not implement:

```python
area()
```

it remains abstract.

Therefore:

```python
circle = Circle()
```

will raise an error because the class cannot be instantiated until the abstract method is implemented.

### ⭐ Interview Point

> A concrete subclass must implement all inherited abstract methods before it can normally be instantiated.

---

# 43. Encapsulation vs Abstraction

These two concepts are commonly confused.

| Encapsulation | Abstraction |
|---|---|
| Controls access to data and implementation | Hides unnecessary implementation details |
| Focuses on protecting internal state | Focuses on exposing essential functionality |
| Uses classes, access conventions, properties, methods | Can use ABCs and abstract methods |
| Example: private `__balance` | Example: abstract `area()` |

### Easy Way to Remember

**Encapsulation → "How do I control access?"**

**Abstraction → "What should I expose?"**

---

# 44. Inheritance vs Encapsulation vs Abstraction

### Inheritance

> Reuse and extend functionality from another class.

### Encapsulation

> Bundle data and methods and control access to internal data.

### Abstraction

> Hide unnecessary implementation details and expose essential functionality.

### Polymorphism

> Allow the same interface/method call to behave differently depending on the object.

---

# 45. Polymorphism

The lecture listed polymorphism as one of the four pillars but did not cover it in detail.

## What is Polymorphism?

**Polymorphism** means "many forms."

It allows the same method/interface to behave differently for different objects.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

Both classes have:

```python
sound()
```

but the behavior is different.

```python
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Output:

```text
Bark
Meow
```

The same method name:

```python
sound()
```

produces different behavior depending on the object.

---

# 46. Method Overriding

A common form of polymorphism in Python is **method overriding**.

A child class provides its own implementation of a method already defined in the parent class.

Example:

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")
```

Now:

```python
animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
```

Output:

```text
Animal makes a sound
Dog barks
```

The `Dog` class overrides the parent's `sound()` method.

---

# 47. Four Pillars — Complete Understanding

## 1. Encapsulation

Protect/control access to internal data.

**Example:**

```python
self.__balance
```

---

## 2. Inheritance

Allow a child class to reuse and extend a parent class.

**Example:**

```python
class Dog(Animal):
```

---

## 3. Polymorphism

Same interface/method can have different behavior.

**Example:**

```python
dog.sound()
cat.sound()
```

---

## 4. Abstraction

Hide unnecessary implementation details and expose essential functionality.

**Example:**

```python
@abstractmethod
def area(self):
    pass
```

---

# 48. Complete OOP Example

The following example combines several OOP concepts:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


dog = Dog("Tommy")
cat = Cat("Kitty")

print(dog.get_name())
dog.sound()

print(cat.get_name())
cat.sound()
```

### Concepts Used

**Encapsulation:**

```python
self.__name
```

The name is private.

**Getter:**

```python
get_name()
```

Used to access the private data.

**Inheritance:**

```python
class Dog(Animal)
class Cat(Animal)
```

Both inherit from `Animal`.

**Abstraction:**

```python
class Animal(ABC)
```

and:

```python
@abstractmethod
def sound(self):
```

**Polymorphism:**

Both `Dog` and `Cat` implement:

```python
sound()
```

but produce different behavior.

---

# 49. Important OOP Terminology

| Term | Meaning |
|---|---|
| Class | Blueprint/template for objects |
| Object | Instance of a class |
| Attribute | Data/property associated with an object/class |
| Method | Function defined inside a class |
| `self` | Reference to the current instance |
| `__init__()` | Initializer automatically called during object initialization |
| Parent class | Class being inherited from |
| Child class | Class that inherits from another class |
| `super()` | Used to access parent-class functionality |
| Encapsulation | Bundling data and controlling access |
| Abstraction | Hiding unnecessary implementation details |
| Inheritance | Reusing/extending another class |
| Polymorphism | Same interface with different behavior |
| Getter | Method used to retrieve data |
| Setter | Method used to modify data |
| Abstract class | Class intended as a blueprint and not directly instantiated when abstract methods remain |
| Abstract method | Method that concrete subclasses must implement |

---

# 50. Important Python OOP Syntax

## Class

```python
class Student:
    pass
```

## Object

```python
student = Student()
```

## Method

```python
class Student:

    def display(self):
        print("Hello")
```

## Instance Attribute

```python
self.name = name
```

## Constructor / Initializer

```python
def __init__(self, name):
    self.name = name
```

## Inheritance

```python
class Dog(Animal):
    pass
```

## Parent Constructor

```python
super().__init__()
```

## Private Attribute

```python
self.__balance = balance
```

## Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

---

# 51. Common Interview Questions

## Q1. What is OOP?

**Answer:**

OOP is a programming paradigm that organizes software around objects and classes. It helps make code modular, reusable, maintainable, and easier to extend.

---

## Q2. What is a class?

**Answer:**

A class is a blueprint or template that defines the attributes and methods that objects created from it can have.

---

## Q3. What is an object?

**Answer:**

An object is an instance of a class. It contains actual data and can use the methods defined by its class.

---

## Q4. What is `self` in Python?

**Answer:**

`self` refers to the current object instance and is used to access that object's attributes and methods.

---

## Q5. What is `__init__()`?

**Answer:**

`__init__()` is a special initializer method that is automatically called when an object is created. It is commonly used to initialize instance attributes.

---

## Q6. What is inheritance?

**Answer:**

Inheritance allows a child class to acquire and reuse attributes and methods from a parent class. It helps reduce code duplication and supports code reuse.

---

## Q7. What is `super()`?

**Answer:**

`super()` is used to access methods of a parent class from a child class, commonly to call the parent's `__init__()` method.

---

## Q8. What is encapsulation?

**Answer:**

Encapsulation means bundling data and related methods inside a class while controlling access to the internal data.

---

## Q9. What is a private variable in Python?

**Answer:**

A variable beginning with double underscores, such as `__balance`, is treated as private by convention and Python applies name mangling to it.

---

## Q10. What are getters and setters?

**Answer:**

A getter retrieves a value, while a setter modifies a value. They can be used to provide controlled access to internal data.

---

## Q11. What is abstraction?

**Answer:**

Abstraction hides unnecessary implementation details and exposes only the essential functionality to the user.

---

## Q12. What is an abstract class?

**Answer:**

An abstract class is a class designed to act as a blueprint for subclasses. In Python, it can be created using `ABC` and can contain abstract methods.

---

## Q13. What is an abstract method?

**Answer:**

An abstract method is a method declared using `@abstractmethod` that must be implemented by a concrete subclass before it can normally be instantiated.

---

## Q14. What is polymorphism?

**Answer:**

Polymorphism allows the same interface or method name to have different implementations or behavior depending on the object.

---

## Q15. What are the four pillars of OOP?

**Answer:**

The four pillars are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

# 52. ⭐ Most Important Interview Points

Remember these points especially for fresher interviews:

### ⭐ 1. Class

A blueprint/template used to create objects.

### ⭐ 2. Object

An actual instance of a class.

### ⭐ 3. `self`

Refers to the current object.

### ⭐ 4. `__init__()`

Automatically runs when an object is initialized and is commonly used to initialize instance attributes.

### ⭐ 5. Inheritance

Allows a child class to reuse and extend a parent class.

### ⭐ 6. `super()`

Used to access parent-class functionality.

### ⭐ 7. Encapsulation

Controls access to internal data.

### ⭐ 8. Abstraction

Hides unnecessary implementation details.

### ⭐ 9. Polymorphism

Same interface/method can behave differently for different objects.

### ⭐ 10. Python Private Members

Double underscore (`__`) triggers name mangling; it is not absolute security.

### ⭐ 11. Type Annotations

Help communicate expected types but are not normally enforced by Python at runtime.

---

# 53. Quick Revision

```text
OOP
│
├── Class
│   └── Blueprint/template
│
├── Object
│   └── Instance of class
│
├── self
│   └── Current object
│
├── __init__()
│   └── Initializes object
│
└── Four Pillars
    │
    ├── Encapsulation
    │   └── Control access to data
    │
    ├── Inheritance
    │   └── Reuse parent functionality
    │
    ├── Polymorphism
    │   └── Same interface, different behavior
    │
    └── Abstraction
        └── Hide implementation details
```

---

# 54. One-Line Definitions for Fast Revision

**OOP:** Programming paradigm based on classes and objects.

**Class:** Blueprint for creating objects.

**Object:** Instance of a class.

**Attribute:** Data associated with an object/class.

**Method:** Function defined inside a class.

**`self`:** Reference to the current object.

**`__init__()`:** Initializer automatically called during object initialization.

**Inheritance:** Mechanism for reusing and extending another class.

**`super()`:** Accesses parent-class functionality.

**Encapsulation:** Bundling data and methods while controlling access.

**Abstraction:** Hiding unnecessary implementation details.

**Polymorphism:** Same interface with different behavior.

**Getter:** Reads/accesses a value.

**Setter:** Updates/modifies a value.

**Abstract Class:** Blueprint class that may contain abstract methods and cannot be instantiated while it remains abstract.

**Abstract Method:** Method that concrete subclasses are required to implement.

---

# 55. Final OOP Interview Summary

If an interviewer asks you to explain OOP, you can answer:

> **Object-Oriented Programming is a programming paradigm that organizes code around classes and objects. A class acts as a blueprint, while an object is an instance of that class. OOP improves code organization, reusability, maintainability, and extensibility. Its four main pillars are Encapsulation, Inheritance, Polymorphism, and Abstraction. In Python, `self` refers to the current object, `__init__()` initializes object state, inheritance allows classes to reuse functionality, encapsulation controls access to data, abstraction hides unnecessary implementation details, and polymorphism allows the same interface to behave differently for different objects.**

---

# ⭐ OOP Topics You Should Know for Interviews

For a fresher Python/backend interview, make sure you understand these properly:

- [ ] Class
- [ ] Object
- [ ] Attributes
- [ ] Methods
- [ ] `self`
- [ ] Instance variables
- [ ] `__init__()`
- [ ] Type annotations
- [ ] Inheritance
- [ ] Parent and child classes
- [ ] `super()`
- [ ] Method overriding
- [ ] Encapsulation
- [ ] Public / protected / private conventions
- [ ] Getters and setters
- [ ] Name mangling
- [ ] Abstraction
- [ ] ABC
- [ ] `@abstractmethod`
- [ ] Polymorphism
- [ ] Four pillars of OOP

## ⭐ Priority

**Very Important:**

Class → Object → `self` → `__init__()` → Inheritance → `super()` → Encapsulation → Abstraction → Polymorphism

These concepts form the core of Python OOP and are frequently discussed in fresher interviews.