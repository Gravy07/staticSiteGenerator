import unittest

from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_all_types(self):
        text = "This is **bold** with _italic_, `code`, an ![image](https://imgur.com/a_b.png) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" with ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(", ", TextType.PLAIN),
                TextNode("code", TextType.CODE),
                TextNode(", an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://imgur.com/a_b.png"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_textnodes(text),
        )

    def test_only_plain(self):
        text = "This is plain text"
        self.assertListEqual(
            [
                TextNode("This is plain text", TextType.PLAIN),
            ],
            text_to_textnodes(text),
        )

    def test_bold_italic_code(self):
        text = "This is **bold** with _italic_, and `code`"
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" with ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(", and ", TextType.PLAIN),
                TextNode("code", TextType.CODE),
            ],
            text_to_textnodes(text),
        )

    def test_italic_image_link(self):
        text = "This is _italic_, an ![image](https://imgur.com/a_b.png) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(", an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://imgur.com/a_b.png"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_textnodes(text),
        )

    def test_multiple_bold_sections(self):
        text = "**first** and **second** bold sections"
        self.assertListEqual(
            [
                TextNode("first", TextType.BOLD),
                TextNode(" and ", TextType.PLAIN),
                TextNode("second", TextType.BOLD),
                TextNode(" bold sections", TextType.PLAIN),
            ],
            text_to_textnodes(text),
        )

    def test_leading_image_link_italic(self):
        text = "![image](https://imgur.com/a_b.png) _italic text_ and a [link](http://boot.dev)"
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://imgur.com/a_b.png"),
                TextNode(" ", TextType.PLAIN),
                TextNode("italic text", TextType.ITALIC),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "http://boot.dev"),
            ],
            text_to_textnodes(text),
        )



if __name__ == "__main__":
    unittest.main()
