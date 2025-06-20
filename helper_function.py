import zipfile
import os
def unzip_data(file_path, extract_to='.'):
    """
    Unzips the specified zip file to the given directory.
    
    :param file_path: Path to the zip file.
    :param extract_to: Directory to extract files to. Defaults to current directory.
    """
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def walk_directory(directory):
    """
    Walks through the specified directory and returns a list of all files.
    
    :param directory: Directory to walk through.
    :return: List of file paths.
    """
    for dirpath,dirnames ,files in os.walk(directory):
        print(f'There are {len(files)} and {len(dirnames)} directories in {dirpath}')

