
# Python Packages

## 1. What Is a Package?

A package is a way to organize related Python modules into a single directory structure.

A **module** is usually a Python `.py` file, whereas a **package** is a directory that groups modules and may contain other packages.

### Advantages of Packages

1. Organize large Python projects.
2. Group related modules together.
3. Reuse code across different programs.
4. Separate functionality into smaller, manageable units.
5. Create subpackages to organize complex projects.

---

## 2. Package Structure

Traditionally, a regular Python package contains an `__init__.py` file. This file can be empty or contain initialization code.

### Example

```text
project/
├── main.py
└── akashPackage/
    ├── __init__.py
    ├── AkashModule.py
    └── ajpackage/
        ├── __init__.py
        └── ajmodule.py
```

### Explanation

- `akashPackage/` is the main package.
- `__init__.py` marks a regular package and can contain initialization code.
- `AkashModule.py` is a module inside `akashPackage`.
- `ajpackage/` is a subpackage.
- `ajmodule.py` is a module inside the subpackage.

**Important:** In modern Python, a directory without `__init__.py` can also act as a *namespace package*. Therefore, `__init__.py` is not mandatory for every possible kind of package, but it remains common and useful.

---

## 3. Create a Package

Create the following files.

### `akashPackage/__init__.py`

```python
# This file can be empty.
```

### `akashPackage/AkashModule.py`

```python
def demo():
    print("Hello from AkashModule")

def add(a, b):
    return a + b
```

### `akashPackage/ajpackage/__init__.py`

```python
# This file can be empty.
```

### `akashPackage/ajpackage/ajmodule.py`

```python
def show():
    print("Hello from ajmodule")

def multiply(a, b):
    return a * b
```

---

## 4. Import a Module from a Package

Use the `import` statement to import a module using its package path.

### Example: `main.py`

```python
import akashPackage.AkashModule

akashPackage.AkashModule.demo()

result = akashPackage.AkashModule.add(10, 20)
print(result)
```

Output:

```text
Hello from AkashModule
30
```

### Explanation

- `akashPackage` is the package name.
- `AkashModule` is the module name.
- `demo()` is a function defined inside that module.
- The dot (`.`) separates package and module names.

Run `main.py` from the `project` directory so Python can find `akashPackage`.

---

## 5. Import Using an Alias

You can assign an alias to a module.

```python
import akashPackage.AkashModule as am

am.demo()
print(am.add(10, 20))
```

Output:

```text
Hello from AkashModule
30
```

Here, `am` is an alias for `akashPackage.AkashModule`.

---

## 6. Import a Specific Function

Use `from ... import ...` to import a function directly.

```python
from akashPackage.AkashModule import demo, add

demo()
print(add(10, 20))
```

Output:

```text
Hello from AkashModule
30
```

You can also rename an imported function:

```python
from akashPackage.AkashModule import demo as d

d()
```

---

## 7. Import from a Subpackage

A subpackage is a package inside another package.

Using our example structure:

```text
akashPackage/
├── __init__.py
├── AkashModule.py
└── ajpackage/
    ├── __init__.py
    └── ajmodule.py
```

Import a module from the subpackage:

```python
from akashPackage.ajpackage import ajmodule

ajmodule.show()

print(ajmodule.multiply(5, 4))
```

Output:

```text
Hello from ajmodule
20
```

The full import path is:

```text
akashPackage.ajpackage.ajmodule
```

---

## 8. Relative Imports Inside Packages

Inside a package, relative imports can refer to other modules using leading dots.

For example, suppose the structure is:

```text
akashPackage/
├── __init__.py
├── AkashModule.py
└── ajpackage/
    ├── __init__.py
    └── ajmodule.py
```

Inside `ajmodule.py`, you could import a member from `AkashModule.py` using:

```python
from ..AkashModule import demo

demo()
```

Explanation:

- `.` refers to the current package.
- `..` refers to the parent package.
- `..AkashModule` refers to the `AkashModule` module in the parent package.

Relative imports are intended for code running as part of a package. Running a package module directly as a standalone script can cause relative-import errors.

---

## 9. What Is `__init__.py`?

The `__init__.py` file can be empty, or it can contain code that runs when the package is initialized.

For example:

```python
# akashPackage/__init__.py

print("akashPackage initialized")
```

When the package is first imported in a Python process, this statement runs as part of package initialization.

You can also expose selected members through the package:

```python
# akashPackage/__init__.py

from .AkashModule import demo, add
```

Now you can write:

```python
from akashPackage import demo, add

demo()
print(add(10, 20))
```

This works because `__init__.py` imports those names into the package namespace.

**Best practice:** Keep package initialization simple. Avoid placing expensive or unnecessary work in `__init__.py`.

---

## 10. Package vs Module

| Feature | Module | Package |
|---|---|---|
| Meaning | Usually a Python file | Organizes modules in a directory structure |
| Typical example | `AkashModule.py` | `akashPackage/` |
| Contains | Functions, variables, classes | Modules and possibly subpackages |
| Import example | `import AkashModule` | `import akashPackage.AkashModule` |

---

## 11. Package vs Library

A package is a way to organize Python code. A library is reusable code designed to provide functionality to other programs.

A library may consist of one or more packages and modules.

Examples of widely used Python libraries include Django and Requests.

---

## 12. Common Mistakes

### Mistake 1: Incorrect Module Name

If the file is named `AkashModule.py`, use the matching module name in your import:

```python
from akashPackage import AkashModule
```

Python module names are case-sensitive in many environments, including typical Linux systems.

### Mistake 2: Running from the Wrong Directory

For this structure:

```text
project/
├── main.py
└── akashPackage/
    ├── __init__.py
    └── AkashModule.py
```

Run the program from the project directory:

```bash
python main.py
```

### Mistake 3: Confusing a Package with a Module

- `akashPackage` is a package.
- `AkashModule.py` is a module.
- `demo()` is a function.

### Mistake 4: Forgetting the Import Path

This works when `akashPackage` is importable:

```python
from akashPackage.AkashModule import demo
```

If Python cannot find the package, check your folder structure, current working directory, and Python import path.

---

## Summary

- A module is usually a `.py` file containing reusable code.
- A package organizes related modules into a directory structure.
- A subpackage is a package inside another package.
- `__init__.py` is commonly used to define regular Python packages and can be empty.
- Modern Python also supports namespace packages without `__init__.py`.
- Use dot notation to import modules from packages.
- Relative imports use dots to refer to the current or parent package.
