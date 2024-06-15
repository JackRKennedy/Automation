#!/usr/bin/env python3

from typing import Dict, List
import os
import shutil
import logging
from pathlib import Path


def organise_downloads(directory: str) -> None:
    """Organizes files in the specified directory into folders based on file type."""

    # List all files in the specified directory
    files: List = os.listdir(directory)

    # Dictionary of common file types and their corresponding extensions
    file_types = {
        'Text': ['txt', 'doc', 'docx', 'pdf', 'rtf'],
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'tiff', 'ico'],
        'Videos': ['mp4', 'mkv', 'mov', 'avi', 'wmv'],
        'Audio': ['mp3', 'wav', 'ogg', 'flac'],
        'Web': ['html', 'htm', 'css', 'js'],
        'Data': ['csv', 'xml', 'json', 'yml', 'yaml'],
        'Programming': ['py', 'java', 'c', 'cpp', 'js', 'rb', 'go', 'php', 'cs', 'r', 'db', 'sqlite'],
        'Executable': ['exe', 'app', 'bin', 'jar', 'sh', 'dmg'],
        'Archives': ['zip', 'rar', 'tar', 'gz', 'gzip', '7z'],
    }

    # Iterate over all files in the list (downloads dir)
    for filename in files:
        # Create the full file path
        file_path = os.path.join(directory, filename)

        # If this is a file rather than a directory
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = filename.split('.')[-1].lower()

            # Check if the file extension exists in our file types dictionary above
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    # Create the folder path
                    folder_path = os.path.join(directory, folder)

                    # Check if the path has already been created, if not, create it
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    # Move the file into the appropriate folder
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    logging.info(f'Moved file {file_path} into {folder_path}')
                    break
            else:
                logging.warning(f'No matching folder for file extension {file_extension}: {filename}')


# Main entry point of the script
if __name__ == '__main__':
    # Directory to organize (Downloads folder)
    download_dir: str = '/Users/jackkennedy/Downloads/'

    # Logging setup: Going to log all file runs for debugging and peace of mind
    log_file_folder = Path(__file__).resolve().parent.joinpath('log_data')
    log_file_folder.mkdir(parents=True, exist_ok=True)
    log_file_path = log_file_folder.joinpath('organiser.log')

    # Configure logging
    logging.basicConfig(filename=str(log_file_path), level=logging.INFO)
    logging.info('Started organizing downloads')

    # Call the function to organize the downloads directory
    organise_downloads(download_dir)

    logging.info('Finished organizing downloads')

    # I have copied this to my path so it can be executable anywhere
