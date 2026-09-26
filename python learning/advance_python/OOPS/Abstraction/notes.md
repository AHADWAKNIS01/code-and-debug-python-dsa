# Polymorphism in Python

## Polymorphism

Polymorphism means **"many forms"**.

It allows the same method name to perform different tasks depending on the object.

Example:
- Rectangle area → width × height
- Circle area → π × radius²


---

# Method Overriding (Runtime Polymorphism)

When a child class provides its own implementation of a parent class method, it is called **method overriding**.

Example:

```python
class Shape:

    def area(self):
        return 0


class Rectangle(Shape):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


shapes = [
    Rectangle(3,4),
    Circle(3)
]


for s in shapes:
    print(s.area())
```

Output:

```
12
28.26
```


---

# How Polymorphism Works

Here:

```python
s.area()
```

The same method call gives different results.

### Rectangle Object:
```python
Rectangle(3,4)
```

Runs:

```python
return self.w * self.h
```


### Circle Object:
```python
Circle(3)
```

Runs:

```python
return 3.14 * self.r ** 2
```


---

# Important Points

- Polymorphism allows one interface with multiple implementations.
- Child classes override parent methods.
- The same method name behaves differently for different objects.
- Commonly used with inheritance.
- Makes code flexible and reusable.


---

# Method Overloading in Python

Python does not support traditional method overloading.

Example:

```python
def area(self,w,h):
    pass

def area(self):
    pass
```

The second method replaces the first one.

Use:
- Default arguments
- `*args`

instead of method overloading.