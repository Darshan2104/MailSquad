def write_markdown_file(content, filename):
    """Writes the given content as a markdown file to the local directory."""
    with open(f"{filename}.md", "w") as f:
        f.write(content)