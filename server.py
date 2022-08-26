#send a message to whoever is listining on port 4444 then emideately close the socket

import socket

host = socket.gethostname()
port = 4444

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #STREAM is for tcp and DGRAM is for udp 
sock_.bind((host,port))
sock_.listen(1) #max number of 1 connection

print("\nServer started...\n")

conn,addr = sock_.accept() #for accepting the connection and fetching the addr of client

print("Connection established with ",str(addr))

msg = "\nThank you for connecting "+str(addr)
conn.send(msg.encode("ascii"))
conn.close()

