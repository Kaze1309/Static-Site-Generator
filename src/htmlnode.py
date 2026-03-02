
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
    def __init__(self, tag=None,value= None,props = None):
        super().__init__(tag,value)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("No value to leaf node")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.prop_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
