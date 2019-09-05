# package cmd
# pyinstaller -F ./ImageEngine.py
from os import listdir

from os.path import isfile, join
from tkinter import filedialog
from tkinter import *

import glob
import os

import OhEngine

root = Tk()
root.withdraw()
folder = filedialog.askdirectory(initialdir = "/",title = "Select file")

allFile = os.listdir(folder)

engine = OhEngine.UIButtonEngin()

fileSet = set()
for file in allFile:
    isImage = ".png" in file or  ".pdf" in file
    if not isImage: continue
    try:
        endIndex = str(file).index("@")
    except:
        endIndex = file.index(".")
    fileSet.add(file[0:endIndex])
    
for file in fileSet:
    if "Pressed" not in file and "Normal" not in file and "Disabled" not in file:
        continue
    else:
        engine.addFileWith(file)

engine.output("ButtonFactory")        


# print("file count -> ", len(fileSet))
# print(fileSet)
