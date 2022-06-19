import os
import glob
import shutil
from tqdm import tqdm


html_folder = os.path.join("_build", "html")
favicon_filename = "favicon.png"
shutil.copy(favicon_filename, os.path.join(html_folder, favicon_filename))


old_head = "<head>"
head_with_favicon_template = """
<head>
    <link rel="icon" type="image/png" href="{}"/>
"""


def faviconize_file(filename: str, path_to_favicon: str):
    with open(filename, encoding='utf-8', mode="r") as f:
        content = f.read()
    new_head = head_with_favicon_template.format(path_to_favicon)
    if new_head not in content:
        new_content = content.replace(old_head, new_head)
        with open(filename,  encoding='utf-8', mode="w") as f:
            f.write(new_content)

def faviconize_folder(folder: str, path_to_favicon: str):
    pattern = os.path.join(folder, "*.html")
    for filename in tqdm(glob.glob(pattern, recursive=True)):
        faviconize_file(filename, path_to_favicon)



docs_folder = os.path.join(html_folder, "docs")
faviconize_folder(docs_folder, os.path.join("..", favicon_filename))

filename = os.path.join(docs_folder, "index.html")
faviconize_file(filename, favicon_filename)

notebooks_folder = os.path.join(html_folder, "notebooks")
faviconize_folder(notebooks_folder, os.path.join("..", favicon_filename))
for subfolder in glob.glob(os.path.join(notebooks_folder, "*/")):
    faviconize_folder(subfolder, os.path.join("..", "..", favicon_filename))