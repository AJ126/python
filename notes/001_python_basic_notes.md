# Python Basics — Study Notes

> Beginner-friendly notes covering identifiers, reserved words, built-in data types, escape characters, identity operators, and membership operators.

## Table of Contents

1. [Python](#python)
2. [Identifiers](#identifiers)
3. [Reserved Words (Keywords)](#reserved-words-keywords)
4. [Built-in Data Types](#built-in-data-types)
5. [Escape Characters](#escape-characters)
6. [Identity Operators](#identity-operators)
7. [Membership Operators](#membership-operators)
8. [Quick Revision](#quick-revision)

---

## Python

- In Python, **everything is an object**. Numbers, strings, lists, functions, and many other values are objects.
- Use `type()` to check an object's type.
- Use `id()` to get an object's identity value. It is **not guaranteed to be a physical memory address**.

```python
number = 10
name = "Python"

print(type(number))  # <class 'int'>
print(type(name))    # <class 'str'>
print(id(number))    # An identity value for this object
```

---

## Identifiers

An **identifier** is a name used in a Python program. Identifiers can name variables, functions, classes, modules, and more.

### Rules for identifiers

- Allowed characters are letters (`A–Z`, `a–z`), digits (`0–9`), and underscores (`_`).
- An identifier **cannot start with a digit**.
- Identifiers are case-sensitive: `total` and `TOTAL` are different names.
- Spaces and symbols such as `$` are not allowed in identifiers.
- Python identifiers can be long, but short, meaningful names are usually easier to read.
- A single leading underscore, such as `_name`, is a **convention** indicating that a name is intended for internal use. It does not make the name truly private.
- A double leading underscore in a class, such as `__name`, can trigger *name mangling*. It is not a universal privacy mechanism.
- Names that begin and end with double underscores, such as `__init__`, are commonly reserved for special Python methods and attributes. Avoid inventing such names for ordinary variables.

### Valid and invalid identifiers

| Identifier | Valid? | Reason |
|---|---|---|
| `123total` | ❌ No | Starts with a digit |
| `total123` | ✅ Yes | Letters followed by digits |
| `java2share` | ✅ Yes | Letters and digits |
| `ca$h` | ❌ No | `$` is not allowed |
| `_abc_abc_` | ✅ Yes | Underscores and letters are allowed |
| `def` | ❌ No | `def` is a Python keyword |
| `if` | ❌ No | `if` is a Python keyword |
| `total` | ✅ Yes | Valid name |
| `TOTAL` | ✅ Yes | Valid and different from `total` |

```python
total = 10
TOTAL = 999

print(total)  # 10
print(TOTAL)  # 999
```

**Tip:** Prefer descriptive names such as `student_name` and `total_marks` instead of unclear names such as `x1` or excessively long names.

---

## Reserved Words (Keywords)

**Keywords** are words that have special meaning in Python syntax. They cannot be used as ordinary identifiers.

The exact keyword list can vary by Python version. To see the keywords in your installed version:

```python
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
```

Common Python keywords include:

```text
False  None  True
and  or  not  is
if  elif  else
for  while  break  continue  pass
try  except  finally  raise  assert
import  from  as
class  def  return  yield  lambda
global  nonlocal  del  with
in
```

> **Note:** `match` and `case` are soft keywords in modern Python: they have special meaning in pattern-matching contexts but can be used as identifiers in some other contexts. Do not rely on an old fixed count of Python keywords.

---

## Built-in Data Types

Python includes several built-in data types.

| Type | What it represents | Example |
|---|---|---|
| `int` | Integers (whole numbers) | `10`, `-5` |
| `float` | Floating-point numbers | `10.5`, `-0.25` |
| `complex` | Complex numbers | `2 + 3j` |
| `bool` | Truth values | `True`, `False` |
| `str` | Text | `"Python"` |
| `bytes` | Immutable sequence of bytes | `bytes([10, 20, 30])` |
| `bytearray` | Mutable sequence of bytes | `bytearray([10, 20, 30])` |
| `range` | Sequence-like range of integers | `range(5)` |
| `list` | Ordered, mutable collection | `[10, 20, 10]` |
| `tuple` | Ordered, immutable collection | `(10, 20, 30)` |
| `set` | Mutable collection of unique elements | `{10, 20, 30}` |
| `frozenset` | Immutable set | `frozenset([10, 20])` |
| `dict` | Key-value mapping | `{"id": 101, "name": "Durga"}` |
| `NoneType` | The type of `None` | `None` |

Check types with `type()`:

```python
value = 10
print(type(value))  # <class 'int'>
```

### 1. `int`

Represents integers (whole numbers).

```python
age = 25
temperature = -3

print(type(age))  # <class 'int'>
```

### 2. `float`

Represents floating-point numbers.

```python
price = 99.50
height = 1.75

print(type(price))  # <class 'float'>
```

### 3. `complex`

Represents complex numbers. In Python, `j` denotes the imaginary part.

```python
number = 2 + 3j

print(number.real)  # 2.0
print(number.imag)  # 3.0
```

### 4. `bool`

Represents either `True` or `False`.

```python
is_logged_in = True
print(type(is_logged_in))  # <class 'bool'>
```

### 5. `str` (String)

A string is a sequence of characters enclosed in single or double quotes. Triple quotes can represent multi-line strings.

```python
first_name = 'Shiv'
language = "Python"

message = '''This is
a multi-line
string.'''

print(first_name)
print(message)
```

#### String indexing and slicing

Python strings use **zero-based indexing**. Positive indexes count from left to right; negative indexes count from right to left.

For `"shiv"`:

| Character | `s` | `h` | `i` | `v` |
|---|---:|---:|---:|---:|
| Positive index | `0` | `1` | `2` | `3` |
| Negative index | `-4` | `-3` | `-2` | `-1` |

```python
word = "shiv"

print(word[0])    # s
print(word[-1])   # v
print(word[1:3])  # hi
```

The slice `word[start:stop]` includes `start` but **does not include** `stop`.

Strings are immutable, which means their individual characters cannot be changed in place.

### 6. `bytes`

`bytes` represents an immutable sequence of integers from `0` to `255`. It is useful for binary data, such as file contents or network data.

```python
values = [10, 20, 30, 40]
data = bytes(values)

print(data[0])  # 10
# data[0] = 100  # TypeError: bytes objects are immutable
```

### 7. `bytearray`

`bytearray` is similar to `bytes`, but its elements can be modified. Each element must remain in the range `0` to `255`.

```python
values = [10, 20, 30, 40]
data = bytearray(values)

data[0] = 100
print(data[0])  # 100
```

### 8. `list`

A list stores multiple values in one collection.

**Key features:**

1. Preserves insertion order.
2. Allows duplicate values.
3. Allows values of different types (heterogeneous values).
4. Is mutable: elements can be changed.
5. Can grow or shrink.
6. Uses square brackets `[]`.
7. Can contain another list (a nested list).

```python
items = [10, 10.5, "Durga", True, 10]
nested = [10, 20, [30, 40]]

print(items[0])    # 10
print(items[1:3])  # [10.5, 'Durga']
print(nested[2])   # [30, 40]

items[0] = 99
items.append("Python")
print(items)
```

Lists use zero-based positive and negative indexes, just like strings.

### 9. `tuple`

A tuple is an ordered collection like a list, but it cannot be reassigned element by element after creation (it is immutable).

- Uses parentheses in common notation: `()`.
- Allows duplicate values and mixed types.
- Useful when a collection should not be changed.

```python
values = (10, 20, 30, 40)

print(values[0])  # 10
# values[0] = 99  # TypeError
```

A one-element tuple needs a comma: `single = (10,)`.

### 10. `range`

`range` represents an immutable sequence of integers, often used with loops. The stop value is excluded.

```python
print(list(range(10)))         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10, 20)))     # 10 through 19
print(list(range(10, 20, 2)))  # [10, 12, 14, 16, 18]
```

General form: `range(start, stop, step)`. The `start` and `step` arguments are optional; by default, `start` is `0` and `step` is `1`.

### 11. `set`

A set is a mutable collection of **unique** hashable elements.

**Key features:**

- Duplicate elements are removed.
- Sets do not support indexing or slicing.
- Sets are mutable; elements can be added or removed.
- Do not rely on a set's display order.
- Uses braces `{}` for a non-empty set.

```python
values = {100, 0, 10, 200, 10, "Durga"}
print(values)  # Contains each unique value once

values.add(50)
values.discard(100)
print(values)

empty_set = set()  # {} creates an empty dictionary, not an empty set
```

### 12. `frozenset`

A `frozenset` is an immutable set. Its elements cannot be added or removed after creation.

```python
values = frozenset([10, 20, 30, 20])
print(values)

# values.add(40)  # AttributeError: no add() method
```

### 13. `dict` (Dictionary)

A dictionary stores data as **key-value pairs**.

- Keys must be unique and hashable.
- Values may be duplicated.
- If a key is assigned again, its value is replaced.
- Dictionaries are mutable.
- Dictionaries preserve insertion order in modern Python (guaranteed in Python 3.7 and later).

```python
students = {
    101: "Durga",
    102: "Ravi",
    103: "Shiva",
}

print(students[101])  # Durga

students[102] = "Ravi Kumar"  # Update an existing key
students[104] = "Meera"       # Add a new key
print(students)
```

Example of a repeated key:

```python
data = {"name": "Ravi", "name": "Shiva"}
print(data)  # {'name': 'Shiva'}
```

### 14. `None`

`None` represents the absence of a value. Its type is `NoneType`.

```python
result = None

print(result)        # None
print(type(result))  # <class 'NoneType'>
```

Use `is None` to check for it:

```python
if result is None:
    print("No result is available")
```

---

## Escape Characters

Escape sequences begin with a backslash (`\`) and represent special characters inside strings.

| Escape sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Horizontal tab |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\f` | Form feed |
| `\v` | Vertical tab |
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | A literal backslash |

Example:

```python
print("Hello\nPython")
# Hello
# Python

print("Name:\tShiv")
# Name:   Shiv

print('It\'s Python')
print("A backslash: \\")
```

**Tip:** Raw strings (such as `r"C:\new\test"`) are useful for many Windows paths because backslashes are treated literally, with some limitations.

---

## Identity Operators

Python has two identity operators:

- `is`
- `is not`

They check whether two references point to the **same object**, not whether their values are equal.

```python
a = [10, 20]
b = a
c = [10, 20]

print(a is b)      # True: both refer to the same list object
print(a is c)      # False: these are separate list objects
print(a == c)      # True: their contents are equal
print(a is not c)  # True
```

### `is` versus `==`

- `==` compares values for equality.
- `is` compares object identity.

For ordinary value comparisons, use `==`. Use identity checks when identity matters, especially `value is None`.

Avoid relying on examples such as `a = 10; b = 10; a is b` to demonstrate identity: Python may reuse some immutable objects, so the result can depend on implementation details.

---

## Membership Operators

Membership operators check whether an item is present in a collection or sequence.

- `in` returns `True` when a match is found.
- `not in` returns `True` when a match is not found.

They can be used with strings, lists, tuples, sets, ranges, and dictionaries. For dictionaries, membership tests **keys**, not values.

```python
numbers = [10, 20, 30]

print(20 in numbers)      # True
print(50 not in numbers)  # True

word = "Python"
print("Py" in word)       # True
print("py" in word)       # False: string matching is case-sensitive

student = {101: "Durga", 102: "Ravi"}
print(101 in student)             # True: checks keys
print("Durga" in student)         # False: checks keys, not values
print("Durga" in student.values())  # True: checks values
```

---

## Quick Revision

| Concept | Remember |
|---|---|
| Identifier | A valid name for a variable, function, class, etc. |
| Keyword | A reserved word with special meaning in Python syntax |
| `type(x)` | Returns the type of `x` |
| `id(x)` | Returns an identity value for the object |
| Mutable examples | `list`, `dict`, `set`, `bytearray` |
| Immutable examples | `int`, `float`, `bool`, `str`, `bytes`, `tuple`, `range`, `frozenset` |
| `==` | Value equality |
| `is` | Object identity |
| `in` / `not in` | Membership test |
| `None` | Represents absence of a value |

## Practice Questions

1. Which of these are valid identifiers: `student1`, `1student`, `_total`, `class`?
2. What is printed by `print("Python"[-1])`?
3. What is the main difference between a list and a tuple?
4. Which collection removes duplicate elements?
5. What is the difference between `==` and `is`?
6. What does `20 in [10, 20, 30]` return?
7. How do you create an empty set?
8. What does `None` represent?

### Answers

1. `student1` and `_total` are valid; `1student` starts with a digit and `class` is a keyword.
2. `n`
3. A list is mutable; a tuple is immutable.
4. A set (and a `frozenset`) stores unique elements.
5. `==` compares values; `is` checks whether both references point to the same object.
6. `True`
7. `set()`
8. The absence of a value.
