import sys
import os
import glob
import Engine

# package cmd
# pyinstaller -F ./ImageEngine.py

# gat image input path
inputPath = sys.argv[1] if len(sys.argv) > 1 else "/"
# get image.swift output path
outputPath = sys.argv[2] if len(sys.argv) > 2 else "/"
# move os workplace
os.chdir(inputPath)

fileSet = set()
for path in os.listdir(inputPath):
    isImageFolder = ".imageset" in path and os.path.isdir(path)
    if not isImageFolder: continue
    for imageFile in os.listdir(path):
        isImage = ".png" in imageFile or ".pdf" in imageFile
        if not isImage: continue
        try:
            endIndex = str(imageFile).index("@")
        except:
            endIndex = str(imageFile).index(".")
        fileSet.add(imageFile[0:endIndex])

engine = Engine.UIImageEngine()
engine.imageList = sorted(list(fileSet),key = lambda s: s[0].lower())
engine.output(outputPath)
print("file count -> ", len(fileSet))
