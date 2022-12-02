from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import socket
import sys
import time
import socketserver
import platform
import psutil
import netifaces
import netaddr
import shutil


os = ("")
cpu = psutil.cpu_count()
name =("")
ip = socket.gethostbyname(name)
host = socket.gethostname()
netifaces.interfaces()
stockage = ("")
adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr'] # en0 = ethernet,si votre adresse ip est sur une autre interface il faudra changer "en0" par le nom de l'interface
netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
stockage = shutil.disk_usage("/")
help =""


port = 7000





class client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SAE 302")
        self.setFixedSize(325, 540)
        grid = QGridLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(grid)


        rama = QPushButton("RAM")
        cpuu = QPushButton("CPU")
        ipp = QPushButton("IP")
        oss = QPushButton("OS")
        namee = QPushButton("Name")
        pingg = QPushButton("Ping")
        porto= QPushButton("Port")
        disque = QPushButton("Disque")
        btn = QPushButton("Quit")
        self.label = QTextEdit("")
        help = QPushButton("Help")
        clear = QPushButton("Clear")
        

#PARTIE GRID
    
        grid.addWidget(rama, 0, 0)
        grid.addWidget(cpuu, 0, 1)
        grid.addWidget(ipp, 1, 0)
        grid.addWidget(oss, 1, 1)
        grid.addWidget(namee, 2, 0)
        grid.addWidget(pingg, 2, 1)
        grid.addWidget(porto, 3, 0)
        grid.addWidget(disque, 3, 1)
        grid.addWidget(btn, 4,0,1,2)
        grid.addWidget(clear, 5,0,1,2)
        grid.addWidget(self.label, 18, 0, 1, 2)
        grid.addWidget(help, 20, 0, 1, 2)
        
#PARTIE DES ACTIONS

        rama.clicked.connect(self.__actionram)
        cpuu.clicked.connect(self.__actioncpu)
        ipp.clicked.connect(self.__actionip)
        oss.clicked.connect(self.__actionos)
        namee.clicked.connect(self.__actionname)
        porto.clicked.connect(self.__actionport)
        disque.clicked.connect(self.__actiondisque)
        help.clicked.connect(self.__actionhelp)
        clear.clicked.connect(self.__actionclear)
        btn.clicked.connect(self.__actionbtn)

#PARTIE FONCTION

    def __actionram(self):
        message = "ram"
        client_socket.send(message.encode())
        print("La requête pour la ram a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"{data}\n")
        
    def __actionbtn(self):
        message= "arret"
        client_socket.send(message.encode())
        print("Le serveur se ferme")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.close()

    def __actionip(self):
        message = "ip"
        client_socket.send(message.encode())
        print("La requête pour l'ip a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"-- IP: {data} --\n")
    
    def __actionos(self):
        message = "os"
        client_socket.send(message.encode())
        print("La requête pour l'os a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"-- OS: {data} --\n")
        
    
    def __actionname(self):
        message = "name"
        client_socket.send(message.encode())
        print("La requête pour le nom a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"-- Name: {data} --\n")
    
    def __actiondisque(self):
        message = "stockage"
        client_socket.send(message.encode())
        print ("La requête pour le stockage a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"-- Disque: {data} --\n")

        
    
    
    def __actionport(self):
       
        self.label.append(f"-- Vous êtes sur le port{port} --\n")
    
   
    def __actioncpu(self):
        self.label.append(f"-- CPU USAGE: {cpu} % --\n")
        
  

    def __actionclear(self):
        self.label.clear()
        self.label.append("")

    def __actionhelp(self):
        message = QMessageBox()
        message.setText("Commande disponible:\n \n - La commande ram permet d'afficher la ram totale, la ram utilisée et la ram libre \
            \n \n - La commande ip permet d'afficher l'adresse ip de la machine \
            \n \n  - La commande os permet d'afficher le nom de l'os\
            \n \n - La commande name permet d'afficher le nom de la machine\
            \n \n - La commande port permet d'afficher le port utilisé  \
            \n \n - La commande cpu permet d'afficher le nombre de coeur de la machine \
            \n \n - La commande disque permet d'afficher le stockage total, le stockage utilisé et le stockage libre")
        message.exec()


if __name__ == "__main__":

    print(f"Ouverture de la socket sur le serveur {host} port {port}")
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Serveur est connecté")

    app = QApplication(sys.argv)
    window = client()
    window.show()
    app.exec()

# Path: testApp.py