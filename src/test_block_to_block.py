import unittest
from blocks import block_to_block_type, markdown_to_blocks

class TestBlockToBlock(unittest.TestCase):
    def test_block_to_block(self):
        md = """- this is\n- unordered list"""
        node = block_to_block_type(md)
        self.assertEqual(node, 'unordered_list')
    def test_block_to_block_heading(self):
        md = """# heading 1
        # heading 2"""
        node = block_to_block_type(md)
        self.assertEqual(node, 'heading')
    def test_block_to_block_paragraph(self):
        md = """just some random ass shit bro"""
        node = block_to_block_type(md)
        self.assertEqual(node, 'paragraph')
    def test_block_to_block_ordered_list(self):
        md = """1. yeah bitch\n2. naah bitch"""
        node = block_to_block_type(md)
        self.assertEqual(node, 'ordered_list')