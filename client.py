import socket

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #STREAM is for tcp and DGRAM is for udp
sock_.connect((socket.gethostname(),4444))
msg = sock_.recv(1024) #1024 bytes
print(msg.decode("ascii"))