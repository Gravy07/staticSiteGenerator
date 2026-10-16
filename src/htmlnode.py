class HTMLNode:
    def __init__(self,
        tag: str | None = None,  # HTML tag name ("p", "a", "h1"...)
        value: str | None = None,  # The text inside a paragraph
        children: list["HTMLNode"] | None = None,  # A list of HTMLNode objects
        props: dict[str, str] | None = None # The attributes of the HTML tag (<a>) {"href": "http://www.boot.dev"}
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        formated_lst = []  # sets up .join() method
        for key, value in self.props.items():  # Iterates over props
            formated_element = f'{key}="{value}"'
            formated_lst.append(formated_element)  # appends each formated k, v pair to list
        return " " + " ".join(formated_lst)  # Adds whitespace before each pair before joining default space wiht " " +

    def __repr__(self):
        return f'HTMLNode({repr(self.tag)}, {repr(self.value)}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str | None, props: dict[str, str]|None = None):
            super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'  # Expected <a href="website">Text Here</a>

    def __repr__(self):
        return f'LeafNode({repr(self.tag)}, {repr(self.value)}, {self.props})'
