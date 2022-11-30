import socket
import sys
import time
import socketserver
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

host = "localhost" # "", "127.0.0.1
port = 7100




    




print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

message = input("Message au serveur ->")
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print(f"Message du serveur : {data}")
while message != "bye" or data != "bye":
    message = input("Message au serveur ->")
    client_socket.send(message.encode())
    print("Message envoyé")
    data = client_socket.recv(1024).decode()
    print(f"Message du serveur : {data}")
    if message == "bye" or data == "bye":
        break
    if data == "arret" or message == "arret":
        break
   




# Fermeture de la socket du client
client_socket.close()
print("Socket fermée")



