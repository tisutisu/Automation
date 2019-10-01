import os

def get_files_from_dir(path):
    return os.listdir(path)

def get_content_in_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines
