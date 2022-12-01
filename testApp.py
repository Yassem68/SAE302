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
name = socket.gethostname()
ip = socket.gethostbyname(name)
host = socket.gethostname()
netifaces.interfaces()
port = 7001
adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr'] # en0 = ethernet,si votre adresse ip est sur une autre interface il faudra changer "en0" par le nom de l'interface
netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
stockage = shutil.disk_usage("/")


print(f"{stockage[0] /1000000000} , {stockage[1]/1000000000}, {stockage[2]/1000000000} " )






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
        btn.clicked.connect(QApplication.instance().quit)
        self.label = QTextEdit("")
        


    
        grid.addWidget(rama, 0, 0, 1, 2)
        grid.addWidget(cpuu, 2, 0,1,2)
        grid.addWidget(ipp, 4, 0,1,2)
        grid.addWidget(oss, 6, 0,1,2)
        grid.addWidget(namee, 8, 0, 1, 2)
        grid.addWidget(pingg, 10, 0, 1, 2)
        grid.addWidget(porto, 12, 0, 1, 2)
        grid.addWidget(btn, 16, 0,1,2)
        grid.addWidget(disque, 14, 0, 1, 2)
        grid.addWidget(self.label, 18, 0, 1, 2)
        

        rama.clicked.connect(self.__actionram)
        cpuu.clicked.connect(self.__actioncpu)
        ipp.clicked.connect(self.__actionip)
        oss.clicked.connect(self.__actionos)
        namee.clicked.connect(self.__actionname)
        porto.clicked.connect(self.__actionport)
        disque.clicked.connect(self.__actiondisque)

    def __actionram(self):
        message = "ram"
        client_socket.send(message.encode())
        print("La requête pour la ram a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"{data}\n")
        

    def __actionip(self):
        message = "ip"
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"-- IP: {data} --\n")
    
    def __actionos(self):
        
        self.label.append(f"-- OS: {platform.platform()} --\n")
    
    def __actionname(self):
        
        self.label.append(f"-- Nom de la machine:{name} --\n")
    
    def __actionport(self):
       
        self.label.append(f"-- Vous êtes sur le port{port} --\n")
    
   
    def __actioncpu(self):
        self.label.append(f"-- CPU USAGE: {cpu} % --\n")
        
    def __actiondisque(self):
        self.label.append(f"Stockage TOTAL: {round(stockage [0]/1000000000, 2)} GB \nStockage UTILISE: {round(stockage[1]/1000000000,2)} GB \nStockage RESTANT: {round(stockage [2]/1000000000,2)} GB\n")



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