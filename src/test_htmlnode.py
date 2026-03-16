import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("h1",
                         "Something", 
                         "p", 
                         {'class': "my-h1", 'href': "www.tootdev.com"})
                         
        self.assertEqual(node1.prop_to_html(), ' class="my-h1" href="www.tootdev.com"')
    def test_single_value(self):
        node1 = HTMLNode("h1",
                         "Something", 
                         "p", 
                         {'class': "my-h1", 'href': "www.tootdev.com"})
        self.assertEqual(node1.tag, "h1")
    def test_repr(self):
        node1 = HTMLNode("h1",
                         "Something", 
                         "p", 
                         {'class': "my-h1"})
        self.assertEqual(node1.__repr__(), "HTMLNode(h1, Something, p, {'class': 'my-h1'})")
if __name__ == "__main__":
    unittest.main()
