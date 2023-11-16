from os import listdir, mkdir, path, walk
import pillow_avif
from PIL import Image
from env import keep_name, dir_, folder, new_dir

def convert_avif_to_png(current_path: str, new_path: str, keep_name: bool):
    """Converts avif images with its corresponding subdirectories in new_path.

    Args:
        current_path (str): The path of the avif image folder.
        new_path (str): The path of the converted png image folder.
        keep_name (bool): keep original image name or false for numerical names(1 to n).
    """
    for root, dirs, files in walk(current_path):
        # Create corresponding subdirectories in the new_path
        relative_path = path.relpath(root, current_path)
        new_subdir = path.join(new_path, relative_path)

        for directory in dirs:
            new_dir_path = path.join(new_subdir, directory)
            if not path.exists(new_dir_path):
                mkdir(new_dir_path)

        # Start converting avif images.
        for file in files:
            if file.endswith('.avif'):
                avif_path = path.join(root, file)
                img = Image.open(avif_path)

                if not keep_name:
                    png_name = f"{len(listdir(new_subdir)) + 1}.png"
                else:
                    png_name = f"{path.splitext(file)[0]}.png"

                png_path = path.join(new_subdir, png_name)

                if not path.exists(png_path):
                    print(f"Converting {file} to {png_name}")
                    img.save(png_path, "png")
                    print(f"Successful: {png_name}\n")
                else:
                    print(f"Skipping {file} --> {png_name} already exists\n")

if __name__ == '__main__':
    current_path = path.join(dir_, folder)
    print(f"avif_path: {current_path}")

    new_path = path.join(dir_, new_dir)
    print(f"png path: {new_path}\n")

    if not path.exists(new_path):
        mkdir(new_path)

    convert_avif_to_png(current_path, new_path, keep_name)
