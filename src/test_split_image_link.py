import unittest
from splitter import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitImageLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is a test for links here this is [to boot dev](https://boot.dev) next one for nothing [nothing](www.youtube.com) yeah that's it",
            TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a test for links here this is ", TextType.PLAIN_TEXT),
                TextNode("to boot dev", TextType.LINK, "https://boot.dev"),
                TextNode(" next one for nothing ", TextType.PLAIN_TEXT),
                TextNode("nothing", TextType.LINK, "www.youtube.com"),
                TextNode(" yeah that's it", TextType.PLAIN_TEXT)
            ],
            new_nodes
        )
    def test_no_images_or_links(self):
        node = TextNode("This is normal text node", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is normal text node", TextType.PLAIN_TEXT),
            ],
            new_nodes
        )