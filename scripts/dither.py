from lid import Dither
import os
from glob import glob

if __name__=="__main__":
    files  = glob("./assets/images/**/*.webp", recursive=True) + glob("./assets/images/**/*.png", recursive=True)
    print(files)
    for file_path in files:
        if not "logo"  in file_path:
            dithered_path = file_path.replace("images", "dithered").replace(".webp", ".png")
            os.makedirs(os.path.dirname(dithered_path), exist_ok=True)
            dither = Dither({"path": file_path, '-f':"png", 'out':'', '-q':25, '-t':''})
            dither.ordered_dither_9(False)
            dither.new.save(dithered_path, optimize=False, quality=100)
            print(f"Dithered : {file_path}")