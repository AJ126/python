
# Python Modules

## 1. What Is a Module?

A module is a Python file containing reusable code, such as functions, variables, and classes.

Every `.py` file can act as a module.

Modules help us organize code into separate files and reuse it in other Python programs.

### Example: Module Structure

Create two files in the same folder:

```text
project/
├── akashModules.py
└── main.py
```

**akashModules.py**

```python
name = "Akash"
age = 25

def demo():
    print("This is the demo function")

def testfun():
    print("This is the test function")

class Student:
    def show(self):
        print("This is the Student class")
```

**main.py**

```python
import akashModules

print(akashModules.name)
print(akashModules.age)

akashModules.demo()
akashModules.testfun()

student = akashModules.Student()
student.show()
```

Output:

```text
Akash
25
This is the demo function
This is the test function
This is the Student class
```

### Explanation

- `akashModules.py` is the module file.
- `import akashModules` imports the module.
- `akashModules.name` accesses a variable.
- `akashModules.demo()` calls a function.
- `akashModules.Student` accesses a class.

**Important:** Use the module's filename without the `.py` extension when importing it. The module file must be available through Python's module search path.

---

## 2. Why Do We Use Modules?

Modules provide several advantages:

1. **Code reusability:** Write code once and use it in multiple programs.
2. **Organization:** Separate related functionality into different files.
3. **Maintainability:** Update one module instead of duplicating code.
4. **Readability:** Keep large projects organized.
5. **Namespace separation:** Access module members through the module name.

### Real-Life Example

Imagine building a Django project with separate modules for:

- Customer operations
- Product operations
- Payment processing
- Email notifications

Each module can contain related functions and classes, making the project easier to maintain.

---

## 3. Module Aliasing

Module aliasing means assigning a shorter or different name to a module when importing it.

### Syntax

```python
import module_name as alias_name
```

### Example

```python
import akashModules as module

module.demo()
module.testfun()

print(module.name)
```

Here, `module` is an alias for `akashModules`.

You use the alias to access members instead of writing the full module name.

### Another Example

```python
import math as m

print(m.sqrt(25))
print(m.pi)
```

Output:

```text
5.0
3.141592653589793
```

**Important:** The alias is the name used in the importing file. It does not rename the original module file.

---

## 4. Member Aliasing

Member aliasing means importing a specific function, variable, or class from a module under a different name.

### Syntax

```python
from module_name import member_name as alias_name
```

### Example

```python
from akashModules import demo as d, testfun as t

d()
t()
```

Output:

```text
This is the demo function
This is the test function
```

Here:

- `d` is an alias for `demo`.
- `t` is an alias for `testfun`.

### Importing a Member Without an Alias

```python
from akashModules import demo

demo()
```

This lets you call `demo()` directly without writing `akashModules.demo()`.

**Tip:** Prefer clear alias names. Very short names may make larger programs harder to understand.

---

## 5. Importing Multiple Members

You can import multiple members from one module.

```python
from akashModules import name, age, demo

print(name)
print(age)
demo()
```

You can also import a module and access its members through the module name:

```python
import akashModules

print(akashModules.name)
akashModules.demo()
```

For larger programs, `import module_name` often makes it clearer where a member comes from.

---

## 6. Reloading a Module

Python normally caches an imported module in `sys.modules`. Importing that module again generally reuses the existing module object rather than executing the module's code from scratch.

If the source file changes while a Python process is running, you may want to reload it.

Python provides the `reload()` function through the `importlib` module.

### Example

**akashModules.py**

```python
def demo():
    print("Original version")
```

**main.py**

```python
import akashModules
from importlib import reload

akashModules.demo()

# Reload the module when its source file has been updated.
reload(akashModules)

akashModules.demo()
```

### How to use it

1. Import the module.
2. Update the module's source code and save the file.
3. Call `reload(akashModules)`.
4. Call the function again to check the updated behavior.

**Important:** `reload()` does not wait for 30 seconds automatically. It reloads the module when the `reload()` call executes.

### Example with a Delay

```python
import time
import akashModules
from importlib import reload

time.sleep(30)
reload(akashModules)

print("Module reloaded")
```

This program waits 30 seconds and then reloads the module. However, it does not automatically detect whether the file changed.

### Important Reloading Notes

- `reload()` re-executes the module's code.
- It does not automatically update every reference previously imported using `from module import function`.
- Existing objects created from classes in the old module may continue to use the old class definition.
- Reloading a module is not a substitute for restarting a production application when a clean restart is required.

---

## 7. Finding Module Members Using `dir()`

Python provides the built-in `dir()` function to list names available in a scope or names associated with an object.

### 7.1 Using `dir()` Without Arguments

```python
name = "Akash"

def demo():
    pass

print(dir())
```

This lists names in the current local scope, including names such as `name` and `demo`.

The output can also contain special names added by Python.

### 7.2 Using `dir()` with a Module

```python
import math

print(dir(math))
```

This displays names available in the `math` module, including functions and constants such as:

- `sqrt`
- `pi`
- `ceil`
- `floor`

You can check whether a specific member exists:

```python
import math

print("sqrt" in dir(math))
```

Output:

```text
True
```

**Important:** `dir()` lists names; it does not necessarily tell you what every member does. Use `help()` to learn more.

---

## 8. Using `help()` to Understand a Module

The `help()` function displays documentation about a module, function, class, or other object.

### Example

```python
import math

help(math)
```

To get help for a specific function:

```python
help(math.sqrt)
```

This displays information about the `sqrt()` function.

You can also inspect your own module:

```python
import akashModules

help(akashModules)
```

---

## 9. What Happens When We Import a Module?

When Python imports a module for the first time in a process, it generally:

1. Finds the module through its import search mechanism.
2. Creates or prepares a module object.
3. Executes the module's top-level code.
4. Makes the resulting module object available for reuse through the import system.

### Example

**akashModules.py**

```python
print("Module is being executed")

def demo():
    print("Demo function")
```

**main.py**

```python
import akashModules
import akashModules

akashModules.demo()
```

Typical output:

```text
Module is being executed
Demo function
```

The module's top-level code normally executes only once per module object in that Python process. A later import usually reuses the cached module.

---

## 10. Python Compiled Files: `.pyc` and `__pycache__`

Python may compile imported source modules into bytecode and cache that bytecode in `.pyc` files.

These cached files are commonly stored in a directory named `__pycache__`.

### Example Folder Structure

```text
project/
├── akashModules.py
├── main.py
└── __pycache__/
    └── akashModules.cpython-313.pyc
```

The exact filename and Python version tag may differ.

### Important Correction

It is **not guaranteed that every module import creates a permanent compiled file on the hard disk**.

- Python may write bytecode cache files for imported source modules.
- The cache is normally stored under `__pycache__`.
- Python can run without writing these cache files in certain configurations.
- Cache files can be deleted and regenerated.
- They are not a replacement for the original `.py` source file.
- A script executed directly is not necessarily cached in the same way as an imported module.

### Should We Commit `__pycache__` to Git?

Usually, no. Add the following entries to your `.gitignore` file:

```gitignore
__pycache__/
*.py[cod]
```

These rules ignore Python bytecode cache directories and common compiled Python files.

---

## 11. Difference Between `import` and `from ... import`

### Using `import`

```python
import akashModules

akashModules.demo()
```

You access members through the module name.

### Using `from ... import`

```python
from akashModules import demo

demo()
```

You can use the imported member directly.

### Comparison

| Feature | `import module` | `from module import member` |
|---|---|---|
| Imports | Module object | Selected member names |
| Calling a function | `module.demo()` | `demo()` |
| Namespace clarity | Module name remains visible | Source module may be less obvious |
| Useful when | You need multiple module members | You need a small number of specific members |

**Note:** `from module import member` binds the member name in the importing scope. If the module is later reloaded, that previously imported reference is not automatically rebound.

---

## 12. Important Best Practices

- Use meaningful module filenames, such as `customer_utils.py`.
- Avoid naming your files after standard-library modules, such as `random.py`, `json.py`, or `time.py`, because this can interfere with imports.
- Keep related functionality together.
- Use `if __name__ == "__main__":` to separate reusable module code from code intended to run when the file is executed directly.
- Do not store passwords, secret keys, or other sensitive information in reusable modules.
- Avoid unnecessary wildcard imports such as `from module import *`.
- Keep `__pycache__` and `.pyc` files out of version control in most projects.

### Example: `if __name__ == "__main__":`

```python
def demo():
    print("Demo function")

if __name__ == "__main__":
    demo()
```

When this file is run directly, `demo()` executes. When it is imported as a module, that block does not execute.

---

## Summary

- A module is a Python file containing reusable code.
- `import` imports a module.
- `as` creates an alias.
- `from ... import` imports selected members.
- `reload()` re-executes an already imported module's code.
- `dir()` lists names available in a scope or associated with an object.
- `help()` displays documentation.
- Imported modules may have bytecode cached in `__pycache__`.
- Bytecode cache files are not guaranteed to be created permanently for every import.
