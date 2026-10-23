
# Regular Expressions in Python

## 1. What Are Regular Expressions?

A **Regular Expression (Regex)** is a sequence of characters used to describe a particular pattern in text.

In simple words, if we want to identify strings that follow a specific format or pattern, we can use Regular Expressions.

**Examples:**
1. Finding mobile numbers in text.
2. Validating email addresses.
3. Searching for a particular word in a document.
4. Finding digits, alphabets, or special characters in a string.

### Applications of Regular Expressions

1. **Validation:** Validating mobile numbers, email addresses, passwords, etc.
2. **Pattern matching:** Searching text using tools such as Ctrl+F and Unix `grep`.
3. **Text processing:** Finding, replacing, or extracting information from text.
4. **Compilers and interpreters:** Recognizing tokens such as identifiers and numbers.
5. **Communication protocols:** Validating text formats used in protocol messages.

> Note: Regular expressions can help validate text formats used in protocols, but they do not implement protocols such as TCP/IP or UDP themselves.

---

## 2. Python `re` Module

Python provides the built-in `re` module to work with Regular Expressions.

```python
import re
```

The `re` module provides functions such as:

- `compile()`
- `match()`
- `fullmatch()`
- `search()`
- `findall()`
- `finditer()`
- `sub()`
- `subn()`
- `split()`

## 3. `compile()` Function

The `compile()` function compiles a regular expression pattern into a reusable pattern object.

### Syntax

```python
pattern = re.compile("ab")
```

### Example

```python
import re

pattern = re.compile("ab")

print(pattern)
```

The compiled pattern can be reused to search different strings.

It is especially useful when the same pattern is needed multiple times.

---

## 4. `finditer()` Function

The `finditer()` function returns an iterator that produces a Match object for every non-overlapping match.

### Example

```python
import re

pattern = re.compile("ab")
matcher = pattern.finditer("abaababa")

for match in matcher:
    print(match.group(), match.start(), match.end())
```

### Output

```text
ab 0 2
ab 3 5
ab 5 7
```

### Important Match Object Methods

| Method | Description |
|---|---|
| `start()` | Returns the starting index of the match. |
| `end()` | Returns the index immediately after the match. |
| `group()` | Returns the matched text. |

**Remember:** Python string indexes start from `0`, and `end()` is exclusive.

For example, if `"ab"` is found at indexes `0` and `1`, `start()` returns `0` and `end()` returns `2`.

---

## 5. Character Classes

Character classes specify which characters are allowed at a particular position.

| Pattern | Meaning | Example matches |
|---|---|---|
| `[abc]` | Either `a`, `b`, or `c` | `a`, `b`, `c` |
| `[^abc]` | Any character except `a`, `b`, or `c` | `d`, `x`, `1` |
| `[a-z]` | Any lowercase ASCII letter | `a`, `m`, `z` |
| `[A-Z]` | Any uppercase ASCII letter | `A`, `M`, `Z` |
| `[a-zA-Z]` | Any uppercase or lowercase ASCII letter | `A`, `b` |
| `[0-9]` | Any digit from `0` to `9` | `0`, `5`, `9` |
| `[a-zA-Z0-9]` | Any ASCII letter or digit | `a`, `Z`, `7` |
| `[^a-zA-Z0-9]` | Any character outside those ASCII letters and digits | `@`, `#`, `!` |

### Example

```python
import re

text = "Python123@"

print(re.findall("[a-z]", text))
print(re.findall("[A-Z]", text))
print(re.findall("[0-9]", text))
print(re.findall("[^a-zA-Z0-9]", text))
```

### Output

```text
['y', 't', 'h', 'o', 'n']
['P']
['1', '2', '3']
['@']
```

---

## 6. Predefined Character Classes

Python provides shorthand patterns for commonly used character groups.

| Pattern | Meaning |
|---|---|
| `\s` | A whitespace character, such as a space, tab, or newline |
| `\S` | Any non-whitespace character |
| `\d` | A Unicode decimal digit |
| `\D` | Any character that is not a decimal digit |
| `\w` | A Unicode word character, including letters, digits, and underscore |
| `\W` | Any character that is not a word character |
| `.` | Any character except a newline by default |

**Important:** In Python, `\w` includes underscore (`_`) and Unicode letters. It is not limited to `[a-zA-Z0-9]`.

### Example

```python
import re

text = "Hello_123 @ Python"

print(re.findall(r"\d", text))
print(re.findall(r"\w+", text))
print(re.findall(r"\s", text))
print(re.findall(r"\W", text))
```

### Output

```text
['1', '2', '3']
['Hello_123', 'Python']
[' ', ' ', ' ']
[' ', '@', ' ']
```

### Why Use `r` Before a Pattern?

Use raw strings such as `r"\d+"` when writing regex patterns containing backslashes.

```python
pattern = r"\d+"
```

Raw strings make regex patterns easier to read because Python does not process most backslash escapes first.

---

## 7. Quantifiers

Quantifiers specify how many times a character or pattern may occur.

| Pattern | Meaning |
|---|---|
| `a` | Exactly one `a` |
| `a+` | One or more occurrences of `a` |
| `a*` | Zero or more occurrences of `a` |
| `a?` | Zero or one occurrence of `a` |
| `a{3}` | Exactly three occurrences of `a` |
| `a{2,4}` | Between two and four occurrences of `a` |

### Example

```python
import re

text = "a aa aaa aaaa"

print(re.findall(r"a+", text))
print(re.findall(r"a{2,3}", text))
```

### Output

```text
['a', 'aa', 'aaa', 'aaaa']
['aa', 'aaa', 'aaa']
```

The second pattern finds non-overlapping matches of two or three `a` characters.

**Remember:**
- `+` means at least one.
- `*` includes zero occurrences.
- `?` means optional.
- `{m,n}` specifies a minimum and maximum.

---

## 8. Important Functions of the `re` Module

### 8.1 `match()`

Checks for a match only at the beginning of the string.

If the pattern matches, it returns a Match object. Otherwise, it returns `None`.

```python
import re

print(re.match(r"Hello", "Hello Python"))
print(re.match(r"Python", "Hello Python"))
```

The first call returns a Match object; the second returns `None`.

### 8.2 `fullmatch()`

Checks whether the entire string matches the pattern.

```python
import re

print(re.fullmatch(r"\d+", "12345"))
print(re.fullmatch(r"\d+", "123abc"))
```

The first call returns a Match object; the second returns `None`.

Use `fullmatch()` when the entire input must follow a specified format.

### 8.3 `search()`

Searches anywhere in the string and returns the first match.

```python
import re

result = re.search(r"\d+", "My age is 25")

if result:
    print(result.group())
```

Output:

```text
25
```

### 8.4 `findall()`

Finds all non-overlapping matches and returns them in a list.

```python
import re

result = re.findall(r"\d+", "10 apples and 25 oranges")

print(result)
```

Output:

```text
['10', '25']
```

When the pattern contains capturing groups, `findall()` may return strings or tuples of captured groups rather than the entire matched text.

### 8.5 `finditer()`

Returns an iterator that yields a Match object for each non-overlapping match.

```python
import re

for match in re.finditer(r"\d+", "Age 25, score 90"):
    print(match.group(), match.start(), match.end())
```

Output:

```text
25 4 6
90 14 16
```

Use `finditer()` when you need both the matched text and its position.

### 8.6 `sub()`

The name `sub` means substitution.

It replaces every non-overlapping match with the specified replacement.

**Syntax:**

```python
re.sub(pattern, replacement, target_string)
```

Example:

```python
import re

text = "My phone number is 9876543210"

result = re.sub(r"\d", "*", text)

print(result)
```

Output:

```text
My phone number is **********
```

### 8.7 `subn()`

Works like `sub()`, but also returns the number of replacements.

It returns a tuple containing:

1. The resulting string.
2. The number of substitutions performed.

```python
import re

text = "a1b2c3"

result = re.subn(r"\d", "*", text)

print(result)
```

Output:

```text
('a*b*c*', 3)
```

### 8.8 `split()`

Splits a string wherever the regex pattern matches and returns a list.

```python
import re

text = "apple,banana;orange mango"

result = re.split(r"[,; ]+", text)

print(result)
```

Output:

```text
['apple', 'banana', 'orange', 'mango']
```

The pattern `[,; ]+` matches one or more commas, semicolons, or spaces.

### 8.9 `compile()`

Creates a reusable compiled pattern object.

```python
import re

pattern = re.compile(r"\d+")

print(pattern.findall("10 apples and 25 oranges"))
print(pattern.search("Age 30").group())
```

Output:

```text
['10', '25']
30
```

---

## 9. Difference Between Important Regex Functions

| Function | Purpose |
|---|---|
| `match()` | Checks at the beginning |
| `fullmatch()` | Checks the entire string |
| `search()` | Finds the first match anywhere |
| `findall()` | Returns all matches in a list |
| `finditer()` | Returns an iterator of Match objects |
| `sub()` | Replaces matches |
| `subn()` | Replaces matches and returns the replacement count |
| `split()` | Splits a string using a pattern |
| `compile()` | Creates a reusable pattern object |

---

## 10. Example: Validate a Mobile Number

Suppose we want to check whether a string contains exactly ten ASCII digits.

```python
import re

mobile = input("Enter a 10-digit mobile number: ")

if re.fullmatch(r"[0-9]{10}", mobile):
    print("Valid format")
else:
    print("Invalid format")
```

This checks the **format only**. It does not prove that the number is assigned, active, or belongs to a particular person.

---

## 11. Example: Find Email-Like Text

```python
import re

text = "Contact us at help@example.com or admin@test.org"

pattern = r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print(emails)
```

Output:

```text
['help@example.com', 'admin@test.org']
```

This is a simple pattern for learning and extracting email-like text. It is not a complete implementation of every valid email address format.

---

## 12. Quick Revision

- A regular expression describes a text pattern.
- Python provides regex functions through the `re` module.
- `compile()` creates a reusable pattern.
- Character classes specify allowed or excluded characters.
- Quantifiers specify the number of occurrences.
- `match()` checks the beginning; `fullmatch()` checks the whole string.
- `search()` finds the first match anywhere.
- `findall()` returns all matches in a list.
- `finditer()` provides Match objects with positions.
- `sub()` replaces matches; `subn()` also returns a count.
- `split()` separates text according to a pattern.

## 13. Practice Questions

1. What is a Regular Expression?
2. What is the purpose of Python's `re` module?
3. What is the difference between `match()`, `search()`, and `fullmatch()`?
4. What is the difference between `findall()` and `finditer()`?
5. What is the meaning of `\d`, `\w`, and `\s`?
6. Explain the difference between `*`, `+`, and `?`.
7. Write a program to find all digits in `"Python123 Django456"`.
8. Write a program to replace every space in a string with an underscore.
9. Write a program to split `"red,green;blue yellow"` using commas, semicolons, or spaces.
10. Write a program that accepts exactly ten ASCII digits using `fullmatch()`.

## 14. Practice Answers

```python
import re

# 7. Find all digits
print(re.findall(r"\d", "Python123 Django456"))

# 8. Replace spaces with underscores
print(re.sub(r" ", "_", "Learn Python Easily"))

# 9. Split using commas, semicolons, or spaces
print(re.split(r"[,; ]+", "red,green;blue yellow"))

# 10. Validate exactly ten ASCII digits
number = input("Enter number: ")
print(bool(re.fullmatch(r"[0-9]{10}", number)))
```
