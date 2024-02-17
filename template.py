import os 
import sys 
import pathlib 
from pathlib import Path


list_of_files = [
    "\\src\\__init__.py",
    "\\src\\components\\__init__.py",
    "\\src\\pipeline\\__init__.py",
    "\\src\\logger.py",
    "\\src\\exception_file.py",
    "\\setup.py",
    "\\requirements.txt",
    "\\src\\notebook\\EDA.ipynb",
    "\\src\\notebook\\FE.ipynb",
    "\\src\\components\\data_ingestion.py",
    "\\src\\components\\data_transformation.py",
    "\\main.py",
    "\\src\\utils.py"
]


dir_path_1 = os.getcwd() 

for file in list_of_files:

    full_path = dir_path_1 + file 
    whole_path = Path(full_path)
    dir_path, filename = os.path.split(whole_path)

    os.makedirs(dir_path, exist_ok=True)

    if os.path.exists(full_path):
        print(f"File already exists {filename}") 

    if (not os.path.exists(full_path)):
        with open(full_path, 'w') as f:
            print(f"File created {filename}")

