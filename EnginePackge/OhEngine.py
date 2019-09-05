import datetime
import os.path

class UIImageEngine:

    fileName = "OhImgae"

    iamgeList = []

    def __init__(self, fileName = "OhImgae"):
        self.fileName = fileName

    # private property or methods

    # can add to many image
    def addImage(self, name):
        self.iamgeList.append(name)

    def __imageStrf(self, imageName):
        return "    static var %(imageName)s: UIImage {\n        return UIImage(named: \"%(imageName)s\")!\n    }" % { "imageName": imageName }
        # f"    static var {imageName} UIImage(named: {imageName})!"

    def output(self, fileName):
        homedir = os.path.expanduser("~")

        file = open(f"{homedir}/Desktop/{fileName}.swift", "w+")

        today = datetime.datetime.today()

        header = f"""
//
//  {self.fileName}.swift
//  ohlulu
//
//  Created by OhImgae.py on {today.strftime("%Y/%m/%d")}
//  Lastupdate on 2019/7/9
//  Copyright © 2019 ohlulu. All rights reserved.
//
        """ 

        result = """
%(header)s
import UIKit

extension UIImage {\n
"""

        # print(result %  {"header": header})
        file.write(result %  {"header": header})
        for imageName in self.iamgeList:
            # print(self.__imageStrf(imageName), "\n")
            file.write(self.__imageStrf(imageName))
            file.write("\n\n")
                    
        # print("}")
        file.write("}")
        file.close()

class UIButtonEngin:

    buttonList = {}

    def __init__(self):
        pass

    def addFileWith(self, file):
        lowerFile = file.lower()
        if "normal" in lowerFile:
            lowerFile = file.replace("Normal","")
        elif "pressed" in lowerFile:
            lowerFile = file.replace("Pressed","")
        elif "disabled" in lowerFile:
            lowerFile = file.replace("Disabled","")

        if lowerFile in self.buttonList.keys():
            # print("in key", lowerFile)
            self.buttonList[lowerFile].append(file)
        else:
            # print("not in key", lowerFile)
            self.buttonList[lowerFile] = [file]

    def __buttonStrf(self, varName, buttonInfos):
        scope  = "\n\n    static var %(varName)s: UIButton {\n" % {"varName": varName}
        scope += "        return UIButton().oh\n"
        for info in buttonInfos:
            if "Normal" in info:
                scope += "            .backgroundImage(.%(info)s, for: .normal)\n" % {"info": info}
            if "Pressed" in info:
                scope += "            .backgroundImage(.%(info)s, for: .highlighted)\n" % {"info": info}
            if "disabled" in info:
                scope += "            .backgroundImage(.%(info)s, for: .disabled)\n" % {"info": info}
        scope += "            .done()\n"   
        scope += "    }"
        return scope
    
    def output(self, fileName):
        homedir = os.path.expanduser("~")

        file = open(f"{homedir}/Desktop/{fileName}.swift", "w+")

        today = datetime.datetime.today()

        header = f"""
//
//  {fileName}.swift
//  ohlulu
//
//  Created by OhButtonEngin.py on {today.strftime("%Y/%m/%d")}
//  Lastupdate on 2019/7/9
//  Copyright © 2019 ohlulu. All rights reserved.
//
        """ 

        result = """
%(header)s
import UIKit

extension UIButton {
"""
        file.write(result %  {"header": header})
        for key in self.buttonList.keys():
            if len(self.buttonList[key]) == 1: continue
            file.write(self.__buttonStrf(key, self.buttonList[key]))

        file.write("\n}")
        file.close()