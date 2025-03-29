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

def get_files_grouped_by_subdirectory(directory, extensions):
    """
    Gets files with specified extensions grouped by subdirectories.

    Args:
        directory (str): The path to the directory.
        extensions (list): A list of file extensions (e.g., ['.txt', '.pdf']).

    Returns:
        dict: A dictionary where keys are subdirectory paths and values are lists of file paths.
    """
    grouped_files = {}
    for root, _, files in os.walk(directory):
        filtered_files = [
            os.path.join(root, file)
            for file in files
            if any(file.lower().endswith(ext.lower()) for ext in extensions)
        ]
        if filtered_files:
            grouped_files[root] = filtered_files
    return grouped_files

def get_files_grouped_by_first_subdirectory(directory, extensions):
    """
    Gets files with specified extensions grouped by the first-level subdirectories.

    Args:
        directory (str): The path to the directory.
        extensions (list): A list of file extensions (e.g., ['.txt', '.pdf']).

    Returns:
        dict: A dictionary where keys are first-level subdirectory names and values are lists of file paths.
    """
    grouped_files = {}
    for root, _, files in os.walk(directory):
        # Get the relative path of the current directory to the root directory
        relative_path = os.path.relpath(root, directory)
        # Split the relative path to get the first-level subdirectory
        first_subdir = relative_path.split(os.sep)[0] if relative_path != "." else "."

        filtered_files = [
            os.path.join(root, file)
            for file in files
            if any(file.lower().endswith(ext.lower()) for ext in extensions)
        ]

        if filtered_files:
            if first_subdir not in grouped_files:
                grouped_files[first_subdir] = []
            grouped_files[first_subdir].extend(filtered_files)

    # Return a sorted dictionary by first-level subdirectory names
    return dict(sorted(grouped_files.items()))


import pandas as pd

def create_dataframe_from_list(data):
    """
    Creates a Pandas DataFrame from the given list of dictionaries.

    Args:
        data (list): The list of dictionaries.

    Returns:
        pandas.DataFrame: The resulting DataFrame.
    """
    rows = []
    for item in data:
        data = item['data']
        text = data['text']
        timestamp = []
        for chunk in data['chunks']:
            timestamp_start, timestamp_end = chunk['timestamp']
            chunk_text = chunk['text']
            # rows.append({
            #     'text': text,
            #     'timestamp_start': timestamp_start,
            #     'timestamp_end': timestamp_end,
            #     'chunk_text': chunk_text
            # })
            timestamp.append(
                f"{timestamp_start} - {timestamp_end}: {chunk_text}"
            )
        rows.append({
                'file': item['file'],
                'text': text,
                'timestamp': ', '.join(timestamp)
        })
    return pd.DataFrame(rows, columns=['file', 'text', 'timestamp'])
    # return rows

