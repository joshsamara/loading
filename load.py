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
        self.addedText = 0
        self.brackets = 0
        self.barStyle = 0
        self.counter = 0
        self.message = 0

        #Dynamic counter
        self.current = 0

        #Static max
        self.max = 10


    def getMessage(self):
        messages = {
        0: "2 load pres spcae alot",
        2: "Press space to load...",
        3: "Loading: Press Space to process faster."}
        return messages[self.message]

    def isLoaded(self):
        return self.current >= self.max

    def load(self):
        print self.getMessage()
        while not self.isLoaded():
            if getInput() == " ":
                self.current += 1
        print "Done"


def clear():
    os.system('clear')

def getInput():
    userInput = getch()
    if userInput != '\x1b':
        return userInput
    else:
        # clear()
        print ""
        printStats()
        sys.exit()


clear()
a = LoadingBar()
a.load()