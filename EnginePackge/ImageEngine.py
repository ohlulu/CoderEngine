# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-
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

fileList = []

class ImageFloderParser:

    def __init__(self):
        pass

    def parseFloder(self, targetPath):
        print(targetPath)
        for path in targetPath:
            print("parse ->", path)
            isImageset = ".imageset" in path
            if isImageset: 
                print("is image ->", path)
                fileName = path.replace('.imageset', '')
                fileList.append(fileName)
            elif os.path.isdir(path):
                print("is floder ->", path)
                self.parseFloder(os.listdir(path))
            else:
                print("nothing at all ->", path)
                continue


ImageFloderParser().parseFloder(os.listdir(inputPath))
engine = Engine.UIImageEngine()
engine.imageList = sorted(fileList,key = lambda s: s[0].lower())
engine.output(outputPath)
print("file count -> ", len(fileList))
