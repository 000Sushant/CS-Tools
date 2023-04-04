# CS-Tools
cyber security tools written in python


## dictionary_attack.py

Get the wordlist from: [Common Password List ( rockyou.txt ) | Kaggle](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)

dictionary_attack.py file, as suggested by it's name, can be used to perform dictionary attack on any given post request. You can change the word list, and target from the python code.

## hashcracker.py

Library used: [hashlib — Secure hashes and message digests — Python 3.11.2 documentation](https://docs.python.org/3/library/hashlib.html)

The code provided, can be used to undo md5 hashes. Moreover, the code can be customized as well to solve achieve type of hashing algorithm. To know more about what are the other hashes you can solve, visit the library documentation.

## hiddenwifi.py

To run this script you must have an NIC capable of running monitor mode. check the interface if the card, then assign the variable iface  with that particular interface.

**How to check the network interface**

You can run this command in terminal/CMD to know on which interface your network is running.

**Windows**
```powershell
ipconfig
```

**Linux**
```bash
ifconfig
```

## inforecon.py
Fetching details from: [ipinfo](https://ipinfo.io/)

This script can be used to extract the physical location of an IP, through its hosted domain.

## macspoofer.py

This script can be used for changing the MAC address in a Linux OS. It will assign new randomly generated MAC address to the system. If you want to assign a perticular address, you can comment out the new_mac( ) and get_rand( ), then assign the desired address to mac variable. 

## nmapscanner.py

Library used: [python-nmap · PyPI](https://pypi.org/project/python-nmap/)

Nmap manual: [Nmap(1) - Linux man page (die.net)](https://linux.die.net/man/1/nmap)

A simple nmap port scanning, you just need specify the port in port list and it will give you the live status of the port. This script particularly has the potential to achieve more. However, it provides nothing special, but the Nmap features we all know. So, this script can be manipulated by the person who possess the knowledge of Nmap. 

## portscanner.py

The final result of nmapscanner.py and portscanner.py will be same as it also scans the specified port. set the lower port limit(lpr) and upper port limit(hpr) in the code and it will scan the port status of all ports from lpr to upr. The only difference is that this script is written using typical socket programming.

## subdomain.py

Get wordlist from: [dnscan/subdomains-1000.txt at master · rbsec/dnscan (github.com)](https://github.com/rbsec/dnscan/blob/master/subdomains-1000.txt)

This scripts simply performs the dictionary attack to gives you a list of valid sub domains of the given domain name.

## synflooding.py

This script performs DoS attack on the desired target IP. set the source as the attacker IP and target variable as the target's IP. You can target any specific port by changing the dport variable. 
