import os
import argparse

def delete_empty_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                print(f"Deleted empty folder: {folder_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete empty folders from a directory.")
    parser.add_argument("directory", help="Directory path to delete empty folders from")
    args = parser.parse_args()

    delete_empty_folders(args.directory)
