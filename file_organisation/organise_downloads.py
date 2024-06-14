#!/usr/bin/env python3
from typing import Dict, List
import os
import shutil


def organise_downloads(directory: str) -> None:
    # downloads directory
    src_dir: str = directory

    files: List = os.listdir(src_dir)
    # common file types go here: videos, images, code, text, utilities (zip) etc.
    file_types = {'Text': ['.txt', '.doc', '.docx', '.pdf', '.rtf'],
                  'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
                  'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
                  'Audio': ['.mp3', '.wav', '.ogg', '.flac'],
                  'Web': ['.html', '.htm', '.css', '.js'],
                  'Data': ['.csv', '.xml', '.json', '.yml', '.yaml'],
                  'Programming': ['.py', '.java', '.c', '.cpp', '.js', '.rb', '.go', '.php', '.cs', '.r', '.db', '.sqlite'],
                  'Executable': ['.exe', '.app', '.bin', '.jar', '.sh', '.dmg'],
                  'Archives': ['.zip', '.rar', '.tar', '.gz', '.gzip', '.7z'],
                  }
    # for all files in the list (downloads dir)
    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)  # create full file path
        if os.path.isfile(file_path):  # If this is a file rather than a directory
            file_extension = filename.split('.')[-1].lower()  # get the extension
            for folder, extensions in file_types.items():
                if file_extension in extensions:  # checks if file extension exists in out file types dict above
                    folder_path = os.path.join(download_dir, folder)
                    if not os.path.exists(folder_path):  # checks if path has already been created, if not it creates it
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))  # moves file into appropriate folder
                    break


# Main -> add a cron job in terminal to make this run automatically
if __name__ == '__main__':
    download_dir: str = '/Users/jackkennedy/Downloads/'
    organise_downloads(download_dir)
