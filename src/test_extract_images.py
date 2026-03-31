from htmlnode import extract_markdown_images, extract_markdown_links
import unittest

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) another one being ![second image](some link)",
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("second image", "some link")], matches)
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a link [to boot dev](https://www.bootdev.com)"
        )
        self.assertListEqual([("to boot dev", "https://www.bootdev.com")], matches)
    def test_extract_multiple_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    def test_no_links(self):
        matches = extract_markdown_links("This is text with nothing")
        self.assertListEqual([], matches)