from enum import Enum
from htmlnode import HTMLNode
class BlockType(str, Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    line_by_line = markdown.split("\n\n")
    new_block = []
    for line in line_by_line:
        if line == "":
            continue
        new_block.append(line.strip())
    return new_block

def block_to_block_type(block):
    lines = block.split('\n')
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('-'):
        for line in lines:
            if not line.startswith('-'):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        typeof_block = block_to_block_type(block)
        if typeof_block == BlockType.HEADING:
            pass
        elif typeof_block == BlockType.ORDERED_LIST:
            pass
        elif typeof_block == BlockType.CODE:
            pass
        elif typeof_block == BlockType.UNORDERED_LIST:
            pass
        elif typeof_block == BlockType.QUOTE:
            pass
        else:
            para_tag = block.replace('\n', " ")
            paranode = HTMLNode('p', para_tag,)
        