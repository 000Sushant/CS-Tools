import socket

#enter host name for scanning
ip_host = str(input("which website you want to scan? "))

#connecting host name to IPv4
ip_addr = socket.gethostbyname(ip_host)

lpr = 21 #lower port range
hpr = 35  #high port range

for port in range(lpr, hpr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((ip_addr, port))
    #connect_ex(): return an error in case of any exception
    #connect(): raise an exception. in case of no error, return 0

    if(status == 0):
        print('Port ', port, ' is OPEN!!')
    else:
        print('Port ',port, ' is CLOSED!!')
    s.close()

print('PORT SCANNING DONE!!')