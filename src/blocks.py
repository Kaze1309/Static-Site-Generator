
def markdown_to_blocks(markdown):
    line_by_line = markdown.split("\n\n")
    new_block = []
    for line in line_by_line:
        if line == "":
            continue
        new_block.append(line.strip())
    return new_block