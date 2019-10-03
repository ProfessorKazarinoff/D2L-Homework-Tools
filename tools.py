# tools.py

from zipfile37 import ZipFile
from pathlib import Path
import os
import string

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

    625597-437561 - firstname.lastname-Sep 28, 2019 120 PM-Homework_1.ipynb

    :param fname_str:
    :return:
    """
    return fname_str.split("-")[2].strip().rstrip(string.digits)

def reverse_name(fname_str):
    """
    reverse_name() is a function to reverse the last.first to first.last

    :param fname_str:
    :return:
    """
    sep = '.'
    s = fname_str.split(".")
    return sep.join(s[::-1])

def add_ipynb_ext(fname_str):
    """
    remove_json_ext() is a function to remove the extension .json if present at the end of a filename.

    :param fname_str:
    :return:
    """
    sep = '.'
    return sep.join([fname_str, 'ipynb'])

def main():
    f_str = 'Homework 1 Download Oct 1, 2019 1107 AM.zip'
    cwd = Path.cwd()
    print(cwd)
    f = Path(cwd,f_str)
    unzip_f(f)
    temp_dir = Path(cwd,'temp')
    remove_index(temp_dir)
    for path in temp_dir.iterdir():
        path_str = str(path)
        npath_str = reverse_name(path_str)
        npath_ext_str = add_ipynb_ext(npath_str)
        #path.rename(Path(path.parent,npath_ext_str))
        new_path = Path(str(path.parent),npath_ext_str)
        print(new_path)
if __name__ == "__main__":
    main()
