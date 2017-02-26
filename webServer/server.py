#!/usr/bin/env python

import socket, threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print("[+] New thread started for "+ip+":"+str(port))

    def run(self):
        print("Connection from : "+ip+":"+str(port))

        clientsock.send(str("connected").encode())

        data = "dummydata"

        while len(data):
            data = clientsock.recv(2048).decode('utf-8')
            print("Client sent : "+data)
            # Data Analysis
            clientsock.send(("You sent me : "+data).encode())

        print("Client disconnected...")

host = "localhost"
port = 5555

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print("\nListening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
