#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⢀⣀⣤⣤⣀⣀⡀⠀⢸⠃⠀⠀⠀⠀⠘⡇⠀⢀⣀⣀⣤⣤⣀⡀⠀⠀⠀
#⠀⠀⠀⢸⠉⠀⠀⠉⠉⠛⠻⣿⣤⣀⠀⠀⣀⣤⣿⠟⠛⠉⠉⠁⠈⠉⡇⠀⠀⠀
#⠀⠀⠀⠘⣧⡀⠀⠀⠀⠀⠀⣇⣀⣽⠿⠿⣯⣀⣸⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀⠀
#⠀⠀⠀⠀⠈⠻⣦⡀⠀⣠⣴⡟⠉⠀⢀⡀⠀⠉⢻⣦⣄⠀⢀⣴⠟⠁⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⢈⣿⣿⣉⠀⡇⠀⢰⣿⣿⠆⠀⢸⠀⣉⣿⣿⡁⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢀⣴⠟⠁⠀⠙⠻⣧⣀⠀⠉⠉⠀⣀⣼⠟⠋⠀⠈⠻⣦⡀⠀⠀⠀⠀
#⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⡏⠉⣻⣶⣶⣟⠉⢹⠀⠀⠀⠀⠀⠈⢻⡄⠀⠀⠀
#⠀⠀⠀⢸⣀⠀⠀⣀⣀⣤⣴⣿⠛⠉⠀⠀⠉⠛⣿⣦⣤⣀⣀⠀⠀⣀⡇⠀⠀⠀
#⠀⠀⠀⠈⠉⠛⠛⠉⠉⠁⠀⢸⡄⠀⠀⠀⠀⢠⡇⠀⠈⠉⠉⠛⠛⠉⠁⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

import os
import threading
import tkinter as tk
import os
import threading
import subprocess
import socket
import zipfile
import platform
import datetime
from tkinter import ttk
from tkinter import messagebox
import time
from termcolor import colored
import shlex
ver = 1.0
shell = "AtomShell"
import sys




#OS
def main():
        os.system("clear")
        print(colored("Welcome to Atom, the best OS simulation!\n", "blue"))
        print(colored(f"Arch ➜ {platform.machine()}", "green"))
        print(colored(f"OS ➜ {platform.platform()}", "green"))
        print(colored(f"System ➜ {platform.system()}", "green"))
        print(colored(f"Release ➜ {platform.release()}\n", "green"))
        exist = False
        user = open("config/user/username.txt", "r+").read()
        os.chdir("computer")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        cmd = ["bye", "shell", "who", "list", "read", "write", "extract", "purge","compress", "ping", "version", "mkdir", "clear", "new", "remove", "move", "where", "time", "reboot", "run", "get"]
        while True:

            prompt = input(colored(f"Atom⚛{user}({colored(time, "green")}) ❯ ", "blue"))
            if prompt not in cmd:
                print(colored("❌Error : Command not recognized!", "red"))
            else:

                if prompt == "":
                    print(colored("❌Error : Command not recognized!", "red"))
                if prompt == "bye":
                    quit()
                if prompt == "shell":
                    print(shell, ver)
                if prompt == "who":
                    print(colored(f"{user}", "green"))
                if prompt == "list":
                    list = subprocess.run(["ls"], capture_output=True, text=True)
                    print(colored(f"📂Directory ↳\n{list.stdout}", "green"))

                if prompt.startswith("extract "):
                    zip_file = prompt.split(" ", 1)[1]

                    if os.path.exists(zip_file):
                        try:
                            with zipfile.ZipFile(zip_file, "r") as archive:
                                archive.extractall()
                        except zipfile.BadZipFile:
                            print(colored(f"Error: '{zip_file}' is not a valid ZIP file", "red"))
                if prompt.startswith("compress "):
                    file_to_compress = prompt.split(" ", 1)[1]

                    if os.path.exists(file_to_compress):
                        with zipfile.ZipFile(f"{file_to_compress.split(".")[0]}.zip", "w") as archive:
                            archive.write(file_to_compress, arcname=os.path.basename(file_to_compress))
                if prompt.startswith("mkdir "):
                    dir = prompt.split(" ")
                    os.makedirs(dir[1])
                if prompt == "clear":
                    os.system("clear")
                if prompt.startswith("new "):
                    file = prompt.split(" ")
                    os.system(f"touch {file[1]}")
                if prompt.startswith("remove "):
                    e = prompt.split(" ")
                    if os.path.isdir(e[1]):
                        os.rmdir(e[1])
                    else:
                        os.remove(e[1])
                if prompt.startswith("read "):
                        e = prompt.split(" ")
                        with open(e[1], "r") as file:
                            content = file.read()
                            print(content)
                if prompt.startswith("write "):
                        e = prompt.split(" ")
                        with open(e[1], "w") as file:
                            content = file.write(f"{e[2]}")
                if prompt.startswith("move "):
                    cd = prompt.split(" ")
                    os.chdir(cd[1])
                    exist = True
                    
                if prompt == "where":
                    if exist == True:
                        print(colored(f"{cd[1]}", "green"))
                    else:
                        print(colored("computer", "green"))
                if prompt.startswith("ping "):
                    server = prompt.split(" ")
                    os.system(f"ping {server[1]}")
                if prompt.startswith("run "):
                    command = shlex.split(prompt[len("run "):])
                    command_str = " ".join(command)
                    os.system(command_str)
                if prompt.startswith("get "):
                    command = shlex.split(prompt[len("get "):])
                    command_str = " ".join(command)
                    os.system("wget "+command_str+" -P download")
                if prompt == "time":
                    print(datetime.datetime.now())
                if prompt == "reboot":
                    os.system("bash reboot.sh")

                if prompt == "version":
                    print(colored(f"Atom {ver} x86_64", "green"))
                if prompt == "purge":
                    os.system("cd - && rm -rf config/user && rm system/check && rm system/logs.txt")

#Install
def install():
    pourcent = 0
    print(colored("----------Welcome to Atom Installer----------", "blue"))
    username = input("Username ❯ ")
    if len(username) > 50:
        print(colored("❌Error : Username size > 50 characters,please change", "red"))
    else:
        
        password = input("Password ❯ ")
        os.system(f"mkdir config/user")

        while pourcent <= 100:
            if pourcent < 50:
                bar = "─"
                os.system("clear")
                print(colored(f"Kernel build ──────❯ {pourcent}%", "red"))
            else:
                os.system("clear")
                print(colored(f"Kernel build ──────❯ {pourcent}%", "green"))
                user = open(f"config/user/username.txt", "w+")
                user.write(f"{username}")
                user.close()
                passwrd = open(f"config/user/password.txt", "w+")
                passwrd.write(f"{password}")
                passwrd.close()
                shell = open(f"config/shell/shell.txt", "w+")
                shell.write(f"AtomShell")
                shell.close()
                shell = open(f"storage/cache/boot", "w+")
                shell.write("True")
                shell.close()
                logs = open("system/logs.txt", "w+")
                logs.write(f"Kernel build at {datetime.datetime.now()}")
                logs.close()
                check = open("system/check", "w+")
                check.close()
                i = open("config/interface/cli", "w+")
                i.close()
            time.sleep(0.1)
            pourcent += 1
        print(colored("Atom build succesfully!", "green"))
        os.system("python system/kernel.py")

#Boot function
def boot():
    main()

#Install Menu
def install_menu():
    os.system("clear")
    print("""                                                           
              ┌───────Welcome To Atom─────────┐             
              │1.Install                      │             
              │3.Help                         │             
              │4.Exit                         │             
              │                               │                     
              └───────────────────────────────┘             """)

    while True:
        install_prompt = input(f"\n💻 ➜ AtomInstaller({datetime.datetime.now().strftime("%H:%M:%S")}) ❯ ")
        if install_prompt in ["1", "2", "3", "4"]:

            if install_prompt == "1":
                install()
                
            if install_prompt == "3":
                os.system("cd - && clear && cat README.txt")
            if install_prompt == "4":
                quit()
        else:
            print(colored("❌Error : Please choose an option", "red"))
    else:
        install()
if os.path.exists("system/check"):
    boot()
else:
    install_menu()
