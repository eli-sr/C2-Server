#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("172.31.21.91",7000))

s.send("Data".encode("utf-8"))
res = s.recv(1024)
print(res.decode("utf-8"))


