import socket
import json
import views
import threading

def Main(msg):
    host = views.socketServer
    port = int(views.socketPort)
    print('connecting to '+host+':'+str(port))
    s = socket.socket()
    s.connect((host, port))

    message = json.dumps(msg)

    while message != 'q':
        s.send(message.encode())
        data = s.recv(2048).decode('utf-8')
        print('data: '+data)
        recieved = json.loads(data)
        if recieved['status'] == 'created':
            views.gameID = recieved['gameID']
            message = json.dumps({'action': "waiting for player"})
            game = threading.Thread(target=views.createGamePart3())

        elif recieved['status'] == 'connected':
            message = json.dumps({'action': 'connected'})

        elif recieved['status'] == 'game_not_found':
            views.gui.warningBox("Invalid Game ID", "That game ID doesn't seem right. Please confirm it with your buddy.")
            message = 'q'
            views.joinGame('errorBox')


        print("To Send:"+message)

        # if recieved['status'] is 'move'

    s.close()

def joinGame():
    message = {'action': 'join_game', 'gameID': views.gameID, 'p2_name':views.ownName}
    Main(message)

def createGame():
    message = {'action': 'create', 'name': views.ownName }
    Main(message)
