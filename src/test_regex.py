import unittest
from extractregex import extract_md_images, extract_md_links



class TestExtractRegex(unittest.TestCase):
    ### md_images ###

    def test_single_image(self):
        text = "Here is ![alt](https://example.com/a.png)"
        self.assertListEqual(
            extract_md_images(text),
            [("alt", "https://example.com/a.png")],
        )

    def test_multiple_images(self):
        text = "![a](http://g.ca/1.png) and ![b](http://g.ca/2.png)"
        self.assertListEqual(
            extract_md_images(text),
            [("a", "http://g.ca/1.png"), ("b", "http://g.ca/2.png")],
        )

    def test_image_empty_alt(self):
        text = "Here is ![](https://example.com/a.png)"
        self.assertListEqual(
            extract_md_images(text),
            [("", "https://example.com/a.png")],
        )

    def test_ignores_links(self):
        text = "A link [to boot dev](https://www.boot.dev)"
        self.assertListEqual(extract_md_images(text), [])

    def test_no_image_matches(self):
        self.assertListEqual(extract_md_images("plain text"), [])

    def test_no_str_image(self):
        self.assertListEqual(extract_md_images(""), [])

    ### md_links ###

    def test_single_link(self):
        text = "Here is [to boot dev](https://boot.dev)"
        self.assertListEqual(
            extract_md_links(text),
            [("to boot dev", "https://boot.dev")],
        )

    def test_multiple_links(self):
        text = "[google](http://www.google.ca) and [bootdev](http://boot.dev)"
        self.assertListEqual(
            extract_md_links(text),
            [("google", "http://www.google.ca"), ("bootdev", "http://boot.dev")],
        )

    def test_link_empty_alt(self):
        text = "Here is [](https://boot.dev)"
        self.assertListEqual(
            extract_md_links(text),
            [("", "https://boot.dev")],
        )

    def test_ignores_images(self):
        text = "An Image ![a](http://g.ca/1.png)"
        self.assertListEqual(extract_md_links(text), [])

    def test_no_link_matches(self):
        self.assertListEqual(extract_md_links("plain text"), [])

    ### both link and image edge cases ###

    def test_different_link(self):
        text = "![a](http://g.ca/1.png) and [bootdev](http://boot.dev)"
        self.assertListEqual(
            extract_md_links(text),
            [("bootdev", "http://boot.dev")],
        )

    def test_different_image(self):
        text = "![a](http://g.ca/1.png) and [bootdev](http://boot.dev)"
        self.assertListEqual(
            extract_md_images(text),
            [("a", "http://g.ca/1.png")],
        )
