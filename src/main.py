from textnode import TextNode, TextType
import os
import shutil
from gencontent import generate_pages_recursive
def copy_content():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")

def copy_(src,dst):
    src_dirs = os.listdir(src)
    for file in src_dirs:
        file_path = os.path.join(src,file)

        if os.path.isfile(file_path):
            shutil.copy(src=file_path,dst=dst)
        else:
            path = os.path.join(dst,file)
            os.mkdir(path)
            copy_(file_path,path)
def main():
    copy_content()
    copy_("static", "public")
    generate_pages_recursive('content','template.html', 'public')
if __name__ == "__main__":
    main()
