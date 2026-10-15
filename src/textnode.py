from enum import Enum



class TextType(Enum):
    PLAIN = "plain"  # Regular text, no styling
    BOLD = "bold"  # Markdown **bold**
    ITALIC = "italic"  # Markdown _italic_
    CODE = "code"  # Markdown ```code```
    LINKED = "linked"  # Markdown [anchor_text](url)
    IMAGES = "image"  # Markdown ![alt_text](url)

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: "TextNode"):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url # returns True if all of their properties are equal

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
