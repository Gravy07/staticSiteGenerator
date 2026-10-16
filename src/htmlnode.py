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
        formated_lst = []  # sets up .join()
        for key, value in self.props.items():  # Iterates over props
            formated_element = f'{key}="{value}"'
            formated_lst.append(formated_element)  # lists each k, v pair
        return " " + " ".join(formated_lst)  # Adds whitespace before joining each pair

    def __repr__(self):
        return f'HTMLNode({repr(self.tag)}, {repr(self.value)}, {self.children}, {self.props})'
