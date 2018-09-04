#!/usr/bin/env python3

#
# === License: ISC ===
# === Copyright (c) 2016-2018, Maksim Pinigin <pinigin@nvie.ru> ===
#

# -*- coding: utf-8 -*-
# === Importing ===
import os
import math
import datetime
import time

# === Variables ===
global text
global command
global workdir
global ifcd
global login
global username
try:
    workdir = os.getcwd()
    ifcd = 1
except:
    workdir = 0
    ifcd = 0
# ===

# pinos variables
os.putenv("SHELL", "/bin/pinos")

try:
    login = os.getlogin()
except:
    login = "user"

# === Shell ===
while True:

        if login == "root":
            if ifcd == 1:
                text = input("# " + workdir + ": ")
            else:
                text = input("# /: ")
        else:
            if ifcd == 1:
                text = input("$ " + workdir + ": ")
            else:
                text = input("$ /: ")

        if text:
            command = text.split(' ') # SCS

            if command[0] == "hello":
                if len(command) == 2:
                    print("Hello, " + command[1] + "!")
                else:
                    print("Hello, World!")
            elif command[0] == "md":
                if len(command) == 2:
                    try:
                        os.makedirs(command[1])
                    except:
                        print("ERROR: Directory exists or access denied")
                else:
                    print("USAGE: md [path/to/directory]")
            elif command[0] == "rd":
                if len(command) == 2:
                    try:
                        if os.path.exists(command[1]) == True:
                            os.rmdir(command[1])
                        else:
                            print("ERROR: Directory is't exists or access denied")
                    except:
                        print("ERROR: Directory is't empty")
                else:
                    print("USAGE: rd [path/to/directory]")
            elif command[0] == "python":
                copyright()
            elif command[0] == "python_commands":
                help()
            elif command[0] == "pinos":
                print('')
                print('88""Yb 88 88b 88  dP"Yb  .dP"Y8      dP"Yb')
                print('88__dP 88 88Yb88 dP   Yb `Ybo."     dP   Yb')
                print('88"""  88 88 Y88 Yb   dP o.`Y8b     Yb   dP')
                print('88     88 88  Y8  YbodP  8bodP      YbodP')
                print('')
                print("Pinos 0 Pre-alpha master")
                print("Copyright (c) 2016-2018, Maksim Pinigin <maksim@pinig.in>")
                print('')
            elif command[0] == "array":
                print(command[1:])
            #elif command[0] == "pfh":
            #...
            # === Official modules ===
            elif command[0] == "omod":
                # === Math ===
                try:
                    if command[1] == "oldmath": # from 2016
                        global primer
                        print("Math for Pinos by Maxim Pinigin. License ISC")
                        print("Copyright (c) 2016, Maksim Pinigin <maksim@pinig.in>")
                        while True:
                            primer = input("Math> ")
                            if primer == "exit":
                                break
                            elif primer == "+":
                                one = int(input("One: "))
                                two = int(input("Two: "))
                                otv = one+two
                                print(otv)
                            elif primer == "-":
                                one = int(input("One: "))
                                two = int(input("Two: "))
                                otv = one-two
                                print(otv)
                            elif primer == "/":
                                one = int(input("One: "))
                                two = int(input("Two: "))
                                otv = one/two
                                print(otv)
                            elif primer == "*":
                                one = int(input("One: "))
                                two = int(input("Two: "))
                                otv = one*two
                                print(otv)
                            elif primer == "pi":
                                print(math.pi)
                            elif primer == "help":
                                print("+ or - or / or * or pi")
                            else:
                                print("Unknown command")
                    # ===
                    # ===
                    else:
                        print("Module is not found.")
                except:
                    print("Error!")
            # ===
            elif command[0] == "math":
                print("Math for Pinos by Maxim Pinigin.")
                while True:
                    textmath = input("Math> ")
                    commandmath = textmath.split(' ')
                    if commandmath[0] == "exit":
                        break
                    try:
                        if commandmath[1] == "+":
                            one = int(commandmath[0])
                            two = int(commandmath[2])
                            otv = one+two
                            print(otv)
                        elif commandmath[1] == "-":
                            one = int(commandmath[0])
                            two = int(commandmath[2])
                            otv = one-two
                            print(otv)
                        elif commandmath[1] == "/":
                            one = int(commandmath[0])
                            two = int(commandmath[2])
                            otv = one/two
                            print(otv)
                        elif commandmath[1] == "*":
                            one = int(commandmath[0])
                            two = int(commandmath[2])
                            otv = one*two
                            print(otv)
                    except:
                        print("Error")
            elif command[0] == "cd":
                if len(command) == 2:
                    try:
                        os.chdir(command[1])
                        workdir = os.getcwd()
                    except:
                        print("ERROR: Directory is't exists")
                else:
                    print("USAGE: cd [/path/to/directory]")
            elif command[0] == "dir" or command[0] == "ls":
                if len(command) > 1:
                    ls = os.listdir(command[1])
                else:
                    ls = os.listdir(workdir)

                column = 0
                for row in ls:
                    for elem in row:
                        print(elem, end='')
                    print(end="  ")
                    column = column + 1
                    if column == 5:
                        column = 0
                        print()
                if column != 0 and column != 5:
                    print()
            # Phew...
            #elif command[0] == "chmod":
            #    try:
            #        try:
            #            mode = command[1]
            #            filename = command[2]
            #            #group = command[3]
            #            os.chmod(workdir + "/" + filename,mode)
            #        except:
            #            print("FATAL ERROR!1")
            #    except:
            #        print("Error. Maybe, file(or directory?) is not exists?")
            #elif command[0] == "chown":
            #    try:
            #        try:
            #            filename = command[1]
            #            owner = command[2]
            #            group = command[3]
            #            os.chown(workdir + "/" + filename,owner,group)
            #        except:
            #            print("FATAL ERROR!1")
            #    except:
            #        print("Error. Maybe, file(or directory?) is not exists?")
            elif command[0] == "vf":
                if len(command) == 2:
                    file_to_open = command[1]
                    try:
                        f = open(file_to_open, 'r')
                        readed = f.read()
                        print(readed)
                        f.close()
                    except:
                        print("ERROR: File is't exists or access denied")
                else:
                    print("USAGE: vf [path/to/file]")
            elif command[0] == "rf":
                if len(command) == 2:
                    file_to_delete = command[1]
                    try:
                        os.remove(file_to_delete)
                    except:
                        print("ERROR: File is't exists or access denied")
                else:
                    print("USAGE: rf [path/to/file]")
            elif command[0] == "getlogin":
                print(login)
            elif command[0] == "mf":
                if len(command) == 3:
                    file_to_move = command[1]
                    new_name = command[2]
                    try:
                        os.rename(file_to_move, new_name)
                    except:
                        print("ERROR: File is't exists or access denied")
                else:
                    print("USAGE: mf [old/path] [new/path]")
            elif command[0] == "wf":
                if len(command) > 2:
                    text_to_write = text.replace('wf ' + command[1] + ' ', '')
                    filename = command[1]
                    if os.path.exists(filename) == True:
                        f = open(filename, 'r')
                        old_text = f.read()
                        f.close()
                        try:
                            f = open(filename, 'w')
                            f.write(old_text + "\n" + text_to_write)
                            f.close()
                        except:
                            print("ERROR: Access denied or directory is't exists")
                    else:
                        try:
                            f = open(filename, 'w')
                            f.write(text_to_write)
                            f.close()
                        except:
                            print("ERROR: Access denied or directory is't exists")
                else:
                    print("USAGE: wf [file] [text..]")
            elif command[0] == "exit":
                print("Goodbye!")
                exit()
            else:
                os.system(text)
# ===
