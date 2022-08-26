import nmap
import sys


target = str(sys.argv[1])
ports = [21,22,80,139,442,445,8080]

scan_v = nmap.PortScanner()

print("\scanning", target, " for ports 21,22,80,139,443,445,8080...\n")

for port in ports:
    portscan = scan_v.scan(target,str(port))  #portscan will get dict o/p
    print("Port",port," is", portscan['scan'][target]['tcp'][port]['state'])

print("\nhost", target, " is", portscan['scan'][target]['status']['state'])