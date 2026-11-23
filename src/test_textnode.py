import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("This is a text node", TextType.IMAGE, "image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, "image.png")
        self.assertEqual(node1, node2)

    def test_diff_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_diff_text(self):
        node1 = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is another text node", TextType.PLAIN)
        self.assertNotEqual(node1, node2)

    def test_url_and_no_url(self):
        node1 = TextNode("This is a text node", TextType.LINK, "test.com")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
