from scapy.all import *
import os

iface = "wlan0"

def h_packet(packet):
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11AssosReq):
        print("SSID identified"+ packet.info)

#turning wifi adapter to monitor mode
os.system("iwconfig " + iface + " mode monitor")

print("Sniffing traffic on interface " + iface)

#sniff is a scapy function
sniff(iface= iface, prn=h_packet)