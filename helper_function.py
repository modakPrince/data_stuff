import zipfile
def unzip_data(file_path, extract_to='.'):
    """
    Unzips the specified zip file to the given directory.
    
    :param file_path: Path to the zip file.
    :param extract_to: Directory to extract files to. Defaults to current directory.
    """
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
