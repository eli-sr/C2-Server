#!/usr/bin/env python3
import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.31.21.91",7000))
s.listen()
conn, addr = s.accept()
data = conn.recv(1024)
print(data.decode("utf-8"))
#conn.sendall(data)
conn.sendall("Data received".encode("utf-8"))

