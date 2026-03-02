from htmlnode import LeafNode, ParentNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode('p', "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>child</p></div>")
    def test_to_html_with_grandchildren(self):
        child_node = LeafNode('p', "child")
        parent_node = ParentNode('h1', [child_node])
        grandparent_node = ParentNode('div', [parent_node])
        self.assertEqual(grandparent_node.to_html(), "<div><h1><p>child</p></h1></div>")
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
    def test_to_html_with_children_props(self):
        child_node = LeafNode('p', "props test child", {'style':'color:black;'})
        parent_node = ParentNode('a', [child_node], {'href': 'https://boot.dev'})
        self.assertEqual(parent_node.to_html(), '<a href="https://boot.dev"><p style="color:black;">props test child</p></a>')
    def test_to_html_with_multiple_children(self):
        child_node_1 = LeafNode('p', 'child 1')
        child_node_2 = LeafNode('span', 'child 2')
        parent_node = ParentNode('div', [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), '<div><p>child 1</p><span>child 2</span></div>')

