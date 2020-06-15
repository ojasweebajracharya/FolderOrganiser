import sys
import os
import shutil
from PIL import Image
import re

def getDate(folderName):
    # Using regex - Works wherever the date is in the title:
    regex = r"[2][0][0-2][0-9]"
    matchDate = re.search(regex, str(folderName))

    if matchDate == None:
        return None
    else:
        return matchDate.group()


def findAndMove(currentDirectory, moveToDirectory, date, folderName):

    foundFlag = False
    # Loop through moveToDirectory and find the folder that matches the date:
    with os.scandir(moveToDirectory) as entries:
        for entry in entries:
            folderDate = getDate(entry)

            if folderDate == date:
                print(f"We've found a matching folder for {date}!")
                destinationFolder = (f"{moveToDirectory}\{date}")
                currentFolder = (f"{currentDirectory}\{folderName}")
                print(f"Destination Folder: {destinationFolder}")
                print(f"Current Directory: {currentFolder}")

                dest = shutil.move(currentFolder, destinationFolder)
                print("Moved successfully! :D")
                foundFlag = True
                break


        if foundFlag == False:
            answer = input(f"There are no folders with the date {date}, would you like to make a new folder for it?")

            if answer == "Y":
                # Create a folder with title of the date and run function again

                findAndMove(currentDirectory, moveToDirectory, date)
            else:
                print(f"You've chosen not to create a folder for {date}")



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



                print(f"entryDate: {entryDate}")
                print(f"entry.name: {entry.name}")

                findAndMove(currentDirectory, moveToDirectory, entryDate, entry.name)

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
    print("Your paths do not exist.")