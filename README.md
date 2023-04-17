## HTMLDocumentGenerator

The `HTMLDocumentGenerator` is a Python class that allows you to easily generate HTML documents with customizable tags and content. It provides a simple and intuitive way to create HTML documents for websites or other applications.

### Features
- Add HTML tags with custom tag names, attributes, and content
- Set attributes for the `<head>` tag, such as title, style, etc.
- Generate a complete HTML document with the `<!DOCTYPE>`, `<html>`, `<head>`, and `<body>` tags
- Generate a string representation of the HTML document
- NEW FEATURE: Write the generated HTML document to an HTML file using the `open` function

### Example Usage

```python
from html_document_generator import HTMLDocumentGenerator, HTMLTagGenerator

# Create an instance of HTMLDocumentGenerator
doc_generator = HTMLDocumentGenerator()
doc_generator.set_attribute('head', 'title', 'My Website')

# Generate the header tag
header_tag = HTMLTagGenerator(tag_name='header', tag_content='<h1>Welcome to My Website</h1>')
doc_generator.add_tag(header_tag)

# Generate the nav tag
nav_tag = HTMLTagGenerator(tag_name='nav', tag_content='<ul><li>Home</li><li>Contact</li></ul>')
doc_generator.add_tag(nav_tag)

# Generate the main tag
main_tag = HTMLTagGenerator(tag_name='main', tag_content='<p>Explore the content of my website!</p>')
doc_generator.add_tag(main_tag)

# Generate the footer tag
footer_tag = HTMLTagGenerator(tag_name='footer', tag_content='<p>Contact information: email@example.com, Phone: 123-456-7890</p>')
doc_generator.add_tag(footer_tag)

# Generate the complete HTML document
html_doc = doc_generator.generate_document()

# Write the generated HTML document to an HTML file
with open('index.html', 'w') as file:
    file.write(html_doc)

print('HTML file created successfully!')
```
Requirements
Python 3.6+
No external dependencies
License
This class is released under the MIT License.

Contributions
Contributions are welcome! Please feel free to open issues or submit pull requests to improve this class.

