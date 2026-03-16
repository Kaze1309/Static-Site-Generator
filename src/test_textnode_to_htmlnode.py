from htmlnode import text_node_to_html_node
import unittest

from textnode import TextNode, TextType


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_node(self):
        node = TextNode("Some bold text", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Some bold text")

    def test_image_tag(self):
        node = TextNode("Mount Fuji", TextType.IMAGE, "www.jptourism.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "www.jptourism.com", "alt": "Mount Fuji"}
        )
