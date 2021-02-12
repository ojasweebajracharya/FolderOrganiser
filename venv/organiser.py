import sys
import os
import shutil

from functionsFile import *

# Main section that is run first:
currentDirectory = sys.argv[1]
moveToDirectory = sys.argv[2]

# Checks if the directories entered exist:
isExistCurrent = os.path.exists(currentDirectory)
isExistMoveTo = os.path.exists(moveToDirectory)

task = input("Welcome! Would you like to:"
             "A: Move files"
             "B: Move and sort in date order")

if isExistCurrent and isExistMoveTo:
    print("They exist!!!")

    # Loops through the current directory
    with os.scandir(currentDirectory) as entries:
        for entry in entries:
            folderName = entry.name
            if os.path.isdir(f"{currentDirectory}\{folderName}"):
                if task == "A":
                    entryDate = "empty"
                    findAndMove(currentDirectory, moveToDirectory, entryDate, folderName)
                elif task == "B":
                    # Skips files without a date in the title
                    if getDate(entry) != None:
                        entryDate = getDate(entry)

                        print(f"entryDate: {entryDate}")
                        print(f"entry.name: (main) {folderName}")

                        findAndMove(currentDirectory, moveToDirectory, entryDate, folderName)


                    else:
                        print("The folder does not have a date in the title so I will analyse the metadata.")
                        # First get the first image inside the folder, if no images, print("No image files so folder not moved")
                        firstFolder = f"{currentDirectory}\{folderName}"
                        for imagefile in os.listdir(firstFolder):
                            if imagefile.endswith(".JPG") or imagefile.endswith(".jpeg") or imagefile.endswith(".jpg"):
                                imgPath = f"{currentDirectory}\{folderName}\{imagefile}"
                                image = Image.open(imgPath)
                                exifdata = image.getexif()

                                dateCreated = exifdata.get(36867)
                                yearTaken = getDate(str(dateCreated))
                                image.close()
                                findAndMove(currentDirectory, moveToDirectory, yearTaken, folderName)
                                break
                else:
                    print("You didn't enter a valid option.")
            else:
                pass
else:
    print("Your paths do not exist.")