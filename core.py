#!/usr/bin/python3

#
# === License: ===
# === ISC ===
# === Copyright (c) 2016-2017, Maksim Pinigin <pinigin_official@mail.ru> ===
#

# -*- coding: utf-8 -*-
# === Importing ===
import os
import math
import datetime
import time
import panic

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
                try:
                    print("Hello, " + command[1] + "!")
                except:
                    print("Hello, World!")
            elif command[0] == "md":
                try:
                    if command[1][0] == "/":
                        os.makedirs(command[1])
                    else:
                        os.makedirs(workdir + "/" + command[1])
                except:
                    print("Usage: md [path/to/directory] or [/path/to/directory]")
            elif command[0] == "rd":
                if len(command) == 2:
                    try:
                        if command[1][0] == "/":
                            if os.path.exists(command[1]) == True:
                                os.removedirs(command[1])
                            else:
                                print("ERROR: Directory is't exists")
                        else:
                            if os.path.exists(workdir + "/" + command[1]) == True:
                                os.removedirs(workdir + "/" + command[1])
                            else:
                                print("ERROR: Directory is't exists")
                    except:
                        print("ERROR: Directory is't empty")
                else:
                    print("USAGE: rd [path/to/directory]")
            elif command[0] == "python":
                credits()
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
                print('')
            elif command[0] == "array":
                print(command[1:])
            #elif command[0] == "pfh":
            #...
            # === Official modules ===
            elif command[0] == "omod":
                # === Math ===
                try:
                    '''if command[1] == "math":
                        global primer
                        print("Math for Pinos by Maxim Pinigin. License GNU GPL")
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
                    # ==='''
                    # === LinuxCMD ===
                    if command[1] == "linuxcmd":
                        print("Get username...")
                        try:
                            login = os.getlogin()
                        except:
                            login = "user"
                        #print("Get kernel version...")
                        os.system("uname -mrs")
                        while True:
                            cmd = input(login + " $ ")
                            if cmd == "exit":
                                break
                            else:
                                os.system(cmd)
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
                try:
                    if os.path.exists(command[1]):
                        if command[1] == "-":
                            ifcd = 0
                        else:
                            ifcd = 1
                            workdir = command[1]
                            #os.chdir(command[1])
                    else:
                        print("Error. Maybe, directory is not exists?")
                except:
                    print("Usage: cd [/path/to/directory]")
            elif command[0] == "dir" or command[0] == "ls":
                try:
                    ls = os.listdir(command[1])
                    for row in ls:
                        for elem in row:
                            print(elem, end='')
                        print()
                except:
                    try:
                        ls = os.listdir(workdir)
                        for row in ls:
                            for elem in row:
                                print(elem, end='')
                            print()
                    except:
                        ls = os.listdir("/")
                        for row in ls:
                            for elem in row:
                                print(elem, end='')
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
                try:
                    try:
                        f = open(workdir + "/" + command[1], 'r')
                        readed = f.read()
                        print(readed)
                    except:
                        f = open(command[1], 'r')
                        readed = f.read()
                        print(readed)
                except:
                    print("Error. Maybe, file is not exists?")
            elif command[0] == "rf":
                try:
                    filename = command[1]
                    if os.path.exists(workdir + "/" + filename):
                        os.remove(workdir + "/" + filename)
                    else:
                        print("Errno 2: No such file or directory")
                except:
                    print("Undefined error")
            elif command[0] == "getlogin":
                print(login)
            elif command[0] == "iwf":
                try:
                    filename = command[1]
                    writedt = input("Text: ")
                    if ifcd == 1:
                        f = open(workdir + "/" + filename, 'w')
                        f.write(writedt + '\n')
                        f.close()
                        print(writedt + " >> " + workdir + "/" + filename)
                    else:
                        f = open(filename, 'w')
                        f.write(writedt + '\n')
                        f.close()
                        print(writedt + " >> " + filename)
                except:
                    print("Errno 2: No such file or directory")
            elif command[0] == "mf":
                try:
                    sourcefile = command[1]
                    newfile = command[2]
                    os.rename(workdir + "/" + sourcefile,workdir + "/" + newfile)
                except:
                    print("Error. Maybe, file(or directory?) is not exists?")
            elif command[0] == "wf":
                try:
                    filename = command[1]
                    writedt = command[2]
                    if ifcd == 1:
                        f = open(workdir + "/" + filename, 'w')
                        f.write(writedt + '\n')
                        f.close()
                        #print(writedt + ' ==> ' + workdir + "/" + filename)
                    else:
                        f = open(filename, 'w')
                        f.write(writedt + '\n')
                        f.close()
                        #print(writedt + ' ==> ' + filename)
                except:
                    print("Errno 2: No such file or directory")
            elif command[0] == "panictest":
                panic.panic("this is just test, lol")
            elif command[0] == "exit":
                print("Goodbye!")
                exit()
            else:
                print("Command not found")
# ===
