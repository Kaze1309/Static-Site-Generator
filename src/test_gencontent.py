import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_gencontent_with_header(self):
        md = """# This is a header
        #This is definitely not a header
        ## this is h2 should not be considered"""
        self.assertEqual(extract_title(md), "# This is a header")
    def test_no_header(self):
        md = """no header here bitches"""
        with self.assertRaises(Exception):
            extract_title(md)