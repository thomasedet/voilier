import socket
ipserv="192.168.0.229"
port=5005
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ipserv, port))
print "waiting on port:", port
while 1:
    data, addr = s.recvfrom(5005)
    print data

