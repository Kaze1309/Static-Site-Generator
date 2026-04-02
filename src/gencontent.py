import os
from blocks import markdown_to_htmlnode 
from htmlnode import HTMLNode

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line 
        raise Exception("no header found")

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path)
    markdown = f.read()
    t = open(template_path)
    template = t.read()
    html_node_string = markdown_to_htmlnode(markdown)
    html_node = html_node_string.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}",title)
    template =  template.replace("{{ Content }}",html_node)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    name_of_dir = os.path.dirname(dest_path)
    os.makedirs(name_of_dir, exist_ok=True)
    d = open(dest_path, 'w')
    d.write(template)
    f.close()
    t.close()
    d.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_list = os.listdir(dir_path_content)
    os.makedirs(dest_dir_path,exist_ok=True)
    for file in content_list:

        file_path = os.path.join(dir_path_content,file)
        if not os.path.isfile(file_path):

            generate_pages_recursive(file_path,template_path, os.path.join(dest_dir_path,file), basepath)
        elif os.path.isfile(file_path) and file.endswith(".md"):
            html_file = file.replace(".md",".html")

            generate_page(file_path, template_path, os.path.join(dest_dir_path,html_file), basepath)
        else:
            continue
    