# Abstraction in Python

## Abstraction

Abstraction means **hiding implementation details** and showing only the necessary features.

Example:
- We know a car has `start()`.
- We don't need to know exactly how the engine works internally.

Python provides abstraction using:
- `ABC`
- `abstractmethod`


---

# ABC (Abstract Base Class)

`ABC` is used to create an **abstract class**.

Import:

```python
from abc import ABC, abstractmethod
```

Example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

`Shape` is an **abstract class**.

It defines what methods the child class must implement.


---

# @abstractmethod

`@abstractmethod` makes a method an **abstract method**.

Example:

```python
@abstractmethod
def area(self):
    pass
```

The child class must provide its own implementation of this method.


---

# Implementing an Abstract Class

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


rect = Rectangle(3,4)

print(rect.area())
print(rect.perimeter())
```

Output:

```text
12
14
```


---

# Important Rule

If a child class does **not implement all abstract methods**, we cannot create its object.

Example:

```python
class Rectangle(Shape):

    def area(self):
        return 12
```

Here `perimeter()` is not implemented.

Therefore:

```python
rect = Rectangle()
```

will give an error because `Rectangle` is still abstract.


---

# Abstract Class vs Normal Class

| Abstract Class | Normal Class |
|---|---|
| Inherits from `ABC` | No need to inherit `ABC` |
| Can contain abstract methods | Usually contains normal methods |
| Cannot directly create its object | Can create its object |
| Child must implement abstract methods | No such requirement |


---

# Important Points

- Abstraction hides implementation details.
- `ABC` is used to create an abstract base class.
- `@abstractmethod` defines a method that child classes must implement.
- Abstract classes cannot be instantiated directly.
- Child classes must implement all abstract methods.
- Abstraction helps create a common structure for different classes.