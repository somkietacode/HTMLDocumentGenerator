class HTMLTagGenerator:
    def __init__(self, tag_name, tag_text=None, tag_attributes=None, tag_input_type=None):
        self.tag_name = tag_name
        self.tag_text = tag_text
        self.tag_attributes = tag_attributes
        self.tag_input_type = tag_input_type

    def generate_tag(self):
        if self.tag_name == 'input':
            tag = '<{} type="{}"{}'.format(self.tag_name, self.tag_input_type, self._generate_attributes())
        else:
            tag = '<{}{}'.format(self.tag_name, self._generate_attributes())

        if self.tag_text:
            tag += '>{}<{}>'.format(self.tag_text, self.tag_name)
        else:
            tag += '>'

        return tag

    def _generate_attributes(self):
        attributes = ''

        if self.tag_attributes:
            for attr, value in self.tag_attributes.items():
                attributes += ' {}="{}"'.format(attr, value)

        return attributes
