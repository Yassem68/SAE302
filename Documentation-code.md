<h1> Documentation code</h1>

## Table des matières

1. [__Quelle est la structure de l'application__](#Quelle-est-la-structure-de-l'application) 
2. [__Comment est architecturé mon code__](#Comment-est-architecturé-mon-code)
3. [__Qu'avez-vous fait__](#Qu'avez-vous-fait) 
4. [__Pourquoi vous n'avez pas tout fait si c'est le cas__](#Pourquoi-vous-n'avez-pas-tout-fait-si-c'est-le-cas)


## Quelle est la structure de l'application

L'application se compose d'une seule fenêtre. Cette fenêtre est divisée en deux parties. La partie supérieure est dédiée à l'affichage des messages. La partie inférieure est dédiée à l'écriture des messages.
Les commandes que vous utilisez se trouvent dans la partie inférieure. Vous pouvez les utiliser en cliquant sur les boutons correspondants.


Voici un petit schéma qui vous permettra de mieux comprendre la structure de l'application.

 -------------------------------------------
|  ______                  _____            |
| | RAM  |                | CPU |           |
|  ------                  -----            |
|  ______                  _____            |
| | IP   |                | OS  |           |
|  ------                  -----            |
|  ______                  _____            |
| | Name  |               | Ping |          |
|  ------                  -----            |
|  ______                  _____            |
| | Port  |              | Disque |         |
|  ------                  -----            |
|   __________________________________      |
|  |               Quit               |     |
|   ----------------------------------      |                            
|   __________________________________      |
|  |               Clear              |     |
|   ----------------------------------      |
|-------------------------------------------|
|                                           |
|   --------------------------------------  |
|  |                                      | |
|  |                                      | |
|  |                                      | |
|  |       Résultats des commandes        | |
|  |                                      | |
|  |                                      | |
|  |                                      | |
|   --------------------------------------  |
|                                           |
 -------------------------------------------




## Comment est architecturé mon code

### Le serveur
On peut voir que le serveur se découpe en plusieurs parties. La première ou l'on retrouve les imports, la deuxième ou l'on retrouve les variables globales, la troisième ou l'on retrouve les fonctions, et la dernière ou l'on retrouve le code principal.
La dernière partie est la plus importante elle comporte toutes les commandes qu'on peut effectuer sur le serveur. On peut voir que le serveur est composé de plusieurs fonctions. Chaque fonction correspond à une commande. On peut voir que chaque fonction est composée de plusieurs parties. La première partie est la partie qui permet de vérifier si la commande est bien entrée. La deuxième partie est la partie qui permet d'effectuer la commande. La dernière partie est la partie qui permet d'afficher le résultat de la commande.


### Le client
Sur le client on retrouve premièrement les imports, deuxièmement les variables concernant toutes les commandes disponibles, troisièmement les fonctions(qui correspondent aux commandes, comme la fonction ram ou os).
La dernière partie permet de lanceer l'application, c'est le if __name__ == "__main__":.


## Qu'avez-vous fait
Pour cette SAE j'ai effectué le projet intermédiaire. J'ai donc fait le serveur et le client, sous forme d'une application graphique. On peut cliquer sur les boutons dans l'application pour effectuer les commandes.
Cependant, je n'ai pas réussi à faire la partie difficile ou il fallait connecter plusieurs clients au serveur. J'ai donc fait une application qui ne permet de connecter qu'un seul client au serveur.
Je n'ai pas réussi à faire la commande ping. J'ai donc fait une autre commande qui permet de voir le stockage sur le disque dur.
Je pense que j'ai assez bien réussi la SAE même si j'aurai pu faire plus de choses. Je me sens assez satisfait de mon travail.


