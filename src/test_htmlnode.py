import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode



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

    ## Parent Node to_html  ##  Ran short on time, look into more outlaying cases

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children_order(self):
        node = ParentNode("p", [
            LeafNode("b", "bold"),
            LeafNode(None, "plain"),
            LeafNode("i", "italic"),
        ])
        self.assertEqual(node.to_html(), "<p><b>bold</b>plain<i>italic</i></p>")

    def test_nested_parents(self):
        inner = ParentNode("span", [LeafNode("b", "deep")])
        outer = ParentNode("div", [inner])
        self.assertEqual(outer.to_html(), "<div><span><b>deep</b></span></div>")

    def test_mixed_children(self):
        node = ParentNode("div", [
            LeafNode(None, "text"),
            ParentNode("ul", [LeafNode("li", "one"), LeafNode("li", "two")]),
            LeafNode("p", "after"),
        ])
        self.assertEqual(
            node.to_html(),
            "<div>text<ul><li>one</li><li>two</li></ul><p>after</p></div>",
         )

    def test_no_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "x")]).to_html()

    def test_no_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_error_propagates_from_deep_child(self):
        bad = LeafNode("b", None)
        node = ParentNode("div", [ParentNode("span", [bad])])
        with self.assertRaises(ValueError):
            node.to_html()

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
