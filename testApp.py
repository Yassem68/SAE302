from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import socket
import sys
import threading
import time
import socketserver
import platform
import psutil
import netifaces
import netaddr

os = platform.system()
ram = psutil.virtual_memory()
cpu = psutil.cpu_count()
name = socket.gethostname()
ip = socket.gethostbyname(name)
host = socket.gethostname()
ip = socket.gethostbyname(host)
netifaces.interfaces()
port = 7100
adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr'] # en0 = ethernet,si votre adresse ip est sur une autre interface il faudra changer "en0" par le nom de l'interface
netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)



class MainWindow(QMainWindow):
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
        grid.addWidget(btn, 14, 0,1,2)
        grid.addWidget(self.label, 16, 0, 1, 2)
        

        rama.clicked.connect(self.__actionram)
        cpuu.clicked.connect(self.__actioncpu)
        ipp.clicked.connect(self.__actionip)
        oss.clicked.connect(self.__actionos)
        namee.clicked.connect(self.__actionname)
        porto.clicked.connect(self.__actionport)

    def __actionip(self):
        
        self.label.append(f"-- IP de votre interface réseau:{netaddr_adresse_ip} --\n")
    
    def __actionos(self):
        
        self.label.append(f"-- OS:{os} --\n")
    
    def __actionname(self):
        
        self.label.append(f"-- Nom de la machine:{name} --\n")
    
    def __actionport(self):
       
        self.label.append(f"-- Vous êtes sur le port{port} --\n")
    
    def __actionram(self):

        self.label.append(f"RAM TOTALE: {ram[0]/1000000000} GB \nRAM UTILISEE: {ram[1]/1000000000} GB \nRAM RESTANTE: {ram [3]/1000000000} GB\n")
    
    def __actioncpu(self):
        self.label.append(f"-- CPU USAGE: {cpu} % --\n")
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

# Path: testApp.py