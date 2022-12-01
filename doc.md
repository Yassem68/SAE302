<h1> Documentation utilisateur</h1>


## Table Des Matières
1. [__Comment installer les outils nécéssaires__](#Comment-installer-les-outils-nécéssaires)
2. [__Comment démarrer les outils__](#Comment-démarrer-les-outils)
3. [__Comment utiliser le client__](#Comment-utiliser-le-client)




## Comment installer les outils nécéssaires




<pre>Pour faire fonctionner les programmes correctement, veuillez installer les librairies suivantes : </pre>


```pip install netaddr     /    pip3 install netaddr```   
```pip install netifaces     /    pip3 install netifaces```    
```pip install socket     /    pip3 install socket```   
```pip install threading     /    pip3 install threading```     
```pip install time     /    pip3 install time```    
```pip install os     /    pip3 install os```    
```pip install sys     /    pip3 install sys```   
```pip install psutil     /    pip3 install psutil``` ( pour afficher les perfomances du système )       
```pip install platform     /    pip3 install platform```(pour afficher l'OS)  

##

## Comment démarrer les outils

Vous devez d'abord commencer par lancer le serveur.py, puis le client.py

Pour lancer le serveur, il faut lancer le fichier server.py avec python3 ou python
Pour lancer le client, il faut lancer le fichier client.py avec python3 ou python

Une fois sur le serveur vous pouvez commencer à dialoguer. Le client parle en premier, et vous recevez le message sur le serveur.  
A ce moment là, vous pouvez répondre sur le serveur.

Vous pouvez également effectuer des commandes sur le serveur...

##

## Comment utiliser le client
Le client est la partie qui envoie les messages au serveur.   
Il est possible de faire des commandes sur le serveur, mais aussi de faire des commandes sur le client.

Les commandes sont les suivantes:

   <pre> 
    - help : affiche les commandes disponibles  
    - bye : permet de quitter le client  
    - arret : permet d'arrêter le serveur  
    - ram : permet d'afficher la ram utilisée  
    - cpu : permet d'afficher le cpu utilisé  
    - os : permet d'afficher l'OS  
    - ip : permet d'afficher l'ip du client  
    - ping : permet de ping un ip  
    - port : permet de scanner un port  
    - disque : permet d'afficher l'espace disque utilisé  </pre>

Vous pouvez également utiliser ces commandes directement sur *l'application* en cliquant sur les boutons correspondants.

