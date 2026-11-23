import unittest
from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
