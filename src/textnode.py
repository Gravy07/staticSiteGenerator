from enum import Enum
from htmlnode import HTMLNode, LeafNode



class TextType(Enum):
    PLAIN = "plain"  # Regular text, no styling
    BOLD = "bold"  # Markdown **bold**
    ITALIC = "italic"  # Markdown _italic_
    CODE = "code"  # Markdown ```code```
    LINK = "linked"  # Markdown [anchor_text](url)
    IMAGE = "image"  # Markdown ![alt_text](url)

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: "TextNode"):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url # returns True if all of their properties are equal

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: "TextNode") -> LeafNode:  # (self, tag: str | None, value: str, props: dict[str, str] | None = None):
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(tag=None, value=text_node.text, props=None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag='b', value=text_node.text, props=None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag='i', value=text_node.text, props=None)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag='code', value=text_node.text, props=None)
    elif text_node.text_type == TextType.LINK:
        assert text_node.url is not None
        return LeafNode(tag='a', value=text_node.text, props={'href':text_node.url})  # possible that url isnt being fed properly
    elif text_node.text_type == TextType.IMAGE:
        assert text_node.url is not None
        return LeafNode(tag='img', value="", props={'src':text_node.url, 'alt': text_node.text})
    else:
        raise Exception("type not supported")
