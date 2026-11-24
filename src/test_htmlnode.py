import unittest
from htmlnode import HTMLNode, LeafNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
         node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
         self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("h1", "Test Heading", {"a": "one", "b": "two", "c": "three"})
        self.assertEqual(node.to_html(), '<h1 a="one" b="two" c="three">Test Heading</h1>')


if __name__ == "__main__":
    unittest.main()
