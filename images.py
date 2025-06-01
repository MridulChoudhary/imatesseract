import os
import re
import shutil
posts_dir = r"C:\Blog\imatesseract_vault\posts"
attachments_dir = r"C:\Blog\imatesseract_vault"
static_images_dir = r"C:\Blog\imatesseract\static\images"

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        images = re.findall(r'\!\[\[([^]]*\.jpg)\]\]', content)
        for image in images:
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"![[{image}]]", markdown_image)
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
print("Markdown files processed and images copied successfully.")
