# -*-coding:Latin-1 -*
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import codecs
import socket

#IP_Serv = "192.168.0.229" #IP Raspi
IP_Serv = "127.0.0.1"
port = 12800

ide = 65
taille = 5
vvent = 50
dvent = 128
gite = 12
lattitude=1554250
longitude=1562583

b3=00
b2=17
b1=B7
b0=4A

a=00
b=17
c=D7
d=D7

sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind ((IP_Serv, port))

while True:

    data,addr = sock.recvfrom (1024) #ligne de décodage des trames.
    print "ID du systeme", ord (data[0])
    print "Taille de la trame", ord (data[1])
    print "Position de la GV", ord (data[2])
    print "Position du safran", ord (data[3])

    trame_reponse = bytearray([ide, taille, vvent, dvent, gite,b0,b1,b2,b3]) #bytearray creer un tableau.
            
    sock.sendto(trame_reponse, addr)
