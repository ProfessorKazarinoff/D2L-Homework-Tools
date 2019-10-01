# tools.py

from zipfile37 import ZipFile
from pathlib import Path
import os

def unzip_f(in_path):
    """
    unzip_folder() is a function to unzip a folder, all files from the folder end up in the 'temp' dir relative to the in_path

    :param in_path: Path object which is the folder to unzip
    :param outdir_path: Path object which is the folder to save into
    :return: None
    """
    with ZipFile(in_path, 'r') as f:
        f.extractall('temp')

def remove_index(in_dir):
    """
    remove_index() is a function that removes an index.html file from a directory

    :param in_dir: Path object that is a directory that contains an index.html to be removed
    :return:
    """
    if Path(in_dir,'index.html').exists():
        os.remove(Path(in_dir,'index.html'))

def clean_fname(fname_str):
    """
    clean_fname() is a function to clean the beginning of a filename so that it starts just with characters
    :param fname_str:
    :return:
    """
    pass

def reverse_name(fname_str):
    """
    reverse_name() is a function to reverse the last.first to first.last

    :param fname_str:
    :return:
    """
    pass

def remove_json_ext(fname_str):
    """
    remove_json_ext() is a function to remove the extension .json if present at the end of a filename.

    :param fname_str:
    :return:
    """
    pass

def main():
    f_str='Homework 1 Download Oct 1, 2019 1107 AM.zip'
    cwd = Path.cwd()
    f = Path(cwd,f_str)
    unzip_f(f)
    temp_dir = Path(cwd,'temp')
    remove_index(temp_dir)

if __name__ == "__main__":
    main()
