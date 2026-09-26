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


# Python Dunder Methods (Magic Methods)

## Dunder Methods

Dunder methods are special methods in Python that start and end with double underscores.

Example:

```python
__init__()
__str__()
__add__()
__eq__()
```

They allow objects to work with built-in Python operations like:
- `print()`
- `+`
- `-`
- `len()`
- comparison operators


---

# __str__() Method

`__str__()` defines how an object should be represented as a string.

It is automatically called when we use:

```python
print(object)
```


## Without __str__()

Example:

```python
class New:

    def __init__(self,x,y):
        self.x=x
        self.y=y


q = New(3,4)

print(q)
```

Output:

```
<__main__.New object at 0x...>
```

Python prints the default object location.


---

## Using __str__()

Example:

```python
class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y


    def __str__(self):
        return f"Point({self.x},{self.y})"


p = Point(3,4)

print(p)
```

Output:

```
Point(3,4)
```

### Note:
`__str__()` gives a readable representation of an object.


---

# __add__() Method

`__add__()` is used to customize the `+` operator.

Example:

```python
class Distance:

    def __init__(self,km):
        self.km = km


    def __add__(self,other):
        return self.km + other.km


d1 = Distance(10)
d2 = Distance(20)

print(d1 + d2)
```

Output:

```
30
```

Python internally calls:

```python
d1.__add__(d2)
```


---

# __len__() Method

`__len__()` defines the behavior of the `len()` function.

Example:

```python
class Playlist:

    def __init__(self):
        self.song=[]


    def add(self,song):
        self.song.append(song)


    def __len__(self):
        return len(self.song)



p = Playlist()

p.add("Song A")
p.add("Song B")
p.add("Song C")


print(len(p))
```

Output:

```
3
```

Python internally calls:

```python
p.__len__()
```


---

# Comparison Dunder Methods

Used to customize comparison operators.


| Operator | Dunder Method |
|---|---|
| `==` | `__eq__()` |
| `<` | `__lt__()` |
| `<=` | `__le__()` |
| `>` | `__gt__()` |
| `>=` | `__ge__()` |


---

# __eq__() Method

Used for comparing objects.

Example:

```python
class Money:

    def __init__(self,amount):
        self.amount = amount


    def __eq__(self,other):
        return self.amount == other.amount



a = Money(80)
b = Money(80)


print(a == b)
```

Output:

```
True
```


Without `__eq__()` Python compares object memory location.


---

# __lt__() and __le__()

## __lt__()

Used for:

```python
<
```

Example:

```python
def __lt__(self,other):
    return self.amount < other.amount
```


## __le__()

Used for:

```python
<=
```

Example:

```python
def __le__(self,other):
    return self.amount <= other.amount
```


---

# Creating New Objects in Dunder Methods

Dunder methods can return a new object.

Example:

```python
class Distance:

    def __init__(self,km):
        self.km = km


    def __sub__(self,other):
        return Distance(self.km - other.km)


    def __str__(self):
        return f"{self.km} km"



d1 = Distance(100)
d2 = Distance(40)


new_distance = d1 - d2

print(new_distance)
```

Output:

```
60 km
```


Here:

```python
return Distance(...)
```

creates a new object.


---

# Important Points

- Dunder methods customize object behavior.
- `__str__()` controls print output.
- `__add__()` controls `+` operator.
- `__len__()` controls `len()`.
- `__eq__()` controls `==`.
- Comparison operators use dunder methods.
- Dunder methods are also called **Magic Methods**.
- They support polymorphism by allowing different objects to behave differently with the same operation.>