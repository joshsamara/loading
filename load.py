#!/usr/bin/python
import sys
import os
import random
from mygetch import *

class LoadingBar(object):
    """docstring for LoadingBar"""
    def __init__(self):
        super(LoadingBar, self).__init__()
        #levels of properties
        self.loadingText = [0,2]
        self.finishedText = [0,2]
        self.introText = [0,3]
        self.brackets = [0,3]
        self.barStyle = [0,3]
        self.counter = [0,3]

        #Dynamic counter
        self.current = 0

        #Static max
        self.maxVal = 200

    def getIntroText(self):
        texts = {
        0: ".",
        1: "hi",
        2: "Welcome",
        3: "==== Welcome to Loading Bar Sim! ==="
        }
        return texts[self.introText[0]]

    def getLoadingText(self):
        texts = {
        0: "2 load pres spcae alot",
        1: "Press space to load...",
        2: "Loading: Press Space to process faster..."}
        return texts[self.loadingText[0]]

    def getFinishedText(self):
        texts = {
        0: "X",
        1: "Done",
        2: "Loading Complete. Prace any key to continue..."}
        return texts[self.finishedText[0]]

    def getBrackets(self):
        types = {
        0: "  ",
        1: "{!",
        2: "/\\",
        3: "[]"}
        return types[self.brackets[0]]

    def getBar(self):
        types = {
        0: "  ",
        1: "|x",
        2: "-.",
        3: "=-"}
        return types[self.barStyle[0]]

    def getCounter(self):
        if self.counter[0] == 0:
            return ""
        elif self.counter[0] == 1:
            return str(min(self.current/2, self.maxVal/2))
        elif self.counter[0] == 2:
            return "%s/%s" % (min(self.current/2, self.maxVal/2), self.maxVal)
        elif self.counter[0] == 3:
            digit = 2 * int(float(min(self.current/2, self.maxVal/2))/self.maxVal * 100)
            dec = [str(random.randint(0,99)).zfill(2), "00"][digit == 100]
            return "%s.%s%%" % (digit, dec)


    def drawLoadBar(self):
        width = 20
        lbracket,rbracket = self.getBrackets()
        barMaj, barMin = self.getBar()
        progress = self.getCounter()
        #Double bar count
        barCount2 = min(int(float(self.current)/self.maxVal * width * 2), width * 2)
        barStart = barCount2
        if barCount2 % 2 == 0:
            minDraw = ""
        else:
            minDraw = barMin
            barCount2 -= 1
        majCount =  barCount2 / 2
        fillDraw = majCount * barMaj + minDraw
        spaceDraw = " " *(width - len(fillDraw))
        sys.stdout.write("\r" + (50*" ") + "\r")
        fullLine = lbracket + fillDraw + spaceDraw + rbracket + "  %8s" % progress
        sys.stdout.write(fullLine)


    def isLoaded(self):
        return self.current >= self.maxVal

    def load(self):
        clear()
        self.current = 0
        print self.getIntroText()
        print self.getLoadingText()
        while not self.isLoaded():
            self.drawLoadBar()
            if getInput() == " ":
                self.current += random.randint(1,20)
        self.drawLoadBar()    
        print "\n"+self.getFinishedText()
        getInput()    

    def upgrade(self):
        clear()
        prettyDict = {
        "loadingText": "Loading Text",
        "finishedText": "Completion Text",
        "introText": "Introduction Text",
        "brackets": "Bracket Style",
        "barStyle": "Loading Bar Style",
        "counter": "Completion Counter"}

        upgradeable = {}
        i = 0
        for key in self.__dict__:
            if key in prettyDict and self.__dict__[key][0] < self.__dict__[key][1]:
                upgradeable[i + 1] = key
                i += 1

        if len(upgradeable) == 0:
            print "Fully upgraded"
            print "Press any key to continue..."
            getInput()
        else:
            print "Press the matching key to upgrade:"
            print "0) %-25s" % "Random!"
            maxVal = len(upgradeable)
            for i in range(maxVal):
                i=i+1
                place = "%s) " % i
                key = upgradeable[i]
                name  = "%-25s" % prettyDict[key]
                level = "Level: %d  " % self.__dict__[key][0]
                maxLevel = "Max: %s" % self.__dict__[key][1]
                print place + name + level + maxLevel
            upChoice = getNum(maxVal)
            if upChoice == 0:
                upChoice = random.randint(1, len(upgradeable))
            key = upgradeable[upChoice]
            self.__dict__[key][0] += 1
            print "\nUpgraded %s" % prettyDict[key]
            print "Press any key to continue..."
            getInput()


def clear():
    os.system('clear')

def getInput():
    userInput = getch()
    if userInput != '\x1b':
        return userInput
    else:
        # clear()
        print ""
        sys.exit()

def getNum(maxVal = 9):
    userInput = ""
    valid = False
    while not valid:
        try:
            userInput = int(userInput)
            valid = userInput <= maxVal
        except:
            userInput = getInput()   
    return userInput

a = LoadingBar()
while True:
    a.load()
    a.upgrade()
