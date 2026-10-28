import unittest
from markdown_to_blocks import md_to_blocks, BlockType, block_to_block_type



class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is just a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_7(self):
        block = "####### This shouldnt be a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```    This is some code    ```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test__multi_quote(self):
        block = "> This is a quote\n> on multiple\n> lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test__multi_quote_fail(self):
        block = "> This is a quote\n on multiple\n> lines"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_fail(self):
        block = "- item 1\n- item 2\n-item3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. item 1\n2. item 2\n3. item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_fail(self):
        block = "1. item 1\n3. item 2\n4. item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = md_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiple(self):
        md = """
First paragraph

Second paragraph
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, ["First paragraph", "Second paragraph"])

    def test_markdown_to_blocks_single(self):
        md = """
Single paragraph
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, ["Single paragraph"])

    def test_markdown_to_blocks_multi_line_paragraph(self):
        md = """
Line one
Line two

Next paragraph
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, ["Line one\nLine two", "Next paragraph"])

    def test_markdown_to_blocks_heading_paragraph_list(self):
        md = """
# Heading

Paragraph with **bold** and _italic_.

- item 1
- item 2
- item 3
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, [
            "# Heading",
            "Paragraph with **bold** and _italic_.",
            "- item 1\n- item 2\n- item 3",
        ])

    def test_markdown_to_blocks_leading_trailing_whitespace(self):
        md = """

Hello


World


"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, ["Hello", "World"])

    def test_markdown_to_blocks_three_empty(self):
        md = """
a



b
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, ["a", "b"])

    def test_markdown_to_blocks_four_empty(self):
        md = """
a




b
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, ["a", "b"])

    def test_markdown_to_blocks_ordered_list_blockquote(self):
        md = """
> quote line 1
> quote line 2

1. one
2. two
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, ["> quote line 1\n> quote line 2", "1. one\n2. two"])

    def test_markdown_to_blocks_empty(self):
        md = """
"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_much_whitespace(self):
        md = """












"""
        blocks = md_to_blocks(md)
        self.assertEqual(blocks, [])
