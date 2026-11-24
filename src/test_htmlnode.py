import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_none_props(self):
        node = HTMLNode("p", "test text", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_empty_props(self):
        node = HTMLNode("p", "test text", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_one_prop(self):
        node = HTMLNode("p", "test text", None, {"a": "one"})
        self.assertEqual(node.props_to_html(), ' a="one"')

    def test_multiple_props(self):
            node = HTMLNode("p", "test text", None, {"a": "one", "b": "two", "c": "three"})
            self.assertEqual(node.props_to_html(), ' a="one" b="two" c="three"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
         node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
         self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("h1", "Test Heading", {"a": "one", "b": "two", "c": "three"})
        self.assertEqual(node.to_html(), '<h1 a="one" b="two" c="three">Test Heading</h1>')


class TestParentNode(unittest.TestCase):
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
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", [])
        self.assertEqual(parent_node.to_html(), "<p></p>")

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("p", "paragraph child")
        child_node3 = LeafNode("b", "bold child")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><p>paragraph child</p><b>bold child</b></div>")

    def test_to_html_with_grandchildren_from_multiple_children(self):
        grandchild_node1 = LeafNode("span", "span text")
        grandchild_node2 = LeafNode("p", "paragraph text")
        grandchild_node3 = LeafNode("b", "bold text")
        grandchild_node4 = LeafNode("i", "italic text")
        grandchild_node5 = LeafNode("h1", "heading text")
        grandchild_node6 = LeafNode("h2", "subheading text")
        child_node1 = ParentNode("head", [grandchild_node1])
        child_node2 = ParentNode("div", [grandchild_node2, grandchild_node3, grandchild_node4])
        child_node3 = ParentNode("article", [grandchild_node5, grandchild_node6])
        parent_node = ParentNode("body", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<body><head><span>span text</span></head><div><p>paragraph text</p><b>bold text</b><i>italic text</i></div><article><h1>heading text</h1><h2>subheading text</h2></article></body>"
        )


if __name__ == "__main__":
    unittest.main()
