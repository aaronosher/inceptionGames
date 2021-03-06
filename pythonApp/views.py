from appJar import gui
import requests
import socketConnect

gui = gui("Inception Games", "800x600")
gameID = ""
ownName = ""
socketServer = "localhost"
socketPort = "5555"


def viewInit():
    global gui

    gui.setFont(20)
    gui.setIcon("./resources/images/Tic-tac-toe.gif")
    gui.addMenuList("Game", ["Create Game", "Join Game"], menuButtonPush)

    # Dev menu
    gui.addMenuList("Developer", ["dev_server_set", "dev_server_port_set"], devMenuButtonPush)

    gui.addLabel("welcomeText", "Welcome to Incpetion Games", 0, 0, 2)
    gui.addLabel("decisionText", "Would you like to create or join a game?", 1, 0, 2)
    gui.addButton("Create Game", createGamePart1, 4, 0)
    gui.addButton("Join Game", joinGame, 4, 1)

    gui.go()

def menuButtonPush(item):
    if item is "Create Game":
        createGamePart1()
    elif item is "Join Game":
        joinGame()

def createGamePart1(param):
    global gui
    gui.removeAllWidgets()
    gui.setTitle("Iception Games | Create a Game")
    gui.addLabel("createGameTex1", "Create a Game", 0, 0, 2)
    gui.addEntry("name", 1, 0, 2)
    gui.setEntryDefault("name", "What is your name?")
    gui.addButton("Create Game", createGamePart2, 2, 0, 2)

def createGamePart2(param):
    global gui
    global ownName
    ownName = gui.getEntry("name")
    gui.removeAllWidgets()

    socketConnect.createGame()

def createGamePart3():
    global gui
    global ownName
    global gameID
    print('GameID: '+gameID)

    gui.setTitle("Iception Games | Waiting for Player... | Game ID: "+gameID)
    gui.addLabel("waitingForGameText1", "Hi "+ownName+", you have succesfully created a game.", 0, 0, 2)
    gui.addLabel("waitingForGameText2", "Share your game ID with a friend to get started.", 1, 0, 2)
    gui.addLabel("waitingForGameText3", "Your Game ID is: "+gameID+".", 2, 0, 2)
    gui.infoBox("Waiting for Player...", "Your Game ID is: "+gameID+".")

    # Wait for another player to join the game

    # Start the Game

def joinGame(param):
    global gui
    gui.removeAllWidgets()
    gui.setTitle("Iception Games | Join a Game")
    gui.addLabel("joinGameText1", "Join a game. Enter your name and Game ID below", 0, 0, 2)
    gui.addEntry("name", 1, 0, 2)
    gui.setEntryDefault("name", "What is your name?")
    gui.addEntry("gameID", 2, 0, 2)
    gui.setEntryDefault("gameID", "Enter Game ID")
    gui.addButton("Join Game", connectToGame, 3, 0, 2)

def connectToGame(param):
    global gui
    global gameID
    global ownName
    gui.setTitle("Inception Games | Connecting...")
    gui.setEntryState("name", "disabled")
    gui.setEntryState("gameID", "disabled")
    gui.setButtonState("Join Game", "disabled")
    gameID = gui.getEntry("gameID")
    ownName = gui.getEntry("name")
    socketConnect.joinGame()

def devMenuButtonPush(menuItem):
    global gui
    global socketServer
    global socketPort
    if menuItem is "dev_server_set":
        socketServer = str(gui.textBox('dev_server', 'set dev_server'))
    elif menuItem is "dev_server_port_set":
        socketServer = str(gui.textBox('dev_server_port', 'set dev_server_port'))
