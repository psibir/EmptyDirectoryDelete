
import os
from pathlib import Path
from contextlib import suppress

# This script is used to delete empty directories in a given directory.
# WARNING: THIS SCRIPT IS DESTRUCTIVE, USE CAUTION WHEN USING IT.

warning = input("This script will delete all empty folders in the given directory.\nDo you wish to continue? Enter y or n: ")
src_dir = input("Enter the source directory: ")

# Warnings with initial user input prompt
def initialchoice():
    while True:
        if warning == "y": 
            print("Empty folders deleted.")
            break
        elif warning == "n": 
            print("Exiting...")
            exit()
        else: 
            print("Please enter y or n.")
            continue


# Warnings with final user input prompt
def finalchoice():
    while True:
        if final_warning == "y": 
            main()
            print("Empty folders deleted.")
            exit()
        elif final_warning == "n": 
            print("Exiting...")
            exit()
        else: 
            print("Please enter y or n.")
            continue

# Directory deletion function
def main():
    for root,dirs,_ in os.walk(src_dir, topdown=False):
        for d in dirs:
            with suppress(OSError):
                os.rmdir(Path(root,d))

initialchoice()
final_warning = input("Preparing to delete empty directories in " + src_dir + "...\nAre you sure you want to continue? Enter y or n: ")
finalchoice()

if __name__ == "__main__":
    main()
