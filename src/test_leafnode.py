from htmlnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is leaf node")
        self.assertEqual(node.to_html(), "<p>This is leaf node</p>")
    
    def test_with_props_to_html_p(self):
        node = LeafNode("a", "This is a link", {'href':"https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">This is a link</a>')

