import os
import shutil
from pathlib import Path

def main():

    # Get the user's donwloads folder path
    # user_directory = os.path.expanduser('~')
    # downloads_directory = os.path.join(user_directory, 'Downloads')

    # FOR TESTING ONLY - Uncomment above lines when testing is completed ###########################
    downloads_directory = r"C:\Users\thoma\PycharmProjects\downloads-organizer-tool\test_downloads"
    #################################################

    # Create dictionary for organizing subdirectories and assigning file types
    ORGANIZED_SUBDIRECTORIES = {
        "Images" : [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents" : [".pdf", ".txt", ".docx", ".xlsx", ".csv", ".pptx"],
        "Installers" : [".exe", ".msi", ".inf", ".appx", ".msix"],
        "Audio" : [".mp3", ".aac", ".ogg", ".oga", ".flac", ".wav"],
        "Video" : [".mp4", ".mkv", ".webm", ".avi", ".mpg"],
        "Miscellaneous" : []
    }

    # Iterate over the subdirectories, check if each subdir exists in main downloads folder, if not create it
    for subdirectory in ORGANIZED_SUBDIRECTORIES:
        current_subdirectory_path = os.path.join(downloads_directory, subdirectory)
        if not os.path.isdir(current_subdirectory_path):
            os.mkdir(current_subdirectory_path)

    # Iterate over files inside the downloads folder and move them based on dictionary key-value pairs
    for file in os.listdir(downloads_directory):
        file_path = os.path.join(downloads_directory, file)
        if os.path.isfile(file_path):
            # Create a Path object so that use of the suffix property is possible
            current_file_path = Path(file_path)
            current_file_type = current_file_path.suffix

            # Iterate over the dictionary to find what subdirectory the file type is associated with and store that
            # subdirectory as the destination folder
            for key, value in ORGANIZED_SUBDIRECTORIES.items():
                if current_file_type in value:
                    dest_folder = key
                    # Create path and move file to destination folder
                    dest_folder_path = os.path.join(downloads_directory, dest_folder)
                    shutil.move(current_file_path, dest_folder_path)

                    # CURRENT ISSUE --- How can we store the unlisted file types in the Miscellaneous folder





    print(downloads_directory)

if __name__ == '__main__':
    main()