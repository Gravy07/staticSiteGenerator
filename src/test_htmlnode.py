import unittest
from htmlnode import HTMLNode, LeafNode



class TestHTMLNode(unittest.TestCase):

    ### Props to HTML tests ###
    # HTML Node #

    def test_html_props_to_html(self):
        node = HTMLNode(props={"href": "webpage", "tar": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="webpage" tar="_blank"')

    def test_html_props_to_html_empty_value(self):
        node = HTMLNode(props={"href": "", "tar": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="" tar="_blank"')

    def test_html_props_to_html_empty_values(self):
        node = HTMLNode(props={"href": "", "tar": ""})
        self.assertEqual(node.props_to_html(), ' href="" tar=""')

    def test_html_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_html_props_to_html_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    # Leaf Node to_html #

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Eat Slugs!", {"href": "website", "tar": "_blank"})
        self.assertEqual(node.to_html(), '<a href="website" tar="_blank">Eat Slugs!</a>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Eat Slugs!", {"href": "website", "tar": "_blank"})
        self.assertEqual(node.to_html(), '<h1 href="website" tar="_blank">Eat Slugs!</h1>')

    def test_leaf_to_html_none_props(self):
        node = LeafNode("h1", "Eat Slugs!", None)
        self.assertEqual(node.to_html(), '<h1>Eat Slugs!</h1>')

    def test_leaf_to_html_empty_props(self):
        node = LeafNode("h1", "Eat Slugs!", {})
        self.assertEqual(node.to_html(), '<h1>Eat Slugs!</h1>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Eat Slugs!", None)
        self.assertEqual(node.to_html(), 'Eat Slugs!')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", None, {"href": "website", "tar": "_blank"})
        self.assertRaises(ValueError)

    ### repr tests ###
    # HTML Node #

    def test_html_repr_full(self):
        child_node = HTMLNode()
        node = HTMLNode("h1", "Eat Slugs!", [child_node], {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode('h1', 'Eat Slugs!', [HTMLNode(None, None, None, None)], {'href': 'website', 'tar': '_blank'})""")

    def test_html_repr_no_children(self):
        node = HTMLNode("h1", "Eat Slugs!", None, {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode('h1', 'Eat Slugs!', None, {'href': 'website', 'tar': '_blank'})""")

    def test_html_repr_no_tag(self):
        child_node = HTMLNode()
        node = HTMLNode(None, "Eat Slugs!", [child_node], {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode(None, 'Eat Slugs!', [HTMLNode(None, None, None, None)], {'href': 'website', 'tar': '_blank'})""")

    def test_html_repr_no_value(self):
        child_node = HTMLNode()
        node = HTMLNode("h1", None, [child_node], {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """HTMLNode('h1', None, [HTMLNode(None, None, None, None)], {'href': 'website', 'tar': '_blank'})""")

    def test_html_repr_no_props(self):
        child_node = HTMLNode()
        node = HTMLNode("h1", "Eat Slugs!", [child_node], None)
        self.assertEqual(repr(node), """HTMLNode('h1', 'Eat Slugs!', [HTMLNode(None, None, None, None)], None)""")

    def test_html_repr_none(self):
        node = HTMLNode()
        self.assertEqual(repr(node), """HTMLNode(None, None, None, None)""")

    # LeafNode #

    def test_leaf_repr_full(self):
        node = LeafNode("h1", "Eat Slugs!", {"href": "website", "tar": "_blank"})
        self.assertEqual(repr(node), """LeafNode('h1', 'Eat Slugs!', {'href': 'website', 'tar': '_blank'})""")

    def test_leaf_repr_no_props(self):
        node = LeafNode("h1", "Eat Slugs!", None)
        self.assertEqual(repr(node), """LeafNode('h1', 'Eat Slugs!', None)""")
