import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')
prjctname= 'textsummarizer'

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{prjctname}/__init__.py",
    f"src/{prjctname}/components/__init__.py",
    f"src/{prjctname}/utils/__init__.py",   
    f"src/{prjctname}/utils/common.py",
    f"src/{prjctname}/logging//__init__.py",
    f"src/{prjctname}/config/__init__.py",
    f"src/{prjctname}/config/configuration.py",
    f"src/{prjctname}/pipeline/__init__.py",
    f"src/{prjctname}/entity/__init__.py",
    f"src/{prjctname}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

for filepath in list_files:
    filepath=Path(filepath)
    filedir , filename= os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory{filedir}for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Create empty file: {filepath}")
    else:
        logging.info(f"{filename} already exist")

