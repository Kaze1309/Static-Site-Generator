from htmlnode import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode


def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.PLAIN_TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        node_images = extract_markdown_images(node.text)
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        curr_text = node.text
        sections = []
        j = 1
        for image in node_images:
            section = curr_text.split(f"![{image[0]}]({image[1]})", 1)
            sections.append(section[0])
            sections.append(image)
            curr_text = section[1]
        if curr_text != None:
            sections.append(curr_text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.PLAIN_TEXT))
            else:
                split_nodes.append(
                    TextNode(sections[i][0], TextType.IMAGE, sections[i][1])
                )
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_links = extract_markdown_links(node.text)
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        curr_text = node.text
        sections = []
        for link in node_links:
            section = curr_text.split(f"[{link[0]}]({link[1]})", 1)
            sections.append(section[0])
            sections.append(link)
            curr_text = section[1]
        if curr_text != None:
            sections.append(curr_text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.PLAIN_TEXT))
            else:
                split_nodes.append(
                    TextNode(sections[i][0], TextType.LINK, sections[i][1])
                )
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.PLAIN_TEXT)
    new_nodes = []
    split_nodes = []
    italic = split_node_delimiter([node], '_', TextType.ITALIC_TEXT)
    bold = split_node_delimiter(italic, '**', TextType.BOLD_TEXT)
    code = split_node_delimiter(bold, "`", TextType.CODE_TEXT)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    new_nodes.extend(links)
    return new_nodes