from appJar import gui

view = gui("Inception Games", "600x800")

def joinGame(param):
    print(param)

def createGame(param):
    print(param)

def buttonPush(param):
    print(param)

def viewInit(gui):
    # gui.setIcon("./resources/imagesTic-tac-toe.gif")
    gui.addLabel("title", "Welcome to Incpetion Games", 0, 0, 2)
    gui.addMenuList("Game", ["Create Game", "Join Game"], buttonPush)

    gui.go()
