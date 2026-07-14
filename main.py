import os

def main():

    # Get the user's donwloads folder path
    user_directory = os.path.expanduser('~')
    downloads_directory = os.path.join(user_directory, 'Downloads')

    # Create dictionary for organizing subdirectories and assigning file types
    ORGANIZED_SUBDIRECTORIES = {
        "Images" : [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents" : []
    }

    print(downloads_directory)

if __name__ == '__main__':
    main()