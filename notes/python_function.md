
# Python Functions – Beginner to Advanced Notes

## 1. What Is a Function?

A function is a reusable block of code that performs a particular task.

When the same statements are required repeatedly, we can place them inside a function and call that function whenever needed.

### Example

```python
def greet():
    print("Hello!")
    print("Welcome to Python.")

greet()
greet()
```

Output:

```text
Hello!
Welcome to Python.
Hello!
Welcome to Python.
```

### Advantages

- Code reusability.
- Less code duplication.
- Better readability and organization.
- Easier testing and maintenance.

A function does not have to return a value. It can perform an action, return a result, or do both.

---

## 2. Types of Functions

Python functions are commonly classified into two categories.

### 2.1 Built-in Functions

Built-in functions are provided by Python.

Examples:

```python
print("Hello")
len("Python")
type(10)
id(10)
sum([10, 20, 30])
max([10, 20, 30])
```

Explanation:

- `print()` displays information.
- `len()` returns the number of items.
- `type()` returns an object's type.
- `id()` returns an object's identity.
- `sum()` calculates the sum of numeric items.
- `max()` returns the largest item.

### 2.2 User-defined Functions

Functions created by programmers are called user-defined functions.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```text
30
```

Here, `add()` is a user-defined function.

---

## 3. Function Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

Explanation:

- `def` defines a function.
- `function_name` is the function's name.
- `parameters` receive values passed to the function.
- The indented statements form the function body.
- `return` sends a result back to the caller.

The `return` statement is optional.

### Function without return

```python
def greet():
    print("Hello")

greet()
```

### Function with return

```python
def square(number):
    return number * number

result = square(5)
print(result)
```

Output:

```text
25
```

---

## 4. Parameters and Arguments

A **parameter** is a variable written in a function definition.

An **argument** is a value supplied when calling the function.

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Here:

- `a` and `b` are parameters.
- `10` and `20` are arguments.

Python supports several ways of supplying arguments.

### 4.1 Positional Arguments

Values are matched to parameters according to their positions.

```python
def subtract(a, b):
    return a - b

print(subtract(10, 5))
print(subtract(5, 10))
```

Output:

```text
5
-5
```

Changing the order can change the result.

### 4.2 Keyword Arguments

Values are passed using parameter names.

```python
def student(name, marks):
    print("Name:", name)
    print("Marks:", marks)

student(marks=85, name="Shiv")
```

Output:

```text
Name: Shiv
Marks: 85
```

Keyword arguments can make function calls easier to read.

### 4.3 Default Arguments

A parameter can have a default value. Python uses that value when the caller does not supply an argument for the parameter.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Shiv")
```

Output:

```text
Hello Guest
Hello Shiv
```

Parameters with default values generally follow parameters without default values.

```python
def greet(name, message="Welcome"):
    print(message, name)

greet("Shiv")
greet("Shiv", "Good morning")
```

### 4.4 Variable-Length Positional Arguments: `*args`

Use `*args` when a function should accept any number of positional arguments.

```python
def show_values(*args):
    print(args)

show_values(10)
show_values(10, 20)
show_values(10, 20, 30)
```

Output:

```text
(10,)
(10, 20)
(10, 20, 30)
```

Inside the function, `args` is a tuple.

The name `args` is conventional; the asterisk is what enables this behavior.

### 4.5 Variable-Length Keyword Arguments: `**kwargs`

Use `**kwargs` to accept any number of keyword arguments.

```python
def show_details(**kwargs):
    print(kwargs)

show_details(name="Shiv", age=25, city="Pune")
```

Output:

```text
{'name': 'Shiv', 'age': 25, 'city': 'Pune'}
```

Inside the function, `kwargs` is a dictionary.

### `*args` vs `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Accepts | Extra positional arguments | Extra keyword arguments |
| Stored as | Tuple | Dictionary |
| Example | `f(10, 20)` | `f(name="Shiv")` |

---

## 5. The `return` Statement

The `return` statement sends a result back to the caller and ends the current function execution.

```python
def multiply(a, b):
    return a * b

answer = multiply(4, 5)
print(answer)
```

Output:

```text
20
```

### What if we do not use return?

```python
def show():
    print("Hello")

result = show()
print(result)
```

Output:

```text
Hello
None
```

A function without an explicit return value returns `None`.

**Remember:** `print()` displays a value, while `return` provides a value to the code calling the function.

---

## 6. Function vs Module vs Package

### Function

A reusable block of code that performs a task.

### Module

A Python file containing code such as functions, classes, and variables.

Example: `calculator.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Another file can import the module:

```python
import calculator

print(calculator.add(10, 20))
```

Output:

```text
30
```

### Package

A package organizes related Python modules into a directory structure.

Example:

```text
math_tools/
    __init__.py
    arithmetic.py
    geometry.py
```

A package may contain subpackages as well.

**Note:** In casual explanations, a collection of modules is sometimes called a library. Technically, a library is reusable code, and it may be distributed as a package or contain multiple packages and modules.

---

## 7. Types of Variables: Global and Local

### 7.1 Global Variables

A variable declared at module level is called a global variable.

```python
message = "Hello"

def greet():
    print(message)

greet()
print(message)
```

Output:

```text
Hello
Hello
```

The function can read the global variable because it is accessible in that scope.

### 7.2 Local Variables

A variable assigned inside a function is generally local to that function unless another scope declaration applies.

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

Output:

```text
Hello
```

Trying to access `message` outside the function will cause a `NameError` if no such variable exists in the surrounding scope.

### Important distinction

Python uses the LEGB name-resolution rule:

1. Local
2. Enclosing
3. Global
4. Built-in

This explains how Python searches for a name when code uses it.

---

## 8. The `global` Keyword

The `global` keyword allows a function to assign to a variable defined at module level.

### Without `global`

```python
a = 10

def change_value():
    a = 8888
    print(a)

def show_value():
    print(a)

change_value()
show_value()
```

Output:

```text
8888
10
```

Inside `change_value()`, the assignment creates a local variable named `a`. The module-level variable remains `10`.

### With `global`

```python
a = 10

def change_value():
    global a
    a = 8888
    print(a)

def show_value():
    print(a)

change_value()
show_value()
```

Output:

```text
8888
8888
```

Here, `global a` tells Python that the assignment should update the module-level variable.

**Best practice:** Prefer returning values from functions instead of modifying global variables unnecessarily.

---

## 9. Recursive Functions

A recursive function calls itself.

Recursion is useful when a problem can be divided into smaller versions of the same problem.

### Example: Factorial

The factorial of 5 is:

`5 × 4 × 3 × 2 × 1 = 120`

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

### How it works

- `factorial(5)` calls `factorial(4)`.
- `factorial(4)` calls `factorial(3)`.
- This continues until the base case is reached.
- The results are then combined while the calls return.

### Base case

The base case stops the recursion.

Without a suitable base case, recursion may continue until Python raises a `RecursionError`.

### Advantages and disadvantages

Advantages:
- Can express certain problems clearly.
- Useful for tree traversal and divide-and-conquer algorithms.

Disadvantages:
- Uses stack space for function calls.
- May be slower than an iterative solution.
- Deep recursion can exceed Python's recursion limit.

---

## 10. Anonymous or Lambda Functions

A lambda function is a small anonymous function defined using the `lambda` keyword.

### Syntax

```python
lambda arguments: expression
```

A lambda expression contains a single expression whose result becomes the returned value.

### Example

```python
square = lambda n: n * n

print(square(5))
```

Output:

```text
25
```

### Normal function vs lambda

Normal function:

```python
def square(n):
    return n * n
```

Lambda function:

```python
square = lambda n: n * n
```

Both calculate the square of a number.

**Best practice:** Use `def` for complex logic. Lambda functions are most useful for short expressions, such as sorting keys or simple transformations.

---

## 11. The `map()` Function

The `map()` function applies a function to each item in an iterable and returns a map iterator.

### Syntax

```python
map(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

result = map(square, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16, 25]
```

### Using lambda with map()

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda n: n * n, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16, 25]
```

### Important points

- `map()` processes items when its iterator is consumed.
- Convert the result to `list()` if you need to display all results immediately.
- A map iterator is consumed as you iterate over it.

### map() vs for loop

```python
numbers = [1, 2, 3]
squares = []

for number in numbers:
    squares.append(number * number)

print(squares)
```

This produces the same result as the `map()` example.

Use whichever approach makes the code easier to understand.

---

## 12. The `reduce()` Function

The `reduce()` function combines items cumulatively to produce a single result.

It is available in the `functools` module.

### Syntax

```python
from functools import reduce

reduce(function, iterable)
```

### Example: Sum of numbers

```python
from functools import reduce

numbers = [10, 20, 30, 40]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output:

```text
100
```

### How it works

The function combines the values step by step:

```text
10 + 20 = 30
30 + 30 = 60
60 + 40 = 100
```

### Example: Find the largest value

```python
from functools import reduce

numbers = [12, 45, 8, 30]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print(largest)
```

Output:

```text
45
```

**Important:** Calling `reduce()` on an empty iterable without an initial value raises `TypeError`. You can supply an initial value as the third argument when appropriate.

### map() vs reduce()

| Feature | `map()` | `reduce()` |
|---|---|---|
| Purpose | Transform each item | Combine items |
| Result | Iterator | One accumulated result |
| Example | Square every number | Add all numbers |
| Import required | No | Yes, from `functools` |

---

## 13. Function Aliasing

Function aliasing means assigning an existing function object to another name.

```python
def test():
    print("Welcome to Python")

a = test

test()
a()
```

Output:

```text
Welcome to Python
Welcome to Python
```

Both names refer to the same function object.

### Important distinction

```python
a = test
```

Assigns the function itself to `a`.

```python
a = test()
```

Calls the function immediately and assigns its return value to `a`.

For the example above, `test()` returns `None`, so `a` becomes `None` in the second case.

---

## 14. Nested Functions

A nested function is a function defined inside another function.

```python
def test():
    print("Main function")

    def value():
        print("Inner function")

    value()

test()
```

Output:

```text
Main function
Inner function
```

The inner function can access variables from its enclosing function.

### Can an inner function be called outside?

An inner function's name is not automatically available outside its enclosing function. However, the outer function can return the inner function.

```python
def outer():
    def inner():
        print("Hello from inner")

    return inner

function_reference = outer()
function_reference()
```

Output:

```text
Hello from inner
```

This behavior is useful in closures and decorators.

---

## 15. Function Decorators

A decorator is a callable that takes another function or callable and returns a replacement or wrapper, often adding behavior without changing the original function's body.

### Example

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
```

Output:

```text
Before function
Hello
After function
```

### How it works

The syntax:

```python
@my_decorator
def greet():
    print("Hello")
```

is broadly equivalent to:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

### Decorators with arguments

To support decorated functions with different arguments, use `*args` and `**kwargs`.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result = func(*args, **kwargs)
        print("Function has finished")
        return result

    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(10, 20))
```

Output:

```text
Function is starting
Function has finished
30
```

In production code, `functools.wraps` is commonly used to preserve the original function's metadata.

---

## 16. Generator Functions

A generator function produces values one at a time using `yield`.

It returns a generator object when called. Its body begins executing when values are requested from that generator.

### Normal function

```python
def get_numbers():
    return [1, 2, 3, 4, 5]

numbers = get_numbers()
print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

### Generator function

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
3
```

Each `next()` requests the next value. The generator pauses at each `yield` and resumes when another value is requested.

### Iterating over a generator

```python
def get_numbers():
    yield 10
    yield 20
    yield 30

for number in get_numbers():
    print(number)
```

Output:

```text
10
20
30
```

### What happens when a generator finishes?

Once the generator has no more values, another call to `next()` raises `StopIteration`.

```python
def get_numbers():
    yield 1
    yield 2

numbers = get_numbers()

print(next(numbers))
print(next(numbers))
# next(numbers) would raise StopIteration here
```

### Why use generators?

- They produce values on demand.
- They can avoid building a complete list in memory.
- They are useful for large files, data streams, and sequences.

Generators are not automatically faster in every situation; their main benefit is often lazy evaluation and reduced memory use.

---

## 17. `return` vs `yield`

| `return` | `yield` |
|---|---|
| Returns a value and ends the current function execution | Produces a value and pauses a generator |
| Does not resume the same function call after returning | Can resume when another value is requested |
| Commonly used for a final result | Commonly used to produce a sequence |
| A function may return a list of values | A generator can produce values one at a time |

### Example

```python
def normal_function():
    return [1, 2, 3]

def generator_function():
    yield 1
    yield 2
    yield 3

print(normal_function())
print(list(generator_function()))
```

Output:

```text
[1, 2, 3]
[1, 2, 3]
```

Although the displayed results are the same, the functions behave differently internally.

---

## 18. Practice Questions

Try answering these questions before looking up the examples again.

1. What is the difference between a parameter and an argument?
2. What does a function return if it has no explicit `return` statement?
3. What is the difference between positional and keyword arguments?
4. What are `*args` and `**kwargs`?
5. What is the purpose of the `global` keyword?
6. What is the base case in recursion?
7. What is the difference between a normal function and a lambda function?
8. What does `map()` return?
9. Why must `reduce()` be imported from `functools`?
10. What is function aliasing?
11. What is a decorator?
12. What is the difference between `return` and `yield`?

### Short Answers

1. A parameter is a variable in a function definition; an argument is a supplied value.
2. `None`.
3. Positional arguments use position; keyword arguments use parameter names.
4. `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dictionary.
5. It allows assignment to a module-level variable from inside a function.
6. The condition that stops recursive calls.
7. A lambda is a small anonymous function limited to a single expression.
8. A map iterator.
9. `reduce()` is provided by the `functools` module.
10. Giving another name to the same function object.
11. A callable that wraps or replaces another callable to add behavior.
12. `return` ends the function; `yield` pauses a generator and produces a value.

---

## Final Tips

- Use descriptive function names such as `calculate_total()` instead of vague names such as `f1()`.
- Keep functions focused on one task.
- Prefer returning results over changing global variables.
- Use `map()` and `reduce()` when they make the code clearer, not just to avoid a loop.
- Use generators when values can be produced on demand.
- Test functions with normal, boundary, and invalid inputs.
