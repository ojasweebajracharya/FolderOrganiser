import os
import shutil

# Retrieves the date from the folder's name - if no date, returns none
def getDate(folderName):
    regex = r"[2][0][0-2][0-9]"
    matchDate = re.search(regex, str(folderName))

    if matchDate == None:
        return None
    else:
        return matchDate.group()


# Checks if the file is a duplicate
def isDuplicate(folderName, moveToDirectory, moveToFolder):
    # print("Running isDuplicate:")
    # print(f"moveToFolder (inside isDuplicate): {moveToFolder}")
    flag = False
    moveTo = f"{moveToDirectory}\{moveToFolder}"
    # print(f"moveto (inside isDuplicate): {moveTo}")
    with os.scandir(moveTo) as entries:
        for entry in entries:
            destFolderName = entry.name
            if folderName == destFolderName:
                flag = True
                break

    return flag

# Finds the file and moves to the correct folder depending on the date:
def findAndMove(currentDirectory, moveToDirectory, date, folderName):

    foundFlag = False
    # Loop through destination directory and find the folder that matches the date:
    with os.scandir(moveToDirectory) as entries:
        for entry in entries:
            currentFolder = (f"{currentDirectory}\{folderName}")  # The current file in the destination folder
            # print(f"entry.name (findAndMove): {entry.name}") # Destination folder it's at
            if isDuplicate == False:

                if date == "empty":
                    dest = shutil.move(currentFolder, moveToDirectory)
                    print("Moved successfully! :D")

                else:
                    folderDate = getDate(entry)  # Destination Folder's file's date
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







