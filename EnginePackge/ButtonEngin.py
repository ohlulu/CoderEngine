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
folder = filedialog.askdirectory(initialdir = "~/Desktop",title = "Select file")

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
    lowerFile = file.lower()
    if "pressed" not in lowerFile and "normal" not in lowerFile and "disabled" not in lowerFile:
        continue
    else:
        engine.addFileWith(file)

engine.output("ButtonFactory")        

# print(fileSet)
