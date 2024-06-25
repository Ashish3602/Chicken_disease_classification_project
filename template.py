import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')


project_name = "cnnClassifier-Chicken_disease"
list_of_files = [
    ".github/workflows/.gitkeep", #empty folders are not committed so need something in folder
    f"src/{project_name}/__init__.py", #works as local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py"
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="": #check if there is no folder leading up to end file
        os.makedirs(filedir, exist_ok=True) #if directory is already present it wont be created
        logging.info(f"creating directory; {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0 ):
        with open(filepath , "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    
    else: 
        logging.info(f"{filename} already exists")
