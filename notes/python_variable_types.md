# Python Variable Types

## 1. Normal Variable (Local Variable)

A normal variable is a variable created inside a function or in the main program. A variable created inside a function is usually local to that function.

```python
def show():
    name = "Akash"  # Local variable
    print(name)

show()
```

**Output:**
```text
Akash
```

**Note:** A local variable created inside a function cannot normally be accessed outside that function.

## 2. Global Variable

A global variable is defined outside functions and can be accessed inside functions. Use the `global` keyword when you want to reassign a global variable inside a function.

```python
count = 10  # Global variable

def update():
    global count
    count = 20

update()
print(count)
```

**Output:**
```text
20
```

**Note:** Without `global`, assigning to `count` inside the function creates a local variable instead.

## 3. Special Variables

Special variables are often identified by double underscores at the beginning and end of their names, such as `__name__` and `__file__`. Python uses them for special purposes.

```python
print(__name__)
```

**Output when running this file directly:**
```text
__main__
```

**Note:** When a Python file is imported as a module, its `__name__` is usually the module's name instead of `"__main__"`.

## 4. Private Variable (Double Leading Underscore)

A variable beginning with two underscores, such as `__salary`, triggers *name mangling* inside a class. This helps avoid accidental name conflicts with subclasses, but it does not provide strict privacy.

```python
class Employee:
    def __init__(self):
        self.__salary = 50000

emp = Employee()
# print(emp.__salary)  # Raises AttributeError
print(emp._Employee__salary)
```

**Output:**
```text
50000
```

**Note:** Python changes the internal name to `_Employee__salary`. This is not a security feature.

## 5. Single Leading Underscore (`_variable`)

A variable beginning with one underscore indicates that it is intended for internal use. This is a naming convention, not a restriction enforced by Python.

```python
_age = 25

print(_age)
```

**Output:**
```text
25
```

**Note:** You can still access `_age` normally. In a `from module import *` statement, underscore-prefixed names are generally excluded unless the module defines `__all__`.

## 6. Double Leading Underscore (`__variable`)

A double leading underscore is mainly used inside classes to trigger name mangling. It is different from special names such as `__name__`, which have double underscores at both ends.

```python
class Student:
    def __init__(self):
        self.__marks = 90

s = Student()
print(s._Student__marks)
```

**Output:**
```text
90
```

**Note:** Use double leading underscores when you specifically need name mangling, not simply to indicate that a variable is private.

## Quick Comparison

| Variable type | Example | Meaning |
|---|---|---|
| Normal/local | `name` | A regular name; scope depends on where it is defined |
| Global | `count` | Defined outside a function; accessible within its scope |
| Special | `__name__` | Used by Python for a special purpose |
| Single underscore | `_age` | Conventionally intended for internal use |
| Double leading underscore | `__salary` | Triggers name mangling inside a class |
| Double underscores at both ends | `__init__` | Special method name defined by Python's data model |

## Important Points

- `name` has no special meaning by itself; its scope depends on where it is defined.
- `global` is a keyword used to reassign a global variable from inside a function.
- `_name` is a convention for internal use, not a private variable enforced by Python.
- `__name` inside a class triggers name mangling.
- `__name__` is a common pattern for special names, often called *dunder names*.
- Python does not provide strict private instance variables in the same way as some other programming languages.