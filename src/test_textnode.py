import unittest
from textnode import TextNode, TextType, text_node_to_html_node



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

    ### Text Node to HTML Node function ###

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
        node = TextNode("This is a linked text node", TextType.LINK, "http://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a linked text node")
        self.assertEqual(html_node.props, {'href':'http://www.boot.dev'})

    def test_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "http://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {'src':'http://www.boot.dev', 'alt':'This is an image text node'})


if __name__ == "__main__":
    unittest.main()
