#!/usr/bin/env python

import socket, threading
import json
from game import game

class ClientThread(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print("[+] New thread started for "+ip+":"+str(port))

    def run(self):
        global gameInstances
        print("Connection from : "+ip+":"+str(port))

        # clientsock.send(str("connected").encode())

        data = "dummydata"

        while len(data):
            data = clientsock.recv(2048).decode('utf-8')
            print("Client sent : "+data)
            received = json.loads(data)
            messageToSend = ""
            # New Game
            if received['action'] == 'create':
                print('creating new game')
                newGame = game({'name': received['name'], 'socket': self})
                messageToSend = json.dumps({'status': 'created', 'gameID': newGame.game_id})
                gameInstances[newGame.game_id] = newGame
                clientsock.send((messageToSend).encode())

            if received['action'] == 'waiting for player':
                print('host is waiting.')

            if received['action'] == 'join_game':
                print('joining game')
                if received['gameID'] not in gameInstances.keys():
                    messageToSend = json.dumps({'status': 'game_not_found'})
                    clientsock.send((messageToSend).encode())
                    continue
                newGame = gameInstances[received['gameID']]
                newGame.guest_socket == self
                newGame.guest_player['name'] = received['p2_name']
                newGame.host_socket.sendMessage(json.dumps({'status': 'client_connected', 'guest_name': newGame.guest_player['name']}))
                messageToSend = json.dumps({'status': 'connected'})
                clientsock.send(str(messageToSend))

        print("Client disconnected...")

    def sendMessage(self, message):
        print('external message: '+message)
        self.socket.sendmsg(message.encode('utf-8'))

host = "localhost"
port = 5555

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []
gameInstances = {}


while True:
    tcpsock.listen(4)
    print("\nListening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
