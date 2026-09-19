# Advanced Python Notes

# 1. Python Memory Management

## Shallow Copy vs Deep Copy

### Shallow Copy
Creates a new object but keeps references to nested objects.

Changes in nested objects affect both copies.

Example:

```python
import copy
a = [54, 5, 6, [7, 8, 9], 56, 7, 8]
b = copy.copy(a)

b[3][0] = 100

print(a)
# [54, 5, 6, [100, 8, 9], 56, 7, 8]

print(b)
# [54, 5, 6, [100, 8, 9], 56, 7, 8]
```

Output:

```
 [54, 5, 6, [100, 8, 9], 56, 7, 8]
 [54, 5, 6, [100, 8, 9], 56, 7, 8]
```

---

### Deep Copy

Creates a completely independent copy including nested objects.

Changes in one object do not affect another.

Example:

```python
import copy
a = [54, 5, 6, [7, 8, 9], 56, 7, 8]
b = copy.deepcopy(a)

b[3][0] = 100

print(a)
# [54, 5, 6, [7, 8, 9], 56, 7, 8]

print(b)
# [54, 5, 6, [100, 8, 9], 56, 7, 8]
```

Output:

```
 [54, 5, 6, [7, 8, 9], 56, 7, 8]
 [54, 5, 6, [100, 8, 9], 56, 7, 8]
```

---

## Pass by Reference vs Pass by Value

Python uses **Pass by Object Reference**.

The function receives a reference to the same object.

### Mutable Objects
(list, dictionary, set)

Changes affect original object.

Example:

```python
def change(lst):
    lst.append(4)

nums=[1,2,3]

change(nums)

print(nums)
```

Output:

```
[1,2,3,4]
```

---

### Immutable Objects
(int, string, tuple)

Changes create a new object.

Example:

```python
def change(x):
    x = x + 5

a = 10

change(a)

print(a)
```

Output:

```
10
```

---

# 2. Professional Code Practices

# Type Annotations (Type Hints)

Used to specify expected data types.

Improves:
- Code readability
- Error detection
- Maintenance

Example:

Without type hint:

```python
def add(a,b):
    return a+b
```

With type hint:

```python
def add(a:int, b:int) -> int:
    return a+b
```

Explanation:

```
a:int → input should be integer
-> int → function returns integer
```

---
# Mutating vs Rebinding in Python

## 1. Mutating

**Mutating = changing the existing object.**

Example:

```python
nums = [1, 2, 3]

nums.append(4)
```

Before:
```text
[1, 2, 3]
```

After:
```text
[1, 2, 3, 4]
```

The **same list object** is changed.

### Common Mutating Operations

```python
list.append()
list.remove()
list.sort()

dict.update()

set.add()
```

---

## 2. Rebinding

**Rebinding = making a variable point to a different object.**

Example:

```python
x = 10

x = 20
```

`x` first points to `10`, then points to `20`.

The original object is **not changed**.

Another example:

```python
nums = [1, 2, 3]

nums = [4, 5, 6]
```

Here, `nums` now points to a **new list**.

---

# Mutating vs Rebinding

### Mutating

```python
nums = [1, 2, 3]

nums.append(4)
```

➡️ Same object is changed.

### Rebinding

```python
nums = [1, 2, 3]

nums = [4, 5, 6]
```

➡️ Variable points to a new object.

---

# Function Example

```python
def change(nums):
    nums.append(4)       # Mutating
    nums = [10, 20, 30]  # Rebinding

numbers = [1, 2, 3]

change(numbers)

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

### Why?

- `nums.append(4)` → changes the original list.
- `nums = [10,20,30]` → rebinds only the local `nums`.
- `numbers` still points to the original list.

---

## Easy Rule

**Mutating → changes the object.**

**Rebinding → changes what the variable points to.**

---

# 3. Object-Oriented Programming (OOP)

OOP is a programming approach based on objects.

Main concepts:

- Class
- Object
- Encapsulation
- Inheritance
- Abstraction
- Polymorphism

---

# Classes and Objects

## Class

Blueprint for creating objects.

Example:

```python
class Student:
    pass
```

---

## Object

Instance of a class.

Example:

```python
student1 = Student()
```

---

# __init__ Constructor

Automatically runs when object is created.

Used to initialize object values.

Example:

```python
class Student:

    def __init__(self,name):
        self.name = name


s1 = Student("Ahad")

print(s1.name)
```

Output:

```
Ahad
```

---

# Student Class Example

```python
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name,self.marks)


s1 = Student("Ahad",90)

s1.display()
```

---

# Instance vs Class Variables

## Instance Variable

Different value for every object.

Example:

```python
class Student:

    def __init__(self,name):
        self.name = name
```

Each object has its own name.

---

## Class Variable

Common value shared by all objects.

Example:

```python
class Student:

    school = "Rizvi"

    def __init__(self,name):
        self.name = name
```

---

# Encapsulation

Wrapping data and methods together.

Used for data hiding.

Example:

```python
class Bank:

    def __init__(self):
        self.__balance = 1000
```

`__balance` is private.

Access using methods:

```python
def get_balance(self):
    return self.__balance
```

---

# Inheritance

One class uses properties of another class.

Example:

```python
class Animal:

    def sound(self):
        print("Sound")


class Dog(Animal):
    pass


d = Dog()

d.sound()
```

---

## Types of Inheritance

1. Single Inheritance

```
A → B
```

2. Multiple Inheritance

```
A + B → C
```

3. Multilevel Inheritance

```
A → B → C
```

4. Hierarchical Inheritance

```
   A
 /   \
B     C
```

---

# Dunder (Magic) Methods

Special methods with double underscore.

Examples:

```python
__init__()
__str__()
__len__()
__add__()
```

---

## __str__()

Controls object printing.

Example:

```python
class Student:

    def __str__(self):
        return "Student Object"
```

---

# Abstraction

Hiding internal implementation details.

Only showing required information.

Example:

ATM:

User knows:
- Withdraw money
- Check balance

User does not know:
- Internal banking process

Python uses:

```python
from abc import ABC, abstractmethod
```

---

# 4. Error & Resource Management

# Exception Handling

Used to handle runtime errors.

Syntax:

```python
try:
    code

except:
    handle error
```

Example:

```python
try:
    x = 10/0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## finally

Always executes.

Example:

```python
try:
    file=open("data.txt")

finally:
    file.close()
```

---

# File Handling

Used to read and write files.

## Opening File

```python
file=open("data.txt","r")
```

Modes:

```
r → read
w → write
a → append
```

---

## Reading File

```python
file=open("data.txt","r")

content=file.read()

print(content)
```

---

## Writing File

```python
file=open("data.txt","w")

file.write("Hello Python")

file.close()
```

---

## Best Practice (with)

Automatically closes file.

```python
with open("data.txt","r") as file:
    data=file.read()
```

---

# 5. Architecture & Concurrency

# Modules

A module is a Python file containing functions/classes.

Example:

math.py

```python
def add(a,b):
    return a+b
```

Use:

```python
import math
```

---

# Packages

Collection of multiple modules.

Example:

```
project/

    package/

        module1.py
        module2.py
```

Used for organizing large projects.

---

# Multithreading vs Multiprocessing

## Multithreading

Multiple threads inside one process.

Best for:

- I/O tasks
- API calls
- File operations

Example:

```python
import threading

threading.Thread(target=task)
```

---

## Multiprocessing

Uses multiple CPU processes.

Best for:

- Heavy calculations
- Machine learning
- Data processing

Example:

```python
from multiprocessing import Process

Process(target=task)
```

---

# Difference

| Multithreading | Multiprocessing |
|---|---|
| Uses threads | Uses processes |
| Same memory | Separate memory |
| Good for I/O | Good for CPU |
| Faster creation | More resource usage |

---

# Python Advanced Learning Flow

Memory Management  
↓  
Type Hints  
↓  
OOP  
↓  
Exception Handling  
↓  
File Handling  
↓  
Modules & Packages  
↓  
Multithreading  
↓  
Multiprocessing  
↓  
FastAPI / Backend Development