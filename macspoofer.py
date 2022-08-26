#run this in linux sys
#python macspoofer.py
#sudo python macspoofer.py

import random
import os
import subprocess


def get_rand():
    return random.choice("abcdef0123456789")

def new_mac():
    mac = ""
    for i in range(0,5):
        mac += get_rand() + get_rand() + ":"
    
    mac += get_rand() + get_rand()
    return mac

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}")) #command to get only the mac address in linux

#turning eth0 down before chnaging the mac
subprocess.call(["sudo","ifconfig","eth0","down"])

#fetching newly random generated mac address
new_m = new_mac()

#assigning new mac address to eth0
subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m])
#turning the eth0 back up
subprocess.call(["sudo","ifconfig","eth0","up"])

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))