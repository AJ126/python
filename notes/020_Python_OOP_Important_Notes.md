# Python OOP Important Notes

## 01. What Is Inheritance?

**Inheritance** is an OOP mechanism that allows a new class to acquire properties (variables) and behaviours (methods) from an existing class.

Inheritance establishes an **is-a relationship** between classes.

- **Parent class / Base class:** The existing class whose features are inherited.
- **Child class / Derived class:** The new class that inherits features from the parent class.
- **Base classes** generally contain common features.
- **Derived classes** specialize or extend those features.
- **Code reusability:** Inheritance allows us to reuse existing code instead of writing it again.

**Example:** A `Student` is a `Person`. Therefore, the `Student` class can inherit common person details from the `Person` class.

## 02. Syntax to Create a Derived Class

```python
class Parent:
    pass


class Child(Parent):
    pass
```

General syntax:

```python
class DerivedClassName(BaseClassName):
    # Variables and methods
    pass
```

Here, `Child` inherits from `Parent`.

## 03. Python Program Using Inheritance

### Example 1: Basic inheritance

```python
# studentperson.py

class Person:  # Base class
    def displayPersonDetails(self):
        print("Displays person details...")


class Student(Person):  # Derived class
    def displayStudentDetails(self):
        print("Displays student details...")


s = Student()
s.displayPersonDetails()   # Inherited method
s.displayStudentDetails()
```

**Output:**

```text
Displays person details...
Displays student details...
```

**Explanation:** The `Student` class inherits `displayPersonDetails()` from `Person`. Therefore, the `Student` object can call both methods.

### Example 2: Inheritance with constructors

```python
# studentperson2.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayPersonDetails(self):
        print("NAME:", self.name)
        print("AGE:", self.age)


class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def displayStudentDetails(self):
        self.displayPersonDetails()
        print("ROLLNO:", self.rollno)
        print("MARKS:", self.marks)


s = Student("Rama", 21, 100001, 78)
s.displayStudentDetails()
```

**Output:**

```text
NAME: Rama
AGE: 21
ROLLNO: 100001
MARKS: 78
```

**Explanation:**

- `Person` stores common information such as name and age.
- `Student` adds student-specific information such as roll number and marks.
- `super().__init__(name, age)` calls the parent class constructor.
- `self.rollno` and `self.marks` store the child's additional data.
- `self.displayPersonDetails()` calls the inherited method.

## 04. Access Modifiers in Python

An access modifier describes the intended visibility or accessibility of class members.

Python uses naming conventions rather than strict `public`, `protected`, and `private` access restrictions.

| Type | Naming style | Meaning |
|---|---|---|
| Public | `name` | Can normally be accessed from anywhere |
| Protected convention | `_name` | Intended for internal use and subclasses |
| Private name-mangled | `__name` | Python changes the attribute name to reduce accidental access |

### Example

```python
class Employee:
    def __init__(self):
        self.name = "Rama"          # Public
        self._salary = 50000        # Protected convention
        self.__password = "abc123"  # Name-mangled


emp = Employee()

print(emp.name)
print(emp._salary)

# print(emp.__password)  # AttributeError
```

**Important points:**

- Python does not enforce conventional protected and private access in the same way as some other languages.
- A single underscore is a convention, not a restriction.
- A double underscore triggers name mangling. It is not strong security or absolute privacy.
- By convention, ordinary class attributes and methods are public unless named otherwise.

## 05. What Is Method Overriding?

**Method overriding** occurs when a child class defines a method with the same name as a method inherited from its parent class.

- **Overridden method:** The parent class's method.
- **Overriding method:** The child class's replacement implementation.

When the method is called on a child object, Python normally executes the child's version.

### When is method overriding useful?

1. When the child needs the same method name but different behaviour.
2. When the parent's implementation is insufficient for the child.
3. When implementing a method required by an abstract base class.

### Example 1: Basic method overriding

```python
# methodoverriding1.py

class Vehicle:
    def move(self):
        print("Every vehicle should move this way")


class Car(Vehicle):
    def move(self):
        print("As a car, I move in my own way")


c = Car()
c.move()
```

**Output:**

```text
As a car, I move in my own way
```

### Example 2: Calling the parent method using `super()`

```python
# methodoverriding2.py

class Vehicle:
    def move(self):
        print("Every vehicle should move this way")


class Car(Vehicle):
    def move(self):
        super().move()
        print("As a car, I move in my own way too")


c = Car()
c.move()
```

**Output:**

```text
Every vehicle should move this way
As a car, I move in my own way too
```

**Explanation:** `super().move()` calls the parent implementation before executing the remaining statements in the child's method.

## 06. Types of Inheritance

The main inheritance patterns are single, multiple, multilevel, and hierarchical inheritance. Hybrid inheritance combines multiple patterns.

### 1. Single inheritance

One child class inherits from one parent class.

```python
class Person:
    pass


class Student(Person):
    pass
```

Diagram:

```text
Person
   |
Student
```

### 2. Hierarchical inheritance

Multiple child classes inherit from the same parent class.

```python
class Person:
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass
```

Diagram:

```text
       Person
       /    \
  Student  Teacher
```

### 3. Multilevel inheritance

A derived class becomes the parent of another class.

```python
class Person:
    pass


class Student(Person):
    pass


class CollegeStudent(Student):
    pass
```

Diagram:

```text
Person
   |
Student
   |
CollegeStudent
```

### 4. Multiple inheritance

One child class inherits from more than one parent class.

```python
class Car:
    def moveFast(self):
        print("Moves faster")


class Truck:
    def bearLoad(self):
        print("Bears the load")


class CarTruck(Car, Truck):
    pass


ct = CarTruck()
ct.moveFast()
ct.bearLoad()
```

**Output:**

```text
Moves faster
Bears the load
```

**Explanation:** `CarTruck` inherits methods from both `Car` and `Truck`.

## 07. Method Resolution in Multiple Inheritance

When parent classes define methods with the same name, Python follows the **Method Resolution Order (MRO)** to determine which implementation is selected.

```python
class Car:
    def move(self):
        print("Moving like a car")


class Truck:
    def move(self):
        print("Moving like a truck")


class CarTruck(Car, Truck):
    pass


ct = CarTruck()
ct.move()
```

**Output:**

```text
Moving like a car
```

Because `Car` is listed first in `class CarTruck(Car, Truck)`, its method is found first in this example.

You can inspect the method resolution order with:

```python
print(CarTruck.mro())
```

**Key takeaway:** Inheritance supports code reuse and specialization. Method overriding changes inherited behaviour, `super()` can call parent implementations, and Python's MRO determines how methods are resolved in multiple inheritance.