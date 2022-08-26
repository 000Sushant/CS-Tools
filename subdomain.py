import requests
import sys

#download subdomains-1000.txt from github rbsec/dnscan
sublist = open("subdomains-1000.txt").read() #sublist is string
subs = sublist.splitlines() #sub will become list

for sub in subs:
    url = f"http://{sub}.{sys.argv[1]}"
    
    try:
        requests.get(url)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain", url)


#how to use
#python subdomain.py google.com