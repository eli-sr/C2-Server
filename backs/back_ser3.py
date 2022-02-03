#!/usr/bin/env python3
import socket
import threading

#DEV
from time import sleep
connections = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.31.21.91",7000))
s.listen()

#def live(conn):
#    while True:
#        sleep(2)
#        conn.sendall("Data sended".encode("utf-8"))

def catcher(s):
    while True:
        conn, addr = s.accept()
        connections.append(conn)
        print(addr,"added")
#        x = threading.Thread(target=live, args=(conn,))
#        x.start()

com = input(">>>")
x = threading.Thread(target=catcher, args=(s,))
x.start()


