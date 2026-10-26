import re



# Uses regex to extract alt text, and url from raw markdown text
def extract_md_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)  # I just used the given string of regex from boot.dev for this. TODO: try and break this down for understanding purposes
    return matches

def extract_md_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
