# AVIF to PNG Converter

This script converts AVIF images to PNG format while maintaining the original subdirectory structure. 

## Instructions:

1. **Edit env.py:**
   - Open the `env.py` file and customize the following parameters:
     - `keep_name`: Set to `True` if you want PNG images to have the same name as the AVIF images, or `False` if you prefer numerical names start from 1 to n.
     - `dir_`: Provide the absolute path to the parent directory of the AVIF folder.
     - `folder`: Specify the folder name containing all the AVIF files.
     - `new_dir`: Specify the name of the new folder to store the PNG files.

   Example:
   ```python
   # Edit the params below
   keep_name = True
   dir_ = "/media/user/DRIVE/avif-png"
   folder = "avif-folder"
   new_dir = "/media/user/DRIVE/avif-png/png-folder"
   ```

## Dependencies Installation:
Instruction:
  1. Install requirements.txt either globally or in a virtual environment:
     - globally: 
        1. pip install -r requirements.txt
        2. python3 /path/to/avif_to_png.py
     - virtual environment: 
        1. python3 -m venv "Replace with a name with no double quotes"
        2. run source path/to/venv/bin/activate
        3. run path/to/venv/bin/python3 avif_to_png.py
