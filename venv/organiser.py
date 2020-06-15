import sys
import os
import shutil
from PIL import Image
import re
from PIL.ExifTags import TAGS

# Retrieves the date from the folder's name - if no date, returns none
def getDate(folderName):
    regex = r"[2][0][0-2][0-9]"
    matchDate = re.search(regex, str(folderName))

    if matchDate == None:
        return None
    else:
        return matchDate.group()


# Get date from the first images metadata:
def metadataDate(currentDirectory, folderName):
    # First go inside folder, look at metadata of picture one
    with os.scandir(currentDirectory) as entries:
        for entry in entries:

            break
    # Retrieve the date and print it out.


def isDuplicate(folderName, moveToDirectory, moveToFolder):
    flag = False
    moveTo = f"{moveToDirectory}\{moveToFolder}"
    print(f"moveto: {moveTo}")
    with os.scandir(moveTo) as entries:
        for entry in entries:
            destFolderName = entry.name
            if folderName == destFolderName:
                flag = True
                break

    return flag

def findAndMove(currentDirectory, moveToDirectory, date, folderName):

    foundFlag = False
    # Loop through moveToDirectory and find the folder that matches the date:
    with os.scandir(moveToDirectory) as entries:
        for entry in entries:
            folderDate = getDate(entry)
            currentFolder = (f"{currentDirectory}\{folderName}")
            print(isDuplicate(folderName, moveToDirectory, entry.name))

            if isDuplicate == False:

                if folderDate == date:
                    print(f"We've found a matching folder for {date}!")

                    destinationFolder = (f"{moveToDirectory}\{date}")

                    print(f"Destination Folder: {destinationFolder}")
                    print(f"Current Directory: {currentFolder}")

                    dest = shutil.move(currentFolder, destinationFolder)
                    print("Moved successfully! :D")
                    foundFlag = True
                    break

                if foundFlag == False:
                    answer = input(f"There are no folders with the year {date}, would you like to make a new folder for it?")

                    if answer == "Y":
                        # Create a folder with title of the date and run function again
                        newDir = os.path.join(moveToDirectory, date)
                        os.mkdir(newDir)

                        findAndMove(currentDirectory, moveToDirectory, date, folderName)
                    else:
                        print(f"You've chosen not to create a folder for {date}")


            else:

                destinationFolder = (f"{moveToDirectory}\Duplicates")
                dest = shutil.move(currentFolder, destinationFolder)
                print("This file is a duplicate so I've placed it inside the folder 'duplicates'")



# Main section that is run first:
currentDirectory = sys.argv[1]
moveToDirectory = sys.argv[2]

# Checks if the directories entered exist:
isExistCurrent = os.path.exists(currentDirectory)
isExistMoveTo = os.path.exists(moveToDirectory)


if isExistCurrent and isExistMoveTo:
    print("They exist!!!")
    with os.scandir(currentDirectory) as entries:
        for entry in entries:

            # Skips files without a date in the title
            if getDate(entry) != None:
                entryDate = getDate(entry)

                folderName = entry.name


                print(f"entryDate: {entryDate}")
                print(f"entry.name: {folderName}")

                findAndMove(currentDirectory, moveToDirectory, entryDate, folderName)

                # check = input("Would you like to continue? Y or N: ")
                #
                # if check == "Y":
                #     print("You've chosen to continue.")
                #     continue
                # elif check == "N":
                #     print("You've chosen not to continue.")
                #     break
                # else:
                #     print("You did not enter either 'Y' or 'N' so I will assume you wish not to continue.")
                #     break

            else:
                print("The folder does not have a date in the title so I will analyse the metadata.")
                 # Run metadata function

else:
    print("Your paths do not exist.")