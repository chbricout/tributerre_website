import os
from glob import glob
from PIL import Image

if __name__=="__main__":
    files  = glob("./assets/images/**/*.webp", recursive=True) + glob("./assets/images/**/*.png", recursive=True)
    print(files)
    for file_path in files:
        compressed_path = file_path.replace("images", "compressed").replace(".png","")
        os.makedirs(os.path.dirname(compressed_path), exist_ok=True)
        new = Image.open(file_path)
        new.save(compressed_path, "WEBP", optimize=True, quality=30)
        print(f"Compressed : {file_path}")