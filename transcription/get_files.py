import os

def get_file_names_recursive(directory):
    """
    Gets all file names in a directory and its subdirectories.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of file paths.
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def get_just_file_names(directory):
    """
    Gets just the file names, without the full paths.

    Args:
    directory (str): The path to the directory.

    Returns:
    list: A list of file names.
    """
    file_names = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_names.append(file)
    return file_names

def get_files_by_extension(directory, extensions):
    """
    Gets files with specified extensions.
    Args:
        directory (str): The path to the directory.
        extensions (list): A list of file extensions (e.g., ['.txt', '.pdf']).
    Returns:
        list: A list of file paths.
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                file_paths.append(os.path.join(root, file))
    return file_paths