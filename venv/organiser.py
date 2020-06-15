import sys
import os
from PIL import Image
import re

def getDate(folderName):
    # Using regex - Works wherever the date is in the title:
    regex = r"[2][0][0-1][0-9]"
    matchDate = re.search(regex, str(folderName))

    if matchDate == None:
        return None
    else:
        return matchDate.group()


def findAndMove(currentDirectory, moveToDirectory, date):

    foundFlag = False
    # Loop through moveToDirectory and find the folder that matches the date:
    with os.scandir(moveToDirectory) as entries:
        for entry in entries:
            folderDate = getDate(entry)

            if folderDate == date:

                print(f"We've found a matching folder for {date}!")
                foundFlag = True
                break

        if foundFlag == False:
            print(f"There are no folders with the date {date}, would you like to make a new folder for it?")



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
            # Retrieves the date from the title:

            # Using String Manipulation but only works if date at the end:
            # entryDate = (str(entry))[-6:-2]


            # Skips files without a date in the title
            if getDate(entry) != None:
                entryDate = getDate(entry)

                print(entryDate)
                print(entry.name)

                findAndMove(currentDirectory, moveToDirectory, entryDate)

                check = input("Would you like to continue? Y or N: ")

                if check == "Y":
                    print("You've chosen to continue.")
                    continue
                elif check == "N":
                    print("You've chosen not to continue.")
                    break
                else:
                    print("You did not enter either 'Y' or 'N' so I will assume you wish not to continue.")
                    break

else:
    print("Your paths do not exist.")