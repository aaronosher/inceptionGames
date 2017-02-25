import socket
import sys
from _thread import *
import os.path
import json


host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('waiting for a connection')

def threaded_client(conn):
    msg = {'state': 'connected'}
    conn.send(str.encode(json.dumps(msg)))

    while True:
        data = conn.recv(2048)
        if not data:
            break
        print('Data Recieved: '+data.decode('utf-8'))
        recieved = json.loads(data.decode('utf-8').strip())

        if not recieved['action']:
            break

        elif recieved['action'] == str("join_game"):
            reply = joinGame(recieved)

        elif recieved['action'] == str("create_game"):
            reply = createGame(recieved)

        else:
            print('no valid actions')
            break

        conn.sendall(str.encode(reply))

    conn.close()

def joinGame(data):
    gameID = data['gameID']
    p2_name = data['p2_name']
    if os.path.isfile('./games/'+gameID+'.incept'):
        gameFile = open('./games/'+gameID+'.incept', 'r')
        game = json.loads(gameFile.read())
        if not game['p2']:
            game['p2'] = p2_name
            gameFile.close()
            gameFile = open('./games/'+gameID+'.incept', 'w')
            gameFile.write(json.dumps(game))
            gameFile.close()
            return str(json.dumps(game))
    else:
        error = {'error': 'invalid gameID'}
        return str(json.dumps(error))

def createGame(data):
    return false

while True:
    conn, addr = s.accept()
    print('connection to:'+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client, (conn, ))
