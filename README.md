# HTMLTagGenerator
Simple Python HTML Tag Generator

# Explaination

In this updated version, we have added a new parameter tag_input_type to the __init__ method, which represents the type attribute for the <input> tag. The generate_tag method has been modified to handle the <input> tag separately based on the tag_name and tag_input_type values.

You can now create instances of the HTMLTagGenerator class for <input>, <div>, <a>, and <i> tags, and generate the corresponding HTML code by calling the generate_tag method with appropriate values for tag_name, tag_text, tag_attributes, and tag_input_type. Here are some examples:

# Demo
``
# Create an instance of the HTMLTagGenerator class for an <input> tag
input_tag = HTMLTagGenerator(tag_name='input', tag_attributes={'type': 'text', 'name': 'username'})

# Generate the HTML code for the <input> tag
input_tag_code = input_tag.generate_tag()

# Print the generated HTML code
print(input_tag_code)

# Create an instance of the HTMLTagGenerator class for a <div> tag
div_tag = HTMLTagGenerator(tag_name='div', tag_text='Hello, world!', tag_attributes={'class': 'container', 'id': 'my-div'})

# Generate the HTML code for the <div> tag
div_tag_code = div_tag.generate_tag()

# Print the generated HTML code
print(div_tag_code)

# Create an instance of the HTMLTagGenerator class for an <a> tag
a_tag = HTMLTagGenerator(tag_name='a', tag_text='Click me!', tag_attributes={'href': 'https://www.example.com'})

# Generate the HTML code for the <a> tag
a_tag_code = a_tag.generate_tag()

# Print the generated HTML code
print(a_tag_code)

# Create an instance of the HTMLTagGenerator class for an <i> tag
i_tag = HTMLTagGenerator(tag_name='i', tag_text='This is italic text!', tag_attributes={'class': 'italic-text'})

# Generate the HTML code for the <i> tag
i_tag_code = i_tag.generate_tag()

# Print the generated HTML code
print(i_tag_code)``
