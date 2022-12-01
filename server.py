import sys
from PyQt6.QtWidgets import QApplication, QWidget #pip install PyQt6
import psutil #pip install psutil # https://pypi.org/project/psutil/ # https://psutil.readthedocs.io/en/latest/ 
import platform #pip install platform # https://pypi.org/project/platform/ # https://docs.python.org/3/library/platform.html
import socket #pip install socket # https://pypi.org/project/socket/ # https://docs.python.org/3/library/socket.html
import netifaces #pip install netifaces # https://pypi.org/project/netifaces/ # https://netifaces.readthedocs.io/en/latest/
import netaddr #pip install netaddr # https://pypi.org/project/netaddr/ # https://netaddr.readthedocs.io/en/latest/
import os

import socket
import sys


os = platform.system()
ram = psutil.virtual_memory() 
ram1 = ram[0]/1000000000
ram2 = ram[1]/1000000000
ram3 = ram[3]/1000000000
cpu = psutil.cpu_count()
name = socket.gethostname()
ip = socket.gethostbyname(name)
host = socket.gethostname()
ip = socket.gethostbyname(host)
adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr'] # en0 = ethernet,si votre adresse ip est sur une autre interface il faudra changer "en0" par le nom de l'interface
netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)

host = "localhost" # "", "127.0.0.1
port = 7001

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print('En attente du client')
conn, address = server_socket.accept()
print(f'Client connecté {address}')

data = conn.recv(1024).decode()
 
while data != "arret":
    if data == "arret" or data == "arret":
        break

    elif data == "ram":
        reply = str(f"RAM TOTAL: {ram1/10000000}, {ram2}, RAM  : {ram3}")
        conn.send(reply.encode())
        print("Message ram envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu : {data}")

   

    elif data == "cpu":
        reply = str(cpu)
        conn.send(reply.encode())
        print("Message cpu envoyé")
        data = conn.recv(1024).decode()
        print(f"Message envoyé")


    elif data == "name":
        reply = str(name)
        conn.send(reply.encode())
        print("Message name envoyé")
        data = conn.recv(1024).decode()
        print(f"Message envoyé")

    
    elif data == "ip":
        reply = str(netaddr_adresse_ip)
        conn.send(reply.encode())
        print("Message ip envoyé")
        data = conn.recv(1024).decode()
        print(f"Message envoyé")


    elif data == "os":
        reply = str(os)
        conn.send(reply.encode())
        print("Message os envoyé")
        data = conn.recv(1024).decode()
        print(f"Message envoyé")

    else:
        message = input("Message au client ->")
        print("Message envoyé")
        conn.send(message.encode())
        data = conn.recv(1024).decode()
        print(f"Message du client :{message}")
    



# Fermeture
conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket serveur")


    



