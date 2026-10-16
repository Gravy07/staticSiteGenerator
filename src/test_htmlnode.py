import unittest
from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "webpage", "tar": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="webpage" tar="_blank"')

    def test_props_to_html_empty_value(self):
        node = HTMLNode(props={"href": "", "tar": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="" tar="_blank"')

    def test_props_to_html_empty_values(self):
        node = HTMLNode(props={"href": "", "tar": ""})
        self.assertEqual(node.props_to_html(), ' href="" tar=""')

    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr_full(self):
        child_node = HTMLNode()
        node = HTMLNode("h1", "Eat Slugs!", [child_node], {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode('h1', 'Eat Slugs!', [HTMLNode(None, None, None, None)], {'href': 'website', 'tar': '_blank'})""")

    def test_repr_no_children(self):
        node = HTMLNode("h1", "Eat Slugs!", None, {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode('h1', 'Eat Slugs!', None, {'href': 'website', 'tar': '_blank'})""")

    def test_repr_no_tag(self):
        child_node = HTMLNode()
        node = HTMLNode(None, "Eat Slugs!", [child_node], {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode(None, 'Eat Slugs!', [HTMLNode(None, None, None, None)], {'href': 'website', 'tar': '_blank'})""")

    def test_repr_no_value(self):
        child_node = HTMLNode()
        node = HTMLNode("h1", None, [child_node], {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode('h1', None, [HTMLNode(None, None, None, None)], {'href': 'website', 'tar': '_blank'})""")

    def test_repr_no_props(self):
        child_node = HTMLNode()
        node = HTMLNode("h1", "Eat Slugs!", [child_node], None)
        self.assertEqual(repr(node), """HTMLNode('h1', 'Eat Slugs!', [HTMLNode(None, None, None, None)], None)""")

    def test_repr_none(self):
        node = HTMLNode()
        self.assertEqual(repr(node), """HTMLNode(None, None, None, None)""")
