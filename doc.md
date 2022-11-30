#  Documentation de ma SAE 302


## Table Des Matières
1. [__Installation des librairies Python__](#Installation-des-librairies-Python)
2. [__Comment lancer le serveur et le client__](#Comment-lancer-le-serveur-et-le-client)
3. [__Liste des commandes possibles__](#Liste-des-commandes-possibles)
4. [__Une autre sous-puce__](#collaboration)
5. [FAQs](#faqs)

## ‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎

### Installation des librairies Python




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


### Comment lancer le serveur et le client

Vous devez d'abord commencer par lancer le serveur.py, puis le client.py

Pour lancer le serveur, il faut lancer le fichier server.py avec python3 ou python
Pour lancer le client, il faut lancer le fichier client.py avec python3 ou python

Une fois sur le serveur vous pouvez commencer à dialoguer. Le client parle en premier, et vous recevez le message sur le serveur.  
A ce moment là, vous pouvez répondre sur le serveur.

Vous pouvez également effectuer des commandes sur le serveur...

## Liste des commandes possibles
Voici un petit fichier memento pour vous indiquer les principales syntaxes que vous pouvez utiliser en markdown.
Pour voir les détails de la syntaxe, cliquez que l'icone d'édition de ce fichier.

----------------

####Mettre un mot en italique

Voici un mot *en italique* 

Votre mot se trouve entre astérisques `*mon-mot*`

-----------------

####Mettre un mot en gras

Voici un mot __en gras__ ! 

Votre mot se trouve entre deux `__underscores__` 

-----------------

####Les titres

# Titre de niveau 1 
Pour un titre de niveau 1 (h1), il faut placer un `#titre` devant votre titre.

## Titre de niveau 2
Pour un titre de niveau 2 (h2), il faut cette fois deux `##titre` devant votre titre

Et ainsi de suite jusqu'au h6.

-----------------

####Aller à la ligne en fin de phrase

Pour faire un  
changement de ligne

Votre ligne doit se terminer par 2 `espaces` pour faire ce qu'on appelle un __retour-chariot__, c'est à dire aller à la ligne.

-----------------

####Faire une liste à puces

* Une puce
* Une autre puce
* Et encore une autre puce !

Il faut simplement placer un astérisque devant les éléments de votre liste.

`* Une puce`

`* Une autre puce`

`* Et encore une autre puce !`

######Pour faire une liste ordonnée : 

1. Et de un
2. Et de deux
3. Et de trois

`1. Et de un`
`2. Et de deux`
`3. Et de trois`

######Pour imbriquer une liste dans une autre :

* Une puce
* Une autre puce
    * Une sous-puce
    * Une autre sous-puce
* Et encore une autre puce !

`* Une puce`

`* Une autre puce`

    `* Une sous-puce`
    
    `* Une autre sous-puce`
    
`* Et encore une autre puce !`

1. Une puce
2. Une autre puce
    1. Une sous-puce
    2. Une autre sous-puce
3. Et encore une autre puce !

`1. Une puce`

`2. Une autre puce`

    `1. Une sous-puce`
    
    `2. Une autre sous-puce`
    
`3. Et encore une autre puce !`

-----------------

####Faire une citation

> Ceci est un texte cité. Vous pouvez répondre
> à cette citation en écrivant un paragraphe
> normal juste en-dessous !

Il vous suffit d'ajouter un `>` devant votre citation.

`> Ceci est un texte cité. Vous pouvez répondre à cette citation en écrivant un paragraphe normal juste en-dessous !`

-----------------

####Ecrire du code

#####Un code entier

Voici un code en C :

    int main()
    {
        printf("Hello world!\n");
        return 0;
    }
    
Il vous suffit d'écrire votre phrase de présentation comme n'importe quelle phrase et d'écrire votre code à la ligne.
    
`Voici un code en C :`

    int main()
    {
        printf("Hello world!\n");
        return 0;
    }

#####Juste un morceau de code

`<h1>Titre</h1>`

Il vous suffit d'entourer votre morceau de code avec deux accents graves.
Pour faire un accent grave, il vous suffit de faire `AltGr` + `7` sur votre clavier.

-----------------

####Mettre un lien

Rendez-vous sur [Simplonline](http://www.simplonline.com) !

Il vous faut le mot sur lequel vous souhaitez faire votre lien entre crochets [ ], puis votre lien entre parenthèses ( ).

`Rendez-vous sur [Simplonline](http://www.simplonline.com) !`

-----------------

####Intégrer une image

La syntaxe est la même que pour un lien, il suffit juste d'ajouter un point d'exclamation devant les crochets. 

Ce que vous mettez entre crochet est le texte alternatif de l'image, que nous vous conseillons fortement d'intégrer à chaque fois que vous mettez une image.

Important : ça ne marche qu'avec des url d'images prises sur le web.

`![Simplon.co](http://simplon.co/wp-content/uploads/2015/04/if-coder-keep-coding-else-learn-with-simplon-2-600x675.png)`

![Simplon.co](http://simplon.co/wp-content/uploads/2015/04/if-coder-keep-coding-else-learn-with-simplon-2-600x675.png)

-----------------

####Barre de séparation

Pour faire une barre de séparation il vous suffit d'écrire plusieurs `-` d'affilé. Plus vous en mettrez plus le trait sera épais.

`-----------------`

----------------


## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [FAQs](#faqs)
### General Info
***
Write down the general informations of your project. It is worth to always put a project status in the Readme file. This is where you can add it. 
### Screenshot
![Image text](https://www.united-internet.de/fileadmin/user_upload/Brands/Downloads/Logo_IONOS_by.jpg)
## Technologies
***
A list of technologies used within the project:
* [Technologie name](https://example.com): Version 12.3 
* [Technologie name](https://example.com): Version 2.34
* [Library name](https://example.com): Version 1234
## Installation
***
A little intro about the installation. 
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```
Side information: To use the application in a special environment use ```lorem ipsum``` to start
## Collaboration
***
Give instructions on how to collaborate with your project.
> Maybe you want to write a quote in this part. 
> It should go over several rows?
> This is how you do it.
## FAQs
***
A list of frequently asked questions
1. **This is a question in bold**
Answer of the first question with _italic words_. 
2. __Second question in bold__ 
To answer this question we use an unordered list:
* First point
* Second Point
* Third point
3. **Third question in bold**
Answer of the third question with *italic words*.
4. **Fourth question in bold**
| Headline 1 in the tablehead | Headline 2 in the tablehead | Headline 3 in the tablehead |
|:--------------|:-------------:|--------------:|
| text-align left | text-align center | text-align right |