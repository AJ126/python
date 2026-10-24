---

# Object-Oriented Programming (OOP) Questions and Answers

## Table of Contents — New Questions

31. Representing multiple accounts using objects
32. What happens if a method accesses an uninitialized instance variable?
33. What is a constructor?
34. What is the purpose of a constructor?
35. Example of a parameterized constructor
36. Can an object be created without defining a constructor?
37. What are the types of constructors?
38. Does Python support constructor overloading?
39. What is the syntax for creating an object?
40. What is a destructor?
41. What is garbage collection?
42. What is the difference between instance and class variables?
43. What are local variables in a class?
44. How do class variables work?
45. What is a class method?
46. How can we hide class data?
47. What is a static method?

---

## 31. How can we represent two accounts using objects?

We can create a class named `Account` and create two separate objects. Each object stores its own account number, name, and balance.

```python
class Account:
    def store_account_data(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance

    def display_account_details(self):
        print("Account Number:", self.accno)
        print("Name:", self.name)
        print("Balance:", self.balance)


acc1 = Account()
acc1.store_account_data(100001, "Rama", 40000)

acc2 = Account()
acc2.store_account_data(100002, "Ramu", 50000)

print("First account:")
acc1.display_account_details()

print("\nSecond account:")
acc2.display_account_details()
```

**Output:**

```text
First account:
Account Number: 100001
Name: Rama
Balance: 40000

Second account:
Account Number: 100002
Name: Ramu
Balance: 50000
```

**Explanation:**

- `Account` is a class.
- `acc1` and `acc2` are separate objects.
- `self` refers to the object whose method is being called.
- Each object has its own instance variables and state.

## 32. What happens if a method accesses an instance variable before it is initialized?

An `AttributeError` occurs if the attribute has not been created on the object and cannot be found through its class or inheritance.

```python
class Account:
    def display_account_details(self):
        print(self.accno)


acc = Account()
acc.display_account_details()
```

**Error:**

```text
AttributeError: 'Account' object has no attribute 'accno'
```

In this example, `accno` is never initialized.

**Good practice:** Initialize required instance variables in the constructor so objects begin in a valid state.

## 33. What is a constructor in Python?

A constructor is commonly understood as the initialization method `__init__()` in a Python class. Python calls it automatically when a new object is initialized.

```python
class Employee:
    def __init__(self):
        print("Employee object initialized")


emp = Employee()
```

**Output:**

```text
Employee object initialized
```

Technically, `__new__()` creates the object, while `__init__()` initializes it.

## 34. What is the purpose of a constructor?

The main purpose of `__init__()` is to initialize an object's attributes and establish its initial state.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student = Student("Amit", 85)

print(student.name)   # Amit
print(student.marks)  # 85
```

Here, the constructor initializes `name` and `marks` when the object is created.

## 35. Write a Python program using a parameterized constructor.

A parameterized constructor accepts arguments so different objects can start with different values.

```python
class Account:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance

    def display_account_details(self):
        print("Account Number:", self.accno)
        print("Name:", self.name)
        print("Balance:", self.balance)


acc1 = Account(100001, "Rama", 40000)
acc2 = Account(100002, "Ramu", 50000)

acc1.display_account_details()
print()
acc2.display_account_details()
```

**Key point:** Python automatically calls `__init__()` during normal object creation, passing the supplied arguments along with the object reference as `self`.

## 36. Can we create an object without defining a constructor?

Yes. If a class does not define its own `__init__()`, Python can use an inherited initializer, normally from `object`, provided the arguments are compatible.

```python
class Employee:
    pass


emp = Employee()
print("Object created")
```

**Output:**

```text
Object created
```

You do not have to write `__init__()` in every class.

## 37. What are the types of constructors in Python?

In beginner-level OOP notes, constructors are commonly classified as:

1. **Default or zero-argument constructor:** An initializer that takes no extra arguments beyond `self`.
2. **Parameterized constructor:** An initializer that accepts additional arguments.

Example:

```python
class Employee:
    def __init__(self):
        self.name = "Unknown"


class Student:
    def __init__(self, name):
        self.name = name


emp = Employee()
student = Student("Amit")

print(emp.name)       # Unknown
print(student.name)   # Amit
```

**Note:** Python does not automatically insert a new `__init__()` function into the class source code. If one is not defined, an inherited initializer is used where applicable.

## 38. Does Python support constructor overloading?

Python does not support traditional constructor overloading in which several `__init__()` definitions coexist with different parameter lists.

If you define `__init__()` more than once in the same class, the last definition replaces the earlier definition.

```python
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __init__(self):
        self.name = "Rama"
        self.balance = 40000


acc = Account()

print(acc.name)     # Rama
print(acc.balance)  # 40000
```

The first initializer is replaced by the second one.

**How can we support different argument combinations?** Use default parameter values or other initialization logic.

```python
class Account:
    def __init__(self, name="Rama", balance=40000):
        self.name = name
        self.balance = balance


acc1 = Account()
acc2 = Account("Ramu", 50000)

print(acc1.name, acc1.balance)  # Rama 40000
print(acc2.name, acc2.balance)  # Ramu 50000
```

## 39. What is the syntax for creating an object in Python?

The general syntax is:

```python
object_name = ClassName(arguments)
```

Examples:

```python
class Employee:
    def __init__(self, emp_id=None, name=None):
        self.emp_id = emp_id
        self.name = name


emp1 = Employee()
emp2 = Employee(1001, "Rama")

print(emp2.emp_id)  # 1001
print(emp2.name)    # Rama
```

The arguments depend on the class's initializer.

## 40. What is a destructor in Python?

`__del__()` is a special method sometimes called a finalizer. It may run when an object is about to be finalized, but its exact timing is not guaranteed in every Python implementation or situation.

```python
class Demo:
    def __del__(self):
        print("Finalizer called")


obj = Demo()
del obj
```

The message may appear when the object is finalized, but do not rely on `__del__()` for timely resource cleanup.

**Best practice:** Use context managers, such as `with open(...)`, to manage files and other resources reliably.

## 41. What is garbage collection?

Garbage collection is part of Python's memory-management system. It helps reclaim memory occupied by objects that are no longer needed.

```python
class Demo:
    pass


obj = Demo()
obj = None
```

After `obj = None`, the variable no longer refers to the original object. If no other references remain, the object can become eligible for reclamation.

**Important:** Do not assume that all memory is released immediately when a variable is deleted. Exact behavior depends on references and the Python implementation.

## 42. What is the difference between instance variables and class variables?

| Instance variables | Class variables |
|---|---|
| Belong to individual objects | Are defined on the class |
| Usually accessed through `self` | Commonly accessed through the class name |
| Each object can have its own value | Shared through the class unless shadowed by an instance attribute |
| Store object-specific data | Often store information shared across objects |

Example:

```python
class Employee:
    company = "ABC Ltd"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable


e1 = Employee("Rama")
e2 = Employee("Ramu")

print(e1.name)       # Rama
print(e2.name)       # Ramu
print(Employee.company)  # ABC Ltd
```

## 43. What are local variables in a class?

A local variable is created inside a method and is normally available only within that method's scope.

```python
class Calculator:
    def add(self, a, b):
        result = a + b
        return result


calc = Calculator()
print(calc.add(10, 20))  # 30
```

Here, `a`, `b`, and `result` are local variables or parameters within the method. They are not automatically stored as instance attributes.

To store a value on the object, use `self`, such as `self.result = a + b`.

## 44. How do class variables work?

A class variable is defined in the class body, outside instance methods. It can be used to represent information shared by objects.

```python
class Employee:
    emp_count = 0

    def __init__(self):
        Employee.emp_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.emp_count


e1 = Employee()
e2 = Employee()

print(Employee.get_employee_count())  # 2
```

**Why use a class variable?**

If we put `emp_count = 0` inside `__init__()` as `self.emp_count = 0`, each object would have its own counter. The shared count would not work as intended.

**Important:** Assigning `e1.emp_count = 10` creates or updates an instance attribute on `e1`; it does not change the class variable `Employee.emp_count`.

## 45. What is a class method in Python?

A class method is decorated with `@classmethod`. Its first parameter conventionally is `cls`, which refers to the class.

```python
class Employee:
    emp_count = 0

    def __init__(self):
        Employee.emp_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.emp_count


e1 = Employee()
e2 = Employee()

print(Employee.get_employee_count())  # 2
```

Class methods are useful for working with class-level data and for alternative constructors.

They can be called using the class name or an object reference.

## 46. How can we hide data inside a Python class?

Python does not have a `private` keyword. An attribute name that begins with two underscores, such as `__emp_count`, triggers **name mangling**.

```python
class Employee:
    __emp_count = 0

    def __init__(self):
        Employee.__emp_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.__emp_count


e1 = Employee()
e2 = Employee()

print(Employee.get_employee_count())  # 2
```

The double underscore changes the attribute's internal name to help avoid accidental access and naming conflicts.

**Important:** Name mangling is not strict security or absolute privacy. The attribute can still be accessed using its mangled name if necessary.

## 47. What is a static method in Python?

A static method uses the `@staticmethod` decorator. It does not automatically receive `self` or `cls`.

It is useful for utility functions logically related to a class but not requiring access to a particular object or class state.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))  # 30
```

### Difference between instance, class, and static methods

| Method type | Decorator | First argument supplied automatically | Common use |
|---|---|---|---|
| Instance method | None required | `self` | Work with one object's state |
| Class method | `@classmethod` | `cls` | Work with class-level state |
| Static method | `@staticmethod` | None | Related utility logic |


## 48. What is an abstract method?

An **abstract method** is a method declared without a complete implementation that requires concrete subclasses to provide an implementation.

Python provides the `@abstractmethod` decorator in the `abc` module.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
```

**Explanation:**
- `@abstractmethod` marks the method as abstract.
- `pass` is a placeholder; it does not provide the actual behavior.
- A concrete subclass must implement the abstract method before it can be instantiated.

## 49. What is an abstract class?

An **abstract class** is a class that cannot be instantiated while it has unresolved abstract methods.

It commonly inherits from `ABC` and declares one or more abstract methods.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving")


car = Car()
car.move()
```

**Output:**

```text
Car is moving
```

If `Car` does not implement `move()`, attempting to instantiate it raises a `TypeError`.

**Important points:**
- An abstract class can contain both abstract and concrete methods.
- It can have instance variables and class variables.
- A subclass must implement all inherited abstract methods to become instantiable.

## 50. What is the `super()` function in Python?

`super()` is a built-in function that provides access to methods in the next class in the method resolution order (MRO). It is commonly used to call parent-class methods and constructors.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        super().display()
        print("Salary:", self.salary)


emp = Employee("Amit", 50000)
emp.display()
```

**Output:**

```text
Name: Amit
Salary: 50000
```

**Key points:**
- `super().__init__(name)` calls the next class's initializer.
- `super().display()` calls the next class's `display()` method.
- Use `self` to access attributes on the current object, such as `self.name`.
- `super()` can also call class methods and static methods where appropriate.
- In multiple inheritance, `super()` follows the method resolution order; it does not simply mean “call the direct parent.”

## 51. What are the different relationships in object-oriented programming?

Three commonly discussed relationships are **has-a**, **is-a**, and **use-a**.

### 1. Has-a relationship

One object contains or holds a reference to another object.

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()


car = Car()
car.start_car()
```

Here, a `Car` has an `Engine`.

### 2. Is-a relationship

An inheritance relationship in which a child class is a specialized type of its parent class.

```python
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


dog = Dog()
dog.eat()
```

Here, a `Dog` is an `Animal`.

### 3. Use-a relationship

One object uses another object by receiving it as an argument or otherwise accessing it.

```python
class Printer:
    def print_message(self, message):
        print(message)


class Report:
    def display(self, printer):
        printer.print_message("Monthly report")


printer = Printer()
report = Report()
report.display(printer)
```

Here, `Report` uses a `Printer` object.

## 52. How can we display an object's state using `print()`?

Override the `__str__()` method to return a readable string representing the object's state.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}"


student = Student("Amit", 85)
print(student)
```

**Output:**

```text
Name: Amit, Marks: 85
```

**Important points:**
- `__str__()` must return a string.
- `print(student)` calls the object's string representation.
- If you do not override `__str__()`, Python uses the inherited implementation, which normally displays a class name and an object-identifying representation rather than your custom data.

## 53. What is the base class of all Python classes?

In Python 3, `object` is the ultimate base class of ordinary classes that do not explicitly inherit from another class.

```python
class Employee:
    pass


emp = Employee()

print(isinstance(emp, object))  # True
print(issubclass(Employee, object))  # True
```

Python classes inherit behavior from `object`, including methods such as `__str__()` and `__repr__()`, unless those methods are overridden.

## 54. What is polymorphism?

**Polymorphism** means “one interface, multiple forms.” Different objects can respond to the same method call in different ways.

```python
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

**Output:**

```text
Bark
Meow
```

Both objects provide a `sound()` method, but each behaves differently.

**Benefits:**
- Makes code more flexible and extensible.
- Allows different object types to be used through a common interface.
- Reduces the need for type-specific conditional logic.

## 55. What is method overloading?

Traditional **method overloading** means defining multiple methods with the same name but different parameter signatures within one class.

Python does not support traditional method overloading through multiple definitions of the same method name. The last definition replaces earlier definitions.

```python
class Addition:
    def add(self, n1, n2, n3):
        return n1 + n2 + n3

    def add(self, n1, n2):
        return n1 + n2


addition = Addition()

print(addition.add(10, 20))  # 30
print(addition.add(10, 20, 30))  # TypeError
```

The second `add()` definition replaces the first one, so the three-argument call raises `TypeError`.

### How can we handle different numbers of arguments?

Use default values or variable-length arguments.

```python
class Addition:
    def add(self, n1, n2, n3=0):
        return n1 + n2 + n3


addition = Addition()

print(addition.add(10, 20))       # 30
print(addition.add(10, 20, 30))   # 60
```

Python also supports polymorphic behavior through inheritance, overriding, and duck typing. These are not the same as traditional signature-based method overloading.

## 56. What is operator overloading?

**Operator overloading** means defining how an operator behaves when used with objects of a custom class.

Python uses special methods, often called magic methods, to implement this behavior. For example, `__add__()` defines addition behavior.

This topic extends the existing `__add__()` question in your file.

```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __add__(self, other):
        return self.price + other.price


book1 = Book("Python Complete Reference", 635)
book2 = Book("Mastering Python", 1275)

print(book1 + book2)
```

**Output:**

```text
1910
```

Here, `book1 + book2` calls `book1.__add__(book2)`.

Other examples of operator-related special methods include:

| Operator | Special method |
|---|---|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `>` | `__gt__()` |
| `<=` | `__le__()` |
| `==` | `__eq__()` |

Operator overloading allows operators to work naturally with custom objects.

---

## Quick Revision — OOP

- **Class:** A definition describing the attributes and behavior of objects.
- **Object:** An instance of a class.
- **Instance variable:** Stores object-specific data.
- **Class variable:** Stores data associated with the class.
- **Constructor/initializer:** `__init__()` initializes an object.
- **Parameterized initializer:** Accepts arguments to set initial values.
- **Constructor overloading:** Multiple `__init__()` definitions do not coexist in one Python class.
- **Destructor/finalizer:** `__del__()` may run during object finalization; timing is not guaranteed.
- **Garbage collection:** Helps reclaim memory from objects that are no longer needed.
- **Class method:** Uses `@classmethod` and receives `cls`.
- **Static method:** Uses `@staticmethod` and receives neither `self` nor `cls` automatically.
- **Double-underscore name:** Triggers name mangling, not strict privacy.
- **Abstract method:** A method marked with `@abstractmethod` that requires implementation by a concrete subclass.
- **Abstract class:** A class that cannot be instantiated while abstract methods remain unimplemented.
- **`super()`:** Accesses methods through the method resolution order.
- **Has-a:** One object holds a reference to another object.
- **Is-a:** An inheritance relationship.
- **Use-a:** An object uses another object, such as through a method argument.
- **`__str__()`:** Returns a readable string representation of an object.
- **`object`:** The ultimate base class for ordinary Python classes.
- **Polymorphism:** Different objects respond to the same interface in different ways.
- **Method overloading:** Multiple same-named methods with different signatures; traditional signature-based overloading is not supported by Python.
- **Operator overloading:** Customizes operator behavior using special methods such as `__add__()`.