import os
import shutil
import gui

source = gui.source
dest = gui.destination
os.getcwd()  # getting current working folder
os.chdir(source)  # changing to the source folder
allfiles = os.listdir('D:\Sort\source')  # taking all files and folder in allfiles
print(os.getcwd())
print(allfiles)

ext_l = []   # taking empty list for all extension

for file in allfiles:  # running loop for all files
    if os.path.isfile(file):  # checking if it is file
        e = file.split('.')[-1]  # splitting file by its extensions
        ext_l.append(e.upper())  # appending extensions in ext_l

ext_l = set(ext_l)  # removing duplicate values
print(ext_l)  # printing extension list

# taking try and except block for file exist error
try:
    for ext in ext_l:  # running loop for all extensions
        os.makedirs(dest + "\\" + ext)  # make folder for each extensions
        for file in allfiles:  # running loop for all files
            if (os.path.isfile(file)) and (ext.lower() in file):  # checking if it is file and extension is there in files
                shutil.move(file, dest + "\\" + ext)  # then move that file to destination folder
except FileExistsError:
    for ext in ext_l: # running loop for all extensions
        for file in allfiles: # running loop for all files
            if (os.path.isfile(file)) and (ext.lower() in file):  # checking if it is file and extension is there in files
                shutil.move(file, dest + "\\" + ext)  # then move that file to destination folder
