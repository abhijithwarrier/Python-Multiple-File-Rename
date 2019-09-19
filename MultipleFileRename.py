# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO RENAME ALL THE FILES IN A FOLDER
# Files can be renamed using rename() of OS Module in Python

# Importing the os module
import os

# Defining fileRename() which renames all the files of a folder
def fileRename():

    # Initializing a count variable to 0
    count = 0
    # Looping through all the files present in the folder
    for files in os.listdir("FOLDER PATH WHICH CONTAINS THE FILES"):

        # Getting the extension of the file
        file_extension = os.path.splitext(files)[1]
        # Defining a new name for the file with its extension
        newName = "user-input_name ("+str(count)+")"+file_extension

        # Getting the source address of the file
        source = "SOURCE ADDRESS (FOLDER PATH WHICH CONTAINS THE FILES)"+files
        # Defining the destination address to save the file with new name
        destination = "DESTINATION FOLDER ADDRESS"+newName

        # Renaming the files the source files present in the directory
        os.rename(source, destination)

        # Incrementing the count variable
        count += 1

    print("\nALL THE FILES HAVE BEEN RENAMED SUCCESSFULLY")

# Driver Code
if __name__ == '__main__':
    fileRename()
