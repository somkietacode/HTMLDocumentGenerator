class HTMLTagGenerator:
    def __init__(self, tag_name='', tag_content='', tag_attributes=None):
        self.tag_name = tag_name
        self.tag_content = tag_content
        self.tag_attributes = tag_attributes

    def generate_tag(self):
        attributes = ''
        if self.tag_attributes:
            for attr_name, attr_value in self.tag_attributes.items():
                attributes += f' {attr_name}="{attr_value}"'
        tag = f'<{self.tag_name}{attributes}>{self.tag_content}</{self.tag_name}>\n'
        return tag

    def set_attribute(self, attribute_name, attribute_value):
        if not self.tag_attributes:
            self.tag_attributes = {}
        self.tag_attributes[attribute_name] = attribute_value


class HTMLDocumentGenerator:
    def __init__(self, style=''):
        self.tags = []
        self.style = style

    def add_tag(self, html_tag):
        self.tags.append(html_tag)

    def generate_document(self):
        doc = "<!DOCTYPE html>\n<html>\n<head>\n"
        doc += f"<style>{self.style}</style>\n"
        doc += "</head>\n<body>\n"
        for tag in self.tags:
            doc += tag.generate_tag()
        doc += "</body>\n</html>"
        return doc

    def set_style(self, style):
        self.style = style

    def set_attribute(self, tag_name, attribute_name, attribute_value):
        for tag in self.tags:
            if tag.tag_name == tag_name:
                tag.set_attribute(attribute_name, attribute_value)

    def select_element(self, tag_name):
        selected_tags = []
        for tag in self.tags:
            if tag.tag_name == tag_name:
                selected_tags.append(tag)
        return selected_tags

    def add_child_element(self, tag_name, html_tag, position='end'):
        selected_tags = self.select_element(tag_name)
        for tag in selected_tags:
            if position == 'end':
                tag.tag_content += html_tag.generate_tag()
            elif position == 'start':
                tag.tag_content = html_tag.generate_tag() + tag.tag_content
