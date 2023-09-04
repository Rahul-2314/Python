# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os

dir="C:/Users/chowd/Desktop/Python/programs/png_rename/pic"
png_files=[file for file in os.listdir(dir)
            if file.lower().endswith(".png")]

x=0
for png_file in png_files:
    print(png_file)
    x+=1
    old_name=dir+"/"+png_file
    new_name=dir+"/"+f"{x}.png"
    os.rename(old_name,new_name)

dir="C:/Users/chowd/Downloads"
png1_files=[file for file in os.listdir(dir)
            if file.lower().endswith(".png")]
for png1_file in png1_files:
    print(png1_file)
    