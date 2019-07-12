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