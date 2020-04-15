import datetime
import os.path
import Constant

# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-
class UIImageEngine:

    imageList = set()

    def __init__(self):
        pass

    def __imageStrf(self, imageName):
        return "    static var %(imageName)s: UIImage { return UIImage(named: \"%(imageName)s\")! }\n" % { "imageName": imageName }


    def output(self, outputPath):

        file = open(outputPath, "w+")
        
        result = Constant.imageHeader

        file.write(result)
        for imageName in self.imageList:
            file.write(self.__imageStrf(imageName))
            # file.write("\n\n")

        file.write("}")
        file.close()
