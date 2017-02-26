import socket
import json
import views

def Main(msg):
    host = views.socketServer
    port = int(views.socketPort)
    print('connecting to '+host+':'+str(port))
    s = socket.socket()
    s.connect((host, port))

    message = json.dumps(msg)

    while message != 'q':
        s.send(message.encode())
        data = s.recv(2048).decode()

        # Data Analysis

    s.close()

def joinGame():
    message = {'action': 'join_game', 'gameID': views.gameID, 'p2_name':views.ownName}
    Main(message)
