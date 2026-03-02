import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "What is up beyotch", "h1")
        node2 = HTMLNode("p", "What is up beyotch", "h1")
        node3 = HTMLNode("h3", "Nigga pls", "h2")
        node_res = node.prop_to_html()
        node2_res = node2.prop_to_html()
        self.assertEqual(node_res, node2_res)

if __name__ == "__main__":
    unittest.main()
