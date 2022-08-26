import sys                          #to use command line arguments
import requests
import socket
import json

#if any argument is not provided print the following and exit
if len(sys.argv) < 2:
    print("\nUsage: " + sys.argv[0] + " \"<url>\" ")
    sys.exit(1)

#checking if the user has entered an ip address insted of host name
if sys.argv[1].count(".") >= 3:
    print("\nUsage: " + sys.argv[0] + " \"DomainName.TLD\" ")
    sys.exit(1)


req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

#getting ip address by the host name
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is:" + gethostby_ + "\n")

#getting the physical location of the ip using "ipinfo.io" api
req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.loads(req_two.text)

print("location: "+resp_['loc'])
print("Region: "+resp_['region'])
print("City: "+resp_['city'])
print("Country: "+resp_['country'])
