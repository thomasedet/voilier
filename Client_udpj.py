#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import socket

#UDP_IP = "192.168.0.229" #IP Raspi
UDP_IP = "127.0.0.1"

UDP_PORT = 12800
DATAGRAM = 2
ID = 51
TAILLE = 5
SAFRAN = 23
GV = 32


MESSAGE = bytearray([ID,TAILLE,GV,SAFRAN]) #bytearray creer un tableau.

print "",
print "********************",

print "message:", MESSAGE
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "longeur du datagram : ", DATAGRAM
print "ID du systeme : ", ID
print "Taille de la trame : ", TAILLE
print "Position du safran : ", SAFRAN, "Position de la grand voile : ", GV

 
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

trame_reponse,addr = sock.recvfrom (1024) #ligne de décodage des trames.

lattitude = 

print ""
print "******REPONSE DU SERVEUR: ******"
print "ID du systeme", ord (trame_reponse[0])
print "Taille de la trame", ord (trame_reponse[1])
print "vitesse du vent", ord (trame_reponse[2])
print "Direction du vent", ord (trame_reponse[3])
print "gite du bateau", ord (trame_reponse[4])

    
