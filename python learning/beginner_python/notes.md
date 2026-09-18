# Python Basics Notes

## 1. Variables & Data Types

### Variables
A variable stores data in memory.

```python
name = "Ahad"
age = 19
```

### Variable Naming Rules
- Can contain letters, numbers, and `_`
- Cannot start with a number
- Cannot use Python keywords (`if`, `for`, `class`)

Example:
```python
user_name = "Alex"
```

### Common Data Types

| Data Type | Example | Use |
|---|---|---|
| int | 10 | Whole numbers |
| float | 10.5 | Decimal numbers |
| str | "Python" | Text |
| bool | True | True/False |
| list | [1,2,3] | Collection |
| tuple | (1,2,3) | Immutable collection |
| dict | {"a":1} | Key-value data |
| set | {1,2,3} | Unique values |

### print()

Used to display output.

```python
print("Hello World")
```

---

# 2. Core Concepts

## Type Conversion

Changing one data type into another.

```python
x = "10"
y = int(x)

print(y + 5)
```

Common conversions:

```python
int()
float()
str()
bool()
list()
```

---

## Escape Sequences

Special characters inside strings.

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

Common Escape Characters:

- `\n` → New line
- `\t` → Tab
- `\"` → Double quote

---

## Operators

### Arithmetic Operators

```
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
//  Floor Division
**  Power
```

Example:

```python
10 % 3   # Output: 1
2 ** 3   # Output: 8
```

### Comparison Operators

```
>   Greater than
<   Less than
>=  Greater or equal
<=  Less or equal
==  Equal
!=  Not equal
```

### Logical Operators

```
and
or
not
```

Example:

```python
age > 18 and age < 30
```

---

# Flow Control

# 3. if-else Statement

Used for decision making.

Syntax:

```python
if condition:
    code
else:
    code
```

Example:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Child")
```

---

# 4. Loops

## while Loop

Runs until condition becomes false.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## for Loop

Used to iterate over sequence.

```python
for i in range(5):
    print(i)
```

Output:

```
0 1 2 3 4
```

---

## break

Stops the loop completely.

```python
for i in range(10):
    if i == 5:
        break
```

---

## continue

Skips current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## Pattern Problems

Used to improve loop logic.

Example:

```
*
**
***
```

Logic:
- Outer loop → Rows
- Inner loop → Columns

---

# Functions

## Creating Function

Reusable block of code.

```python
def greet():
    print("Hello")

greet()
```

---

## Parameters

Input variables defined during function creation.

```python
def add(a,b):
    return a+b
```

---

## Arguments

Actual values passed to function.

```python
add(5,10)
```

---

## return Statement

Returns value from function.

```python
def square(x):
    return x*x
```

---

## Local Variable

Variable created inside function.

```python
def fun():
    x = 10
```

Only available inside function.

---

## Global Variable

Variable created outside function.

```python
x = 20
```

Available throughout program.

---

## Lambda Function

Small anonymous function.

```python
add = lambda a,b: a+b
```

---

# Data Structures

# Lists

Ordered and changeable collection.

```python
nums = [1,2,3]
```

## Indexing

```python
nums[0]
```

Output:

```
1
```

---

## Slicing

```python
nums[1:3]
```

Output:

```
[2,3]
```

---

## List Methods

```python
append()   # Add item
remove()   # Remove item
pop()      # Remove by index
sort()     # Sort list
reverse()  # Reverse list
```

---

## List Comprehension

Short way to create lists.

```python
nums = [i for i in range(5)]
```

Output:

```
[0,1,2,3,4]
```

---

## Nested List

List inside another list.

```python
matrix = [
[1,2],
[3,4]
]
```

---

# Tuples

Ordered but immutable collection.

```python
t = (1,2,3)
```

Cannot be modified.

---

## Tuple Packing

```python
data = 1,2,3
```

## Tuple Unpacking

```python
a,b,c = data
```

---

# Dictionary

Stores data in key-value pairs.

```python
student = {
"name":"Ahad",
"age":19
}
```

Access:

```python
student["name"]
```

---

## Dictionary Methods

```python
keys()
values()
items()
update()
```

---

## Loop Dictionary

```python
for key,value in student.items():
    print(key,value)
```

---

## Dictionary Comprehension

```python
square = {
x:x*x for x in range(5)
}
```

---

# Sets

Collection of unique values.

```python
s = {1,2,3}
```

Duplicates are removed.

Example:

```python
{1,1,2}
```

Output:

```
{1,2}
```

Methods:

```python
add()
remove()
union()
intersection()
difference()
```

---

# Strings

Sequence of characters.

```python
name = "Python"
```

---

## Indexing

```python
name[0]
```

Output:

```
P
```

---

## Slicing

```python
name[0:3]
```

Output:

```
Pyt
```

---

## String Methods

### Case Conversion

```python
upper()
lower()
title()
```

Example:

```python
"python".upper()
```

Output:

```
PYTHON
```

---

## Checking Content

```python
startswith()
endswith()
isdigit()
isalpha()
```

---

## split()

String to List.

```python
"a b c".split()
```

Output:

```
['a','b','c']
```

---

## join()

List to String.

```python
"-".join(["a","b"])
```

Output:

```
a-b
```

---

## strip()

Removes extra spaces.

```python
" hello ".strip()
```

Output:

```
hello
```

---

# Python Learning Roadmap

Basics  
↓  
Conditions  
↓  
Loops  
↓  
Functions  
↓  
Lists  
↓  
Dictionary  
↓  
Sets  
↓  
Strings  
↓  
OOP  
↓  
Modules  
↓  
APIs  
↓  
FastAPI