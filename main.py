import os

def main():

    # Get the user's donwloads folder path
    user_directory = os.path.expanduser('~')
    downloads_directory = os.path.join(user_directory, 'Downloads')

    # Create dictionary for organizing subdirectories and assigning file types
    ORGANIZED_SUBDIRECTORIES = {
        "Images" : [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents" : [".pdf", ".txt", ".docx", ".xlsx", ".csv", ".pptx"],
        "Installers" : [".exe", ".msi", ".inf", ".appx", ".msix"],
        "Audio" : [".mp3", ".aac", ".ogg", ".oga", ".flac", ".wav"],
        "Video" : [".mp4", ".mkv", ".webm", ".avi", ".mpg"],
        "Miscellaneous" : []
    }

    # Iterate over the subdirectories, check if each exists in main downloads folder, if not create it
    for subdirectory in ORGANIZED_SUBDIRECTORIES:



    print(downloads_directory)

if __name__ == '__main__':
    main()