# Python String Methods

## Introduction

Python provides built-in methods to work with strings. You can use them to change letter case, search for text, replace characters, split strings, and validate string content.

**Important:** Python strings are immutable, which means string methods do not change the original string. Methods that modify text return a new string.

```python
text = "hello world"

result = text.upper()

print(result)  # HELLO WORLD
print(text)    # hello world
```

## Table of Contents

1. [capitalize()](#1-capitalize)
2. [casefold()](#2-casefold)
3. [center()](#3-center)
4. [count()](#4-count)
5. [endswith()](#5-endswith)
6. [find()](#6-find)
7. [format()](#7-format)
8. [index()](#8-index)
9. [isalnum()](#9-isalnum)
10. [isalpha()](#10-isalpha)
11. [isdecimal()](#11-isdecimal)
12. [isdigit()](#12-isdigit)
13. [islower()](#13-islower)
14. [isnumeric()](#14-isnumeric)
15. [join()](#15-join)
16. [lower()](#16-lower)
17. [partition()](#17-partition)
18. [replace()](#18-replace)
19. [split()](#19-split)
20. [rsplit()](#20-rsplit)
21. [lsplit() clarification](#21-lsplit-clarification)
22. [splitlines()](#22-splitlines)
23. [startswith()](#23-startswith)
24. [strip()](#24-strip)
25. [title()](#25-title)
26. [upper()](#26-upper)
27. [Other Useful String Methods](#other-useful-string-methods)

---

## 1. capitalize()

**Purpose:** Converts the first character to uppercase and the remaining characters to lowercase.

```python
text = "hello WORLD"
print(text.capitalize())

# Output:
# Hello world
```

## 2. casefold()

**Purpose:** Converts a string to lowercase in a way suitable for case-insensitive comparisons. It handles some Unicode characters more thoroughly than `lower()`.

```python
text = "HELLO"
print(text.casefold())

# Output:
# hello
```

## 3. center()

**Purpose:** Places a string in the center of a specified width, padding it with spaces or a character.

```python
text = "Python"
print(text.center(12, "-"))

# Output:
# ---Python---
```

## 4. count()

**Purpose:** Counts how many times a substring appears in a string.

```python
text = "banana"
print(text.count("a"))

# Output:
# 3
```

You can also specify the start and end positions.

```python
text = "banana"
print(text.count("a", 2, 5))

# Output:
# 2
```

## 5. endswith()

**Purpose:** Checks whether a string ends with the specified text. Returns `True` or `False`.

```python
filename = "notes.md"
print(filename.endswith(".md"))

# Output:
# True
```

## 6. find()

**Purpose:** Returns the index of the first occurrence of a substring. Returns `-1` if the substring is not found.

```python
text = "Hello Python"
print(text.find("Python"))
print(text.find("Java"))

# Output:
# 6
# -1
```

## 7. format()

**Purpose:** Inserts values into placeholders inside a string.

```python
name = "Amit"
age = 25

text = "My name is {} and I am {} years old."
print(text.format(name, age))

# Output:
# My name is Amit and I am 25 years old.
```

You can also use named placeholders.

```python
text = "Name: {name}, Age: {age}"
print(text.format(name="Amit", age=25))

# Output:
# Name: Amit, Age: 25
```

## 8. index()

**Purpose:** Returns the index of the first occurrence of a substring. Unlike `find()`, it raises a `ValueError` if the substring is not found.

```python
text = "Hello Python"
print(text.index("Python"))

# Output:
# 6
```

Example when the substring is missing:

```python
text = "Hello Python"
print(text.index("Java"))

# Output:
# ValueError
```

**Remember:** Use `find()` if you want `-1` when text is missing. Use `index()` if you want an error when it is missing.

## 9. isalnum()

**Purpose:** Checks whether every character is a letter or a number. The string must not be empty.

```python
print("Python123".isalnum())
print("Python 123".isalnum())

# Output:
# True
# False
```

The second result is `False` because the string contains a space.

## 10. isalpha()

**Purpose:** Checks whether all characters are alphabetic letters. The string must not be empty.

```python
print("Python".isalpha())
print("Python123".isalpha())

# Output:
# True
# False
```

## 11. isdecimal()

**Purpose:** Checks whether all characters are decimal digits, such as `0` through `9` and their Unicode decimal-digit equivalents.

```python
print("12345".isdecimal())
print("12.5".isdecimal())

# Output:
# True
# False
```

A decimal point makes `"12.5"` return `False`.

## 12. isdigit()

**Purpose:** Checks whether all characters are digits. It accepts some additional digit characters that `