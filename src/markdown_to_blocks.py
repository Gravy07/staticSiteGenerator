from enum import Enum
import re



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:  # all() checks to see if everything is True.
    lines = block.split("\n")  # splits each block into lines
    if re.match(r"^#{1,6} .+", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i +1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH



def md_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    final = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        final.append(block)
    return final
