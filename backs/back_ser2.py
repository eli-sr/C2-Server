#!/usr/bin/env python3
import socket
import threading

connections = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.31.21.91",7000))
s.listen()

def live(conn):
    while True:
        data = conn.recv(1024)
        print(data.decode("utf-8"))
        #conn.sendall(data)
        try:
            conn.sendall("Data received".encode("utf-8"))
        except:
            break

while True:
    conn, addr = s.accept()
    connections.append(conn)
    x = threading.Thread(target=live, args=(conn,))
    x.start()
