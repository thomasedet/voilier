 
import socket   #for sockets
Ip="192.168.0.229"
port=5005
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("salut",(Ip,port))
