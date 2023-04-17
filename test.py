from html_document_generator import HTMLDocumentGenerator, HTMLTagGenerator

# Define the content for the home page
header_content = '<h1>Welcome to Farmer\'s Farm</h1>'
nav_content = '<ul><li>Home</li><li>Contact</li></ul>'
main_content = '<p>Explore the freshest produce from our farm!</p>'
footer_content = '<p>Contact information: Email: info@farmersfarm.com, Phone: 123-456-7890</p>'

# Create an instance of HTMLDocumentGenerator for home page
home_doc_generator = HTMLDocumentGenerator()
home_doc_generator.set_attribute('head', 'title', 'Home | Farmer\'s Farm')
home_doc_generator.set_style('body { background-color: lightgreen; }')

# Generate the header tag for home page
header_tag = HTMLTagGenerator(tag_name='header', tag_content=header_content)
home_doc_generator.add_tag(header_tag)

# Generate the nav tag for home page
nav_tag = HTMLTagGenerator(tag_name='nav', tag_content=nav_content)
home_doc_generator.add_tag(nav_tag)

# Generate the main tag for home page
main_tag = HTMLTagGenerator(tag_name='main', tag_content=main_content)
home_doc_generator.add_tag(main_tag)

# Generate the footer tag for home page
footer_tag = HTMLTagGenerator(tag_name='footer', tag_content=footer_content)
home_doc_generator.add_tag(footer_tag)

# Define the content for the contact page
contact_header_content = '<h1>Contact Us</h1>'
contact_form_content = '<form action="/submit" method="post">' \
                       '<label for="name">Name:</label>' \
                       '<input type="text" id="name" name="name" required>' \
                       '<label for="email">Email:</label>' \
                       '<input type="email" id="email" name="email" required>' \
                       '<label for="message">Message:</label>' \
                       '<textarea id="message" name="message" required></textarea>' \
                       '<input type="submit" value="Submit">' \
                       '</form>'
contact_footer_content = '<p>Contact information: Email: info@farmersfarm.com, Phone: 123-456-7890</p>'

# Create an instance of HTMLDocumentGenerator for contact page
contact_doc_generator = HTMLDocumentGenerator()
contact_doc_generator.set_attribute('head', 'title', 'Contact | Farmer\'s Farm')
contact_doc_generator.set_style('body { background-color: lightblue; }')

# Generate the header tag for contact page
contact_header_tag = HTMLTagGenerator(tag_name='header', tag_content=contact_header_content)
contact_doc_generator.add_tag(contact_header_tag)

# Generate the nav tag for contact page
contact_nav_tag = HTMLTagGenerator(tag_name='nav', tag_content=nav_content)
contact_doc_generator.add_tag(contact_nav_tag)

# Generate the main tag for contact page
contact_main_tag = HTMLTagGenerator(tag_name='main', tag_content=contact_form_content)
contact_doc_generator.add_tag(contact_main_tag)

# Generate the footer tag for contact page
contact_footer_tag = HTMLTagGenerator(tag_name='footer', tag_content=contact_footer_content)
contact_doc_generator.add_tag(contact_footer_tag)


# Write the generated HTML document to an HTML file
with open('home.html', 'w') as file:
    file.write(home_doc_generator.generate_document())
    print('HTML file created successfully')
    file.close()

with open('contact.html', 'w') as file:
    file.write(contact_doc_generator.generate_document())
    print('HTML file created successfully')
    file.close()
