import unittest
from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://boot.dev")
        self.assertEqual(node, node2)

    def test_eq_different_text(self):
        node = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_different_text2(self):
        node = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text a", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_different_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Text A", TextType.BOLD, "http://boot.dev")
        self.assertEqual(repr(node), "TextNode(Text A, bold, http://boot.dev)")

    def test_repr_2(self):
        node = TextNode("Text A", TextType.ITALIC, "http://boot.dev")
        self.assertEqual(repr(node), "TextNode(Text A, italic, http://boot.dev)")

    def test_repr_none(self):
        node = TextNode("Text A", TextType.ITALIC)
        self.assertEqual(repr(node), "TextNode(Text A, italic, None)")


if __name__ == "__main__":
    unittest.main()
