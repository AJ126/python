
# Python OOP: Classes, Objects, Variables, Methods, and Constructors

## 1. What Is a Class?

In Python, almost everything is an object. A **class** is a blueprint or template used to create objects.

A class defines the properties (data) and behaviors (operations) that its objects can have.

### Real-Life Example

Think about building a house.

- **Blueprint:** Class
- **Actual house:** Object
- **House color, address, and number of rooms:** Attributes
- **Opening doors or switching on lights:** Behaviors

Using one blueprint, we can create multiple houses.

### Syntax

```python
class ClassName:
    # Attributes and methods
    pass
```

### Example

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Shiv", 85)
s2 = Student("Rudra", 90)

s1.show()
s2.show()
```

**Output:**

```text
Name: Shiv
Marks: 85
Name: Rudra
Marks: 90
```

Both objects belong to the same class, but they have different attribute values.

---

## 2. What Is an Object?

An **object** is an instance of a class. We can create multiple objects from the same class.

### Syntax

```python
reference_variable = ClassName()
```

### Example

```python
class Student:
    pass


s1 = Student()
s2 = Student()

print(s1)
print(s2)
```

Here, `s1` and `s2` refer to two separate `Student` objects.

**Note:** An object is an instance of a class. A class defines how its instances are created and what behavior they support.

---

## 3. What Is a Reference Variable?

A **reference variable** is a variable that refers to an object.

We use it to access an object's attributes and methods.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


s1 = Student("Shiv")

s1.show()
print(s1.name)
```

**Output:**

```text
Shiv
Shiv
```

Here, `s1` refers to the `Student` object.

**Important:** Python variables hold references to objects; assigning an object to another variable does not automatically create a new copy of that object.

```python
s1 = Student("Shiv")
s2 = s1

s2.name = "Rudra"

print(s1.name)
```

**Output:**

```text
Rudra
```

Both variables refer to the same object.

---

## 4. Variables in a Class

In Python classes, we commonly discuss three kinds of variables:

1. Instance variables (object-level variables)
2. Class variables (class-level or static variables)
3. Local variables (method-level variables)

### 4.1 Instance Variables

If an attribute stores data specific to an individual object, it is called an **instance variable**.

Different objects can have different values for their instance variables.

#### Where Can We Declare Instance Variables?

**A. Inside the constructor using `self`**

```python
class Student:
    def __init__(self):
        self.name = "Shiv"
        self.marks = 85


s1 = Student()
print(s1.name)
print(s1.marks)
```

**Output:**

```text
Shiv
85
```

When an object is initialized, the assignments to `self.name` and `self.marks` create or update attributes on that object.

**B. Inside an instance method using `self`**

```python
class Student:
    def __init__(self):
        self.name = "Shiv"

    def add_address(self):
        self.address = "Kailash Parvat"


s1 = Student()
s1.add_address()

print(s1.name)
print(s1.address)
```

**Output:**

```text
Shiv
Kailash Parvat
```

The `address` attribute is created when `add_address()` executes.

If we do not call that method, the attribute will not be created by this code.

**C. Outside the class using an object reference**

```python
class Student:
    def __init__(self):
        self.name = "Shiv"


s1 = Student()
s1.phone = "1234567890"

print(s1.name)
print(s1.phone)
```

The `phone` attribute is added to `s1` only. Other `Student` objects do not automatically receive it.

### Important Point

Each object has its own instance attributes. The objects may have attributes with the same names, but those attributes can hold different values.

---

### 4.2 Class Variables (Static Variables)

A **class variable** is declared directly inside the class but outside its methods.

It is associated with the class and can be accessed through the class itself or through an instance.

```python
class Student:
    school = "ABC School"


s1 = Student()
s2 = Student()

print(Student.school)
print(s1.school)
print(s2.school)
```

**Output:**

```text
ABC School
ABC School
ABC School
```

Class variables are useful for information shared by instances, such as a school name or a common configuration value.

#### Class Variable vs. Instance Variable

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


s1 = Student("Shiv")
s2 = Student("Rudra")

print(s1.name)
print(s2.name)
print(s1.school)
print(s2.school)
```

**Output:**

```text
Shiv
Rudra
ABC School
ABC School
```

- `name` is an instance variable.
- `school` is a class variable.

**Important:** If you assign `s1.school = "XYZ School"`, you normally create or update an instance attribute that shadows the class variable for `s1`. You do not change the class variable itself.

To update the shared class variable, use:

```python
Student.school = "XYZ School"
```

---

### 4.3 Local Variables

A **local variable** is created inside a function or method and is used for temporary calculations or operations.

```python
class Student:
    def __init__(self):
        self.name = "Shiv"

    def add(self):
        address = "Kailash Parvat"
        self.address = address

        print(address)


s1 = Student()
s1.add()

print(s1.name)
print(s1.address)
```

**Output:**

```text
Kailash Parvat
Shiv
Kailash Parvat
```

Here:

- `address` is a local variable.
- `self.address` is an instance variable.

The local name `address` cannot normally be accessed outside the method where it is defined. The value assigned to `self.address`, however, remains available through the object.

**Note:** Python local variables are not necessarily destroyed immediately when a method returns if their values remain referenced elsewhere. The important point is that the local name belongs to that function's local scope.

---

## 5. Methods in Python Classes

A method is a function defined inside a class.

Python commonly uses three method types:

1. Instance methods
2. Class methods
3. Static methods

### 5.1 Instance Methods

An **instance method** operates on an individual object. Its first parameter is conventionally named `self`.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student name:", self.name)


s1 = Student("Shiv")
s1.show()
```

**Output:**

```text
Student name: Shiv
```

Here, `self.name` accesses the current object's `name` attribute.

#### Calling Instance Methods

From outside the class:

```python
s1.show()
```

From another instance method in the same object:

```python
self.show()
```

Python supplies the instance automatically when calling a bound instance method through an object.

**Note:** `self` is a conventional parameter name, not a reserved keyword. Using `self` is the standard Python practice.

---

### 5.2 Class Methods

A **class method** receives the class itself as its first argument, conventionally named `cls`.

Declare a class method using the `@classmethod` decorator.

Class methods are useful when an operation needs to read or modify class-level data or create objects through an alternative constructor.

```python
class Animal:
    legs = 4

    @classmethod
    def walk(cls, name):
        print("{} walks with {} legs.".format(name, cls.legs))


Animal.walk("Dog")
Animal.walk("Cat")
```

**Output:**

```text
Dog walks with 4 legs.
Cat walks with 4 legs.
```

Here:

- `@classmethod` declares a class method.
- `cls` refers to the class.
- `cls.legs` accesses the class variable.

You can call a class method using the class or an instance:

```python
Animal.walk("Dog")

animal = Animal()
animal.walk("Cat")
```

The class is passed automatically as `cls` in both cases.

---

### 5.3 Static Methods

A **static method** is a function placed inside a class because it is logically related to that class, but it does not automatically receive an instance or class argument.

Declare it using `@staticmethod`.

```python
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y


print(Calculator.add(10, 20))

calc = Calculator()
print(calc.add(5, 3))
```

**Output:**

```text
30
8
```

A static method is useful for general utility operations associated with a class.

It does not receive `self` or `cls` automatically.

---

## 6. Difference Between Instance, Class, and Static Methods

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None required | `@classmethod` | `@staticmethod` |
| First parameter | Conventionally `self` | Conventionally `cls` | No automatic first parameter |
| Receives instance automatically | Yes | No | No |
| Receives class automatically | Through `type(self)` if needed | Yes | No |
| Typical use | Work with instance attributes | Work with class-level state or alternative constructors | Utility operations |

---

## 7. What Is `self`?

`self` refers to the current instance when an instance method is called.

It allows us to access the instance's attributes and other instance methods.

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


s1 = Student("Shiv")
s2 = Student("Rudra")

s1.show()
s2.show()
```

**Output:**

```text
Shiv
Rudra
```

When `s1.show()` is called, `self` refers to `s1`. When `s2.show()` is called, `self` refers to `s2`.

### Important Points About `self`

- `self` is not a Python keyword.
- It is the conventional name for the first parameter of an instance method.
- It allows an instance method to access the current object's attributes.
- It is not used as the automatic first parameter of a class method or static method.

---

## 8. What Is a Constructor?

In beginner-level Python OOP, `__init__()` is commonly called the constructor. More precisely, it is the **initializer**: Python calls it to initialize a newly created instance.

### Example

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Shiv", 85)
s1.show()
```

**Output:**

```text
Name: Shiv
Marks: 85
```

### Important Points

1. The initializer's name is `__init__`.
2. It is called automatically as part of normal object creation.
3. Its first parameter is conventionally `self`.
4. It is commonly used to initialize instance attributes.
5. It is called once per normal initialization of an object, not once per class.
6. An explicit `__init__()` is optional. If no initializer is defined, the inherited initialization behavior is used; for a simple class, this usually means no extra initialization work.
7. `__init__()` must return `None`.

### Does Python Create a Default Constructor?

Python does not insert a literal `__init__` method into every class. When a class does not define one, normal inherited initialization behavior is used.

### `__new__()` vs. `__init__()`

- `__new__()` creates and returns the instance.
- `__init__()` initializes an already-created instance.

For ordinary beginner programs, you will usually work with `__init__()`.

---

## 9. Passing an Object from One Class to Another

An object created from one class can be passed as an argument to a method belonging to another class.

```python
class Demo:
    def __init__(self):
        self.name = "Shiv"

    def add(self):
        self.address = "Kailash Parvat"
        print("Demo object:", self)


class Test:
    def show(self, data):
        data.address = "Kailash Parvat"
        print("Received object:", data)


d = Demo()
t = Test()

t.show(d)

print(d.address)
```

**Output:** The two printed object representations refer to the same `Demo` object, followed by:

```text
Kailash Parvat
```

### Explanation

- `d` refers to a `Demo` object.
- `t.show(d)` passes that object to the `show()` method.
- Inside `show()`, `data` refers to the same object as `d`.
- Assigning `data.address` therefore adds an attribute to the object referred to by `d`.

**Important:** The parameter name does not have to be `data`. It could be `obj`, `demo_obj`, or another valid variable name.

---

## 10. Inner Classes (Nested Classes)

A class declared inside another class is called a **nested class** or **inner class**.

Nested classes can be useful when a class is conceptually grouped inside another class.

For example, an `Engine` can be modeled as a nested class inside `Car`.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = self.Engine()

    def show(self):
        print("Car brand:", self.brand)
        self.engine.start()

    class Engine:
        def start(self):
            print("Engine started.")


car = Car("Toyota")
car.show()
```

**Output:**

```text
Car brand: Toyota
Engine started.
```

### Explanation

- `Engine` is defined inside `Car`.
- `Car.Engine` can be used to refer to the nested class.
- `self.engine` is an instance attribute containing an `Engine` object.
- The code explicitly creates the engine object in the `Car` initializer.

**Important:** A nested class does not automatically require an instance of the outer class to exist. Nesting mainly organizes related class definitions; any lifecycle dependency must be implemented explicitly.

---

## 11. Quick Revision

| Concept | Meaning |
|---|---|
| Class | Blueprint for creating objects |
| Object | An instance of a class |
| Reference variable | A variable that refers to an object |
| Instance variable | Data associated with an individual instance |
| Class variable | Data associated with the class |
| Local variable | A name used in a function or method's local scope |
| Instance method | A method that receives the current instance as `self` |
| Class method | A method that receives the class as `cls` |
| Static method | A method that receives no automatic instance or class argument |
| `self` | Conventional reference to the current instance |
| `cls` | Conventional reference to the current class |
| `__init__()` | Initializer called during normal instance creation |
| Nested class | A class defined inside another class |

---

## 12. Practice Questions

1. What is a class in Python?
2. What is the difference between a class and an object?
3. What is a reference variable?
4. What is the difference between an instance variable and a class variable?
5. How can we create an instance variable inside a method?
6. What is a local variable?
7. What is the purpose of `self`?
8. What is the difference between `self` and `cls`?
9. What is the purpose of `@classmethod`?
10. What is the purpose of `@staticmethod`?
11. What is the difference between `__new__()` and `__init__()`?
12. What is a nested class?
13. What happens when two variables refer to the same object?

### Practice Program

Create a `Student` class with the following requirements:

1. A class variable named `school`.
2. Instance variables named `name` and `marks`.
3. An instance method named `show_details()`.
4. A class method named `change_school()` that updates the school name.
5. A static method named `is_passed(marks)` that returns `True` when marks are at least 40 and `False` otherwise.
6. Create two student objects and demonstrate how instance variables can differ while the class variable is shared.
