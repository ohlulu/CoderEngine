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

engine = OhEngine.UIImageEngine()

fileSet = set()
for file in allFile:
    isPng = ".png" in file
    if not isPng: continue
    try:
        endIndex = str(file).index("@")
    except:
        endIndex = file.index(".")
    fileSet.add(file[0:endIndex])
    
for file in fileSet:
    engine.addImage(file)

engine.output("ImageHelper")
print("file count -> ", len(fileSet))
# print(fileSet)
