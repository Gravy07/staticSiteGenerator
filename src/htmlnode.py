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
        raise NotImplementedError("to_html method not implemented")

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
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
            super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'  # Expected <a href="website">Text Here</a>

    def __repr__(self):
        return f'LeafNode({repr(self.tag)}, {repr(self.value)}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have 1 or more children")
        child_html = []  # list start
        for child in self.children: #  iterate over children
            child_html.append(child.to_html())  # calls to_html on each child, adds to child_html list
        child_html_format = "".join(child_html)  # joins list seperator.function.iterator
        return f'<{self.tag}{self.props_to_html()}>{child_html_format}</{self.tag}>'  # final string parent nodes should be the first and last tags

    def __repr__(self):
        return f'ParentNode({repr(self.tag)}, {self.children}, {self.props})'
