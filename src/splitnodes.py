from textnode import TextNode, TextType
from extractregex import extract_md_images, extract_md_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_text_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:  # we only try to split "plain" type text objects (not bold, italic, ect)
            new_text_nodes.append(node)  # appends node to new list
            continue
        parts = node.text.split(delimiter)  # splits the text of current TextNode at the delimiter
        if len(parts) % 2 == 0:
            raise ValueError(f"Odd number of '{delimiter}' parts in {node.text}. Expected matching pairs")
        for i, part in enumerate(parts):  # https://docs.python.org/3/builtins/functions.html#enumerate (doc link for enumerate)
            if part == "":
                continue  # ensures white space cannot leak
            if i % 2 == 0:  # indexes at even addresses should be plain.
                new_text_nodes.append(TextNode(part, TextType.PLAIN))
            else:  # this handles remaining odd indexes which will be deliminated as text_type
                new_text_nodes.append(TextNode(part, text_type))
    return new_text_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_text_nodes = []
    for node in old_nodes:  # iterates over all nodes
        if node.text_type != TextType.PLAIN:  # Only split nodes whose type is ordinary text; preserve other node types unchanged.
            new_text_nodes.append(node)
            continue
        remaining = node.text  # remaining variable innitialized
        for alt, url in extract_md_images(remaining):  # running extract to get remaining (alt, url) tuple
            before, remaining = remaining.split(f"![{alt}]({url})", 1)  # tuple unpacking
            if before:
                new_text_nodes.append(TextNode(before, TextType.PLAIN))  # appends before text to a PLAIN TextNode
            new_text_nodes.append(TextNode(alt, TextType.IMAGE, url))  # creation of the IMAGE TextNode
        if remaining:
            new_text_nodes.append(TextNode(remaining, TextType.PLAIN))  # appending the after text to another PLAIN TextNode
    return new_text_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_text_nodes = []
    for node in old_nodes:  # iterates over all nodes
        if node.text_type != TextType.PLAIN:  # Only split nodes whose type is ordinary text; preserve other node types unchanged.
            new_text_nodes.append(node)
            continue
        remaining = node.text  # remaining variable innitialized
        for alt, url in extract_md_links(remaining):  # running extract to get remaining (alt, url) tuple
            before, remaining = remaining.split(f"[{alt}]({url})", 1)  # tuple unpacking
            if before:
                new_text_nodes.append(TextNode(before, TextType.PLAIN))  # appends before text to a PLAIN TextNode
            new_text_nodes.append(TextNode(alt, TextType.LINK, url))  # creation of the IMAGE TextNode
        if remaining:
            new_text_nodes.append(TextNode(remaining, TextType.PLAIN))  # appending the after text to another PLAIN TextNode
    return new_text_nodes
