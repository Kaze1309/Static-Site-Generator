from textnode import TextNode, TextType
import re
class HTMLNode:
    def __init__(self,tag=None ,value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not implemented")

    def prop_to_html(self):
        ret_str = ""
        if self.props:
            for k, v in self.props.items():
                ret_str += f' {k}="{v}"'
        return ret_str

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag,value,props=None):
        super().__init__(tag,value,None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("No value to leaf node")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.prop_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tags provided")
        if self.children is None:
            raise ValueError("No children found")
        ret_str = ""
        for child in self.children:
           child_html =  child.to_html()
           ret_str  += f'{child_html}'

        return f'<{self.tag}{self.prop_to_html()}>{ret_str}</{self.tag}>'

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode('b',text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode('i',text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode('code',text_node.text)
        case TextType.LINK:
            return LeafNode('a',text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img',"", {'src':text_node.url, 'alt': text_node.text})
        case _:
            return Exception("Value not found")

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches