from appJar import gui
import pygame
import sys
gui = gui("Inception Games", "600x800")

def
def joinGame(param):
    print(param)

def createGame(param):
    print(param)

def buttonPush(param):
    print(param)
    
def board(param):
    global gui

    row = 1
    
    while row < 10:
        gui.addLabel("r"+str(row)+"c1", "1", row, 0)
        gui.addLabel("r"+str(row)+"c2", "2", row, 1)
        gui.addLabel("r"+str(row)+"c3", "3", row, 2)
        gui.addLabel("r"+str(row)+"c4", "4", row, 3)
        gui.addLabel("r"+str(row)+"c5", "5", row, 4)
        gui.addLabel("r"+str(row)+"c6", "6", row, 5)
        gui.addLabel("r"+str(row)+"c7", "7", row, 6)
        gui.addLabel("r"+str(row)+"c8", "8", row, 7)
        gui.addLabel("r"+str(row)+"c9", "9", row, 8)
        row+=1
        gui.addHorizontalSeparator(4,0,9, colour="red")
        gui.addHorizontalSeparator(8,0,9, colour="red")
        gui.addVerticalSeparator(1,4, colour="red")
        gui.addVerticalSeparator(1,8, colour="red")


def viewInit():
    global gui
    # gui.setIcon("./resources/imagesTic-tac-toe.gif")
    gui.addLabel("welcomeText", "Welcome to Incpetion Games", 0, 0, 2)
    gui.addMenuList("Game", ["Create Game", "Join Game"], board)

    gui.go()
