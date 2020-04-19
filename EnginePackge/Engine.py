import datetime
import os.path
import Constant
import re

# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-
class UIImageEngine:

    imageList = []

    def __init__(self):
        pass

    def __imageStrf(self, imageName):
        imageNameForVariable = self.convert(imageName)
        imageNameForVariable = self.removePunctuation(imageNameForVariable)
        return "    static var %(imageNameForVariable)s: UIImage { return UIImage(named: \"%(imageName)s\")! }\n\n" % { "imageNameForVariable": imageNameForVariable,"imageName": imageName }


    def output(self, outputPath):

        file = open(outputPath, "w+")
        
        result = Constant.Constant.imageHeader

        file.write(result)
        for imageName in self.imageList:
            file.write(self.__imageStrf(imageName))
            # file.write("\n\n")

        file.write("}")
        file.close()

    def convert(self, imageName):

        stringList = imageName.split("_")
        stringList = [s.capitalize() for s in stringList]
        outputStr = "".join(stringList)
        lowercase = lambda s: s[:1].lower() + s[1:] if s else '' # just song for use lambda...
        return lowercase(outputStr)

    def  removePunctuation(self, imageName):

        rule = re.compile("[^a-zA-Z0-9\u4e00-\u9fa5]")

        return rule.sub('',imageName)
