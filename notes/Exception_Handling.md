
# Python Exception Handling

## 1. What Is Exception Handling?

Exception handling is a mechanism in Python that allows us to handle errors that occur while a program is running, so the program can respond appropriately instead of terminating unexpectedly.

Exception handling is mainly used for runtime errors. Syntax errors must generally be corrected before the program can execute.

### Example Without Exception Handling

```python
a = 10
b = 0

result = a / b  # ZeroDivisionError
print(result)

print("Program completed")
```

**Output:**

```text
ZeroDivisionError: division by zero
```

The last `print()` statement does not execute because the exception is not handled.

---

## 2. What Is an Exception?

An **exception** is an unwanted or unexpected event that interrupts the normal flow of a program.

### Examples of Built-in Exceptions

| Exception | Meaning |
|---|---|
| `ZeroDivisionError` | Dividing a number by zero |
| `TypeError` | Performing an operation using an inappropriate type |
| `ValueError` | Providing a value of the correct type but an inappropriate value |
| `FileNotFoundError` | Trying to access a file that does not exist |
| `EOFError` | An input operation reaches the end of a file or input stream unexpectedly |
| `IndexError` | Accessing a sequence using an invalid index |
| `KeyError` | Accessing a dictionary using a missing key |
| `NameError` | Using a name that has not been defined |

**Note:** `SleepingError` and `TyrePuncturedError` are not built-in exceptions. We can create custom exceptions with these names if our application needs them.

---

## 3. The `try` and `except` Blocks

We use `try` and `except` to handle exceptions.

- `try`: Contains code that might raise an exception.
- `except`: Contains code that handles a matching exception.

### Syntax

```python
try:
    # Risky code
    pass
except SomeException:
    # Exception-handling code
    pass
```

### Example

```python
try:
    a = 10
    b = 0
    result = a / b
    print(result)

except ZeroDivisionError:
    print("You cannot divide a number by zero.")

print("Program completed")
```

**Output:**

```text
You cannot divide a number by zero.
Program completed
```

The exception is handled, so the program continues after the `try-except` statement.

### Handling Different Exceptions

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")
```

Each `except` block handles a particular type of exception.

---

## 4. Default Exception Handling in Python

Every exception in Python is represented by an object, and exception types are defined by classes.

When an exception occurs:

1. Python creates an exception object.
2. Python looks for a matching exception handler.
3. If a matching handler is found, the handler executes.
4. If no matching handler is found, the exception propagates up the call stack.
5. If it remains unhandled, Python terminates the program's normal execution and displays an error traceback.

### Example

```python
def calculate():
    return 10 / 0

calculate()
print("This statement will not execute")
```

**Output (simplified):**

```text
ZeroDivisionError: division by zero
```

The function raises an exception, and no matching handler is provided, so the final statement does not execute.

---

## 5. The `finally` Block

The `finally` block is used for cleanup code, such as closing files or releasing resources.

It normally executes whether an exception occurs or not, including when an exception is handled or remains unhandled.

### Syntax

```python
try:
    # Risky code
    pass
except SomeException:
    # Handle exception
    pass
finally:
    # Cleanup code
    pass
```

### Example

```python
try:
    num = 10 / 0

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Finally block executed.")
```

**Output:**

```text
Division by zero is not allowed.
Finally block executed.
```

### Why Do We Need `finally`?

It is not recommended to rely on the `try` block for cleanup because an exception can prevent later statements inside it from executing.

It is also not sufficient to put cleanup only inside `except`, because the `except` block does not execute when no matching exception occurs.

The `finally` block is useful for cleanup in both situations.

**Important:** `finally` is not an absolute guarantee under circumstances such as forced process termination or a system crash. For ordinary file handling, prefer the `with` statement when possible.

### Example: Closing a File

```python
file = None

try:
    file = open("example.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    if file is not None:
        file.close()
        print("File closed.")
```

A simpler and usually preferred approach is:

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

The `with` statement manages the file's cleanup automatically when the block exits.

---

## 6. The `else` Block

The `else` block can be used with `try-except`.

It executes only when the `try` block completes without raising an exception.

### Syntax

```python
try:
    # Risky code
    pass

except SomeException:
    # Runs when a matching exception occurs
    pass

else:
    # Runs when try completes without an exception
    pass

finally:
    # Cleanup code
    pass
```

### Example

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Execution completed.")
```

**Example output for input `5`:**

```text
Enter a number: 5
Result: 20.0
Execution completed.
```

**Example output for input `0`:**

```text
Enter a number: 0
Number cannot be zero.
Execution completed.
```

### Execution Rules

| Situation | `except` | `else` | `finally` |
|---|---|---|---|
| No exception in `try` | Skipped | Executes | Executes |
| Matching exception handled | Executes | Skipped | Executes |
| Unhandled exception | No matching handler | Skipped | Normally executes before propagation |

**Important:** If an exception occurs inside the `else` block, it is not handled by the preceding `except` blocks. The `finally` block still normally executes.

---

## 7. Types of Exceptions

Python exceptions can be studied in two broad categories:

1. Built-in (predefined) exceptions
2. User-defined (custom) exceptions

### 7.1 Built-in Exceptions

Built-in exceptions are provided by Python. They are raised automatically when particular errors occur, although programmers can also raise them explicitly.

Examples:

```python
print(10 / 0)       # ZeroDivisionError
print(int("hello")) # ValueError
print("10" + 5)     # TypeError
```

### 7.2 User-Defined Exceptions

Sometimes an application needs a special exception to represent a business rule or application-specific problem.

We can define a custom exception by creating a class that inherits from `Exception`.

### Example: Invalid Age

```python
class InvalidAgeError(Exception):
    """Raised when the supplied age is invalid."""
    pass


age = int(input("Enter your age: "))

try:
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    print("Age:", age)

except InvalidAgeError as error:
    print("Error:", error)
```

**Example output for input `-5`:**

```text
Error: Age cannot be negative.
```

Here:

- `InvalidAgeError` is a custom exception class.
- `raise` explicitly raises the exception.
- `as error` stores the exception object in the variable `error`.
- `except InvalidAgeError` catches that custom exception.

**Note:** The `int()` conversion occurs before the `try` block in this example. If the input is not an integer, a `ValueError` will occur outside the handler. To handle that too, move the conversion inside the `try` block.

---

## 8. Quick Revision

| Keyword | Purpose |
|---|---|
| `try` | Contains code that might raise an exception |
| `except` | Handles a matching exception |
| `else` | Executes if `try` completes without an exception |
| `finally` | Runs cleanup code in normal exception-handling flow |
| `raise` | Raises an exception explicitly |
| `as` | Gives a name to the caught exception object |

### Best Practices

- Catch specific exceptions instead of using a bare `except`.
- Keep the `try` block focused on the statements that may fail.
- Use `with` for resources such as files whenever possible.
- Use custom exceptions to represent meaningful application-specific errors.
- Do not silently ignore exceptions.
- Avoid catching `BaseException` unless there is a specific, well-justified reason.

---

## 9. Practice Questions

1. What is an exception in Python?
2. What is the difference between a syntax error and a runtime exception?
3. What is the purpose of `try` and `except`?
4. When does the `else` block execute?
5. Why is the `finally` block useful?
6. What is the difference between a built-in exception and a custom exception?
7. What does the `raise` keyword do?
8. What happens if an exception is never handled?

### Practice Program

Write a program that asks the user to enter two integers and divides the first number by the second. Handle invalid input and division by zero, display the result using `else`, and display a completion message using `finally`.
