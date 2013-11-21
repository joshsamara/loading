#!/usr/bin/python
import sys
import os
from mygetch import *

class LoadingBar(object):
    """docstring for LoadingBar"""
    def __init__(self):
        super(LoadingBar, self).__init__()
        #levels of properties
        self.loadingText = 0
        self.finishedText = 0
        self.introText = 0
        self.brackets = 0
        self.barStyle = 0
        self.counter = 0

        #Dynamic counter
        self.current = 0

        #Static max
        self.max = 100

    def getIntroText(self):
        texts = {
        0: "hi",
        1: "Welcome",
        2: "==== Welcome to Loading Bar Sim! ==="
        }
        return texts[self.introText]

    def getLoadingText(self):
        texts = {
        0: "2 load pres spcae alot",
        1: "Press space to load...",
        2: "Loading: Press Space to process faster..."}
        return texts[self.loadingText]

    def getFinishedText(self):
        texts = {
        0: "X",
        1: "Done",
        2: "Loading Complete. Prace any key to continue..."}
        return texts[self.finishedText]


    def isLoaded(self):
        return self.current >= self.max

    def load(self):
        clear()
        self.current = 0
        print self.getIntroText()
        print self.getLoadingText()
        while not self.isLoaded():
            if getInput() == " ":
                self.current += 20
        print self.getFinishedText()
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
            if key in prettyDict and self.__dict__[key] < 2:
                upgradeable[i] = key
                i += 1

        if len(upgradeable) == 0:
            print "Fully upgraded"
            print "Press any key to continue..."
            getInput()
        else:
            print "Press the matching key to upgrade:"
            maxVal = len(upgradeable)
            for i in range(maxVal):
                place = "%s) " % i
                key = upgradeable[i]
                name  = "%-25s" % prettyDict[key]
                level = "Level: %d" % self.__dict__[key]
                print place + name + level
            upChoice = getNum(maxVal)
            key = upgradeable[upChoice]
            self.__dict__[key] += 1
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
