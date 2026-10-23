
## 15. Regular Expressions in Web Scraping

**Web scraping** is the process of collecting information from web pages.

During web scraping, Regular Expressions can help us find specific patterns in the extracted text, such as email addresses, mobile numbers, dates, and other text formats.

### Example: Extract Email Addresses

```python
import re

text = """
Contact us at support@example.com
For help, email admin@test.org
"""

emails = re.findall(
    r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
    text
)

print(emails)
```

**Output:**
```text
['support@example.com', 'admin@test.org']
```

### Example: Extract 10-Digit Numbers

```python
import re

text = "Contact numbers: 9876543210, 9123456789"

numbers = re.findall(r"\b[0-9]{10}\b", text)

print(numbers)
```

**Output:**
```text
['9876543210', '9123456789']
```

### Important Note

Regular Expressions help identify patterns in text, but they do not collect web pages by themselves. A web-scraping tool such as `requests` or `BeautifulSoup` can retrieve or parse web content, and Regular Expressions can then extract matching information.

Always respect a website's terms of service, access restrictions, and applicable privacy rules when scraping data.
