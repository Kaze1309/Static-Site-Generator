import os
import shutil
import sys
from gencontent import generate_pages_recursive
def copy_content():
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.mkdir("docs")

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
    basepath = ''
    sys.argv
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    copy_content()
    copy_("static", "docs")
    generate_pages_recursive('content','template.html', 'docs',basepath)
if __name__ == "__main__":
    main()
