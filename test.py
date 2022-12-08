import netaddr # install with pip install netaddr
import netifaces # install with pip install netifaces
import socket
import platform
import psutil
import threading


netifaces.interfaces()
adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr']
netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
print(f"Mon ip est {netaddr_adresse_ip}")

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

ram = psutil.virtual_memory()
print (ram)

#print(f"-- OS:{os} --", )
#print("")
#print(f"    RAM TOTALE: {ram[0]/1000000000} GB \n    RAM UTILISEE: {ram[1]/1000000000} GB \n    RAM RESTANTE: {ram [3]/1000000000} GB ")
#print("")
#print(f"-- CPU USAGE: {cpu} % --" )
#print("")
#print(f"-- Name:{name} --")
#print("")
#print(f"-- IP de votre interface réseau:{ip} --")
#print("")
#print(f"-- IP: {s} --")
