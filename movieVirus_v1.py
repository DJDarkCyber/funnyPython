#!/usr/bin/env python3

import subprocess
import pymsgbox

def messageBox():
    smp1 = ["Ok, Go it", "Fuck Back!"]
    usrRep = pymsgbox.confirm("Your computer Got Hacked By Dr.Hecker!", "Fucked Up!", smp1)
    if usrRep == smp1[0]:
        pymsgbox.alert("You are kind about this system!")
        return "1"
    elif usrRep == smp1[1]:
        pymsgbox.alert("Your computer Going to get Fucked up again!")
        return "2"
    pymsgbox.alert("Your System Got Fucked!")

def myLittleBot():
    subprocess.call("xterm -fullscreen -e /bin/bash -l -c 'hollywood'", shell=True)
someday = messageBox()
if someday == "2":
    myLittleBot()
