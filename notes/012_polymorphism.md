
# Python Polymorphism

## 1. What Is Polymorphism?

The word **Polymorphism** comes from two words:

- **Poly** means many.
- **Morphs** means forms.

Therefore, polymorphism means **many forms**.

In programming, polymorphism allows the same operation, interface, or method name to behave differently depending on the object or the data involved.

### Real-Life Example

Imagine a person:

- With parents, the person may behave respectfully.
- With friends, the person may behave casually.
- At work, the person may behave professionally.

The same person behaves differently in different situations.

This is a simple real-life analogy for polymorphism.

### Example: The `+` Operator

Python's `+` operator behaves differently depending on the operands.

```python
# Integer addition
print(10 + 20)

# String concatenation
print("Hello " + "Python")

# List concatenation
print([1, 2] + [3, 4])
```

**Output:**

```text
30
Hello Python
[1, 2, 3, 4]
```

The same operator performs different operations depending on the operand types.

---

## 2. Types of Polymorphism in Python

The main concepts covered in these notes are:

1. Duck typing
2. Overloading
   - Operator overloading
   - Method overloading
   - Constructor overloading
3. Overriding
   - Method overriding
   - Constructor overriding

---

## 3. Duck Typing Philosophy of Python

Python is a dynamically typed programming language. A variable can refer to objects of different types at different times, and Python determines the relevant behavior at runtime.

**Duck typing** means that we focus on what an object can do rather than requiring it to belong to a particular class.

The principle is commonly expressed as:

> If it walks like a duck and quacks like a duck, it must be a duck.

For example, if an object provides a `talk()` method, a function can call that method without needing to know the object's exact class.

### Example

```python
class Human:
    def talk(self):
        print("Hello!")


class Lion:
    def talk(self):
        print("Roar!")


class Tiger:
    def talk(self):
        print("Growl!")


class Elephant:
    def talk(self):
        print("Trumpet!")


def show(obj):
    obj.talk()


animals = [
    Human(),
    Lion(),
    Tiger(),
    Elephant()
]

for obj in animals:
    show(obj)
```

**Output:**

```text
Hello!
Roar!
Growl!
Trumpet!
```

### Explanation

- Each class provides a `talk()` method.
- The `show()` function accepts an object.
- It calls `obj.talk()` without checking the object's class.
- Each object's own implementation runs.

This is duck typing.

### What Happens If a Method Is Missing?

Suppose one class does not implement `talk()`:

```python
class Human:
    def talk(self):
        print("Hello!")


class Robot:
    def walk(self):
        print("Walking...")


def show(obj):
    obj.talk()


show(Human())
show(Robot())
```

The second call raises an `AttributeError` because `Robot` has no `talk()` method.

### Solution 1: Use `hasattr()`

The built-in `hasattr()` function checks whether an object has a named attribute.

```python
def show(obj):
    if hasattr(obj, "talk"):
        obj.talk()
    else:
        print("This object cannot talk.")


show(Human())
show(Robot())
```

**Output:**

```text
Hello!
This object cannot talk.
```

Syntax:

```python
hasattr(object, "attribute_name")
```

The attribute can be a variable, method, or another accessible attribute.

**Important:** `hasattr()` checks whether attribute lookup succeeds. It does not guarantee that the attribute is callable or that calling it will succeed.

A direct capability check can also be written as:

```python
if callable(getattr(obj, "talk", None)):
    obj.talk()
```

---

## 4. What Is Overloading?

Overloading means using the same operator or method name for different purposes, depending on the arguments or objects involved.

The topics commonly discussed under overloading are:

1. Operator overloading
2. Method overloading
3. Constructor overloading

Python supports operator overloading directly. However, it does not support traditional method or constructor overloading through multiple same-named definitions in the same class.

---

## 5. Operator Overloading

**Operator overloading** allows an operator to behave differently for different types of objects.

For example, `+` performs addition with numbers and concatenation with strings.

Python also allows us to define operator behavior for our own classes through special methods, sometimes called *magic methods* or *dunder methods*.

### Common Operator Methods

| Operator | Special Method |
|---|---|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `==` | `__eq__()` |
| `<` | `__lt__()` |
| `>` | `__gt__()` |

### Example: Overloading the `+` Operator

Suppose we want to add the prices of two books.

```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __add__(self, other):
        return self.price + other.price


book1 = Book("Python", 500)
book2 = Book("Django", 700)

print(book1 + book2)
```

**Output:**

```text
1200
```

### Explanation

When Python evaluates:

```python
book1 + book2
```

it uses the `__add__()` method defined by the class, subject to Python's operator-dispatch rules.

The method adds the two prices and returns the result.

**Important:** The example assumes that `other` is another compatible `Book` object. In a production-quality class, we would also handle unsupported operand types appropriately.

---

## 6. Method Overloading

Traditional method overloading means defining multiple methods with the same name but different parameter lists.

For example, in languages such as Java, we can define:

```text
test(name)
test(name, address)
```

Python does not support this style of method overloading using multiple same-named definitions in one class.

### Example

```python
class Demo:
    def test(self, name):
        print("Name:", name)

    def test(self, name, address):
        print("Name:", name)
        print("Address:", address)


obj = Demo()
obj.test("Shiv", "Pune")
```

**Output:**

```text
Name: Shiv
Address: Pune
```

The second `test()` definition replaces the first definition in the class namespace. Python does not retain both implementations as overloaded methods.

Calling `obj.test("Shiv")` raises a `TypeError` because the remaining method requires both arguments.

### Solution 1: Use Default Arguments

```python
class Demo:
    def test(self, name, address=None):
        if address is None:
            print("Name:", name)
        else:
            print("Name:", name)
            print("Address:", address)


obj = Demo()

obj.test("Shiv")
obj.test("Shiv", "Pune")
```

**Output:**

```text
Name: Shiv
Name: Shiv
Address: Pune
```

### Solution 2: Use `*args`

```python
class Demo:
    def test(self, *args):
        if len(args) == 1:
            print("Name:", args[0])

        elif len(args) == 2:
            print("Name:", args[0])
            print("Address:", args[1])

        else:
            print("Invalid number of arguments")


obj = Demo()

obj.test("Shiv")
obj.test("Shiv", "Pune")
```

These approaches allow one method to handle different argument combinations.

**Note:** Python also supports other approaches, including keyword arguments and, in suitable cases, `functools.singledispatchmethod`. The best choice depends on the required behavior.

---

## 7. Constructor Overloading

A constructor is commonly discussed as the method used to initialize an object. In ordinary Python classes, this is usually `__init__()`.

Python does not support traditional constructor overloading by defining multiple `__init__()` methods in the same class.

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Shiv", 85)
print(s1.name, s1.marks)
```

**Output:**

```text
Shiv 85
```

The second `__init__()` definition replaces the first one. Therefore, the one-argument initialization form is no longer available through that definition.

### Solution: Use Default Arguments

```python
class Student:
    def __init__(self, name, marks=None):
        self.name = name
        self.marks = marks


s1 = Student("Shiv")
s2 = Student("Rudra", 85)

print(s1.name, s1.marks)
print(s2.name, s2.marks)
```

**Output:**

```text
Shiv None
Rudra 85
```

Another option is to use class methods as alternative constructors.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def without_marks(cls, name):
        return cls(name, None)


s1 = Student("Shiv", 85)
s2 = Student.without_marks("Rudra")
```

Here, `without_marks()` provides an alternative way to create a `Student` object.

---

## 8. What Is Overriding?

**Overriding** occurs when a child class provides its own implementation of a method inherited from its parent class.

The child class can change or extend the inherited behavior to meet its requirements.

Overriding is associated with inheritance.

### 8.1 Method Overriding

### Example

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()
```

**Output:**

```text
Animal makes a sound
Dog barks
Cat meows
```

### Explanation

- `Animal` is the parent class.
- `Dog` and `Cat` are child classes.
- Both child classes override the inherited `sound()` method.
- Each object's method call produces behavior appropriate to its class.

### Calling the Parent Implementation with `super()`

Sometimes we want to extend the parent method rather than replace its behavior completely.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")


d = Dog()
d.sound()
```

**Output:**

```text
Animal makes a sound
Dog barks
```

`super()` lets us call the next implementation in the method resolution order, which commonly means the parent implementation in a simple inheritance example.

---

## 9. Constructor Overriding

Constructor overriding is commonly used to describe a child class defining its own `__init__()` method when the parent class also has one.

### Example

```python
class Parent:
    def __init__(self):
        print("Parent initializer")


class Child(Parent):
    def __init__(self):
        print("Child initializer")


obj = Child()
```

**Output:**

```text
Child initializer
```

The child's `__init__()` is used when the `Child` object is initialized. The parent's initializer is not automatically called when the child defines its own initializer.

### Calling the Parent Initializer with `super()`

```python
class Parent:
    def __init__(self):
        print("Parent initializer")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child initializer")


obj = Child()
```

**Output:**

```text
Parent initializer
Child initializer
```

Using `super().__init__()` allows the child initializer to invoke the parent initializer in this example.

**Important:** Unlike Java or some other languages, Python does not require a child class to define its own `__init__()`. If the child does not define one, it can inherit the parent's initializer.

---

## 10. Difference Between Overloading and Overriding

| Overloading | Overriding |
|---|---|
| Reuses an operator or method name for different operations or argument patterns | Replaces an inherited method implementation in a child class |
| Traditional method overloading is not supported through repeated definitions in a Python class | Method overriding is supported |
| Can often be approximated using default arguments or `*args` | Requires an inherited method that the child redefines |
| Operator overloading uses special methods such as `__add__()` | Method overriding uses inheritance and a matching method name |

---

## 11. Quick Revision

- **Polymorphism:** One interface or operation can have different behaviors.
- **Duck typing:** Focuses on what an object can do rather than its exact class.
- **Operator overloading:** Defines operator behavior for custom objects using special methods.
- **Method overloading:** Multiple same-named method definitions do not work as traditional overloads in Python; use flexible arguments or other suitable techniques.
- **Constructor overloading:** Multiple same-named `__init__()` definitions do not coexist as overloads; use optional arguments or alternative constructors.
- **Method overriding:** A child class supplies its own implementation of an inherited method.
- **Constructor overriding:** A child class defines its own `__init__()` instead of inheriting the parent's initializer.

---

## 12. Practice Questions

1. What does polymorphism mean?
2. How does the `+` operator behave differently for integers and strings?
3. What is duck typing in Python?
4. What is the purpose of `hasattr()`?
5. What is operator overloading?
6. Which special method is commonly used to overload `+`?
7. Does Python support traditional method overloading through multiple same-named definitions?
8. How can default arguments simulate different method signatures?
9. What is method overriding?
10. What is the purpose of `super()`?
11. Does a child class automatically call the parent's `__init__()` if it defines its own?
12. What is the difference between overloading and overriding?

### Practice Program

Create a parent class called `Shape` with an `area()` method.

Create two child classes:

1. `Rectangle`, with `length` and `width`.
2. `Circle`, with `radius`.

Override `area()` in both child classes to calculate the appropriate area.

Store one rectangle and one circle in a list, loop through the list, and call `area()` on each object to demonstrate polymorphism.
