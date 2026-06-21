# Chapitre 2 — Le réseau, comme un pro

Tout, en cybersécurité, tourne autour du réseau. Une attaque, c'est presque toujours une machine qui parle à une autre machine. Si tu comprends *comment* les ordinateurs se parlent, tu comprends où on peut écouter, mentir, ou bloquer. Ce chapitre t'explique ça en partant de zéro.

## 2.1 C'est quoi, un réseau ?

Un **réseau**, c'est simplement plusieurs ordinateurs reliés entre eux pour échanger des informations. Ta box internet à la maison relie ton téléphone, ta télé et ton PC : c'est un petit réseau. Internet, c'est le plus grand réseau du monde, fait de millions de petits réseaux reliés entre eux.

Quand deux ordinateurs s'échangent une information, ils ne s'envoient pas un gros bloc d'un coup. Ils découpent le message en petits morceaux appelés **paquets**, un peu comme on enverrait un long courrier en plusieurs enveloppes numérotées. Chaque paquet voyage de son côté, et la machine d'arrivée les remet dans l'ordre. Cette idée de « paquet » reviendra sans arrêt.

## 2.2 Le modèle en couches : un message qui voyage par étapes

### L'analogie de la lettre postale

Imagine que tu écris une lettre à un ami à l'étranger. Plusieurs personnes interviennent sans que tu les voies :

- **Toi**, tu écris le contenu de la lettre.
- Tu la mets dans une **enveloppe** avec l'adresse.
- **La Poste** de ton pays décide par quel chemin l'envoyer.
- **Les avions et les camions** la transportent physiquement.
- À l'arrivée, tout se fait dans l'autre sens : transport, tri, enveloppe ouverte, lettre lue.

Chaque acteur a un rôle précis et ne s'occupe pas du travail des autres. Le facteur n'a pas besoin de lire ta lettre pour la livrer. Internet fonctionne exactement comme ça : par **couches**, chacune avec son rôle, empilées les unes sur les autres.

### Le modèle OSI : 7 couches

Les informaticiens ont défini un modèle de référence à **7 couches**, appelé le **modèle OSI**. Tu n'as pas besoin de le réciter par cœur tout de suite, mais tu dois comprendre l'idée : un message descend les 7 couches chez l'expéditeur, voyage, puis remonte les 7 couches chez le destinataire.

| Couche | Nom | Son rôle, en simple | Exemple |
| --- | --- | --- | --- |
| 7 | Application | Là où vit le programme que tu utilises | Ton navigateur web |
| 6 | Présentation | Chiffre et met en forme les données | Le cadenas HTTPS |
| 5 | Session | Ouvre et ferme la conversation | — |
| 4 | Transport | Vérifie que tout arrive en entier | TCP, UDP |
| 3 | Réseau | Trouve le chemin entre les machines | Les adresses IP |
| 2 | Liaison | Parle aux machines juste à côté | Le câble, le Wi-Fi |
| 1 | Physique | Le signal réel : électricité, ondes | La prise réseau |

> À retenir : un message traverse des couches, de la plus proche de l'humain (couche 7, l'application) à la plus proche du matériel (couche 1, le câble). Chaque couche a un seul rôle.

### Pourquoi ça compte en sécurité

Quand une attaque arrive, savoir à quelle couche elle frappe te dit comment te défendre. Un faux site web qui te vole ton mot de passe, c'est la couche 7. Une inondation de fausses connexions pour saturer un serveur, c'est plutôt la couche 4. Quelqu'un qui se fait passer pour ta box sur le Wi-Fi, c'est la couche 2. Le modèle OSI est ta **carte mentale** : il te dit *où* regarder.

### Le modèle TCP/IP : la version courte

En vrai, dans la pratique, on simplifie les 7 couches OSI en **4 couches**, qu'on appelle le modèle **TCP/IP** (c'est le modèle réellement utilisé sur Internet).

| Couche TCP/IP | Correspond à | Exemples |
| --- | --- | --- |
| Application | OSI 7, 6, 5 | Web, mail, DNS |
| Transport | OSI 4 | TCP, UDP |
| Internet | OSI 3 | IP |
| Accès réseau | OSI 2, 1 | Wi-Fi, câble |

## 2.3 TCP et UDP : deux façons d'envoyer

À la couche transport, il existe deux grandes méthodes pour envoyer des paquets.

- **TCP** est la méthode **fiable**. Avant d'envoyer, les deux machines se mettent d'accord. Pour chaque paquet reçu, la machine d'arrivée renvoie un petit « bien reçu ». Si un paquet se perd, on le renvoie. C'est comme une lettre recommandée avec accusé de réception : lent, mais sûr. On l'utilise pour le web, les mails, les transferts de fichiers.
- **UDP** est la méthode **rapide**. On envoie les paquets sans vérifier qu'ils arrivent. C'est comme jeter des cartes postales dans une boîte : certaines peuvent se perdre, mais c'est rapide et léger. On l'utilise pour la vidéo en direct, les jeux en ligne, le DNS.

### La poignée de main TCP

Pour ouvrir une connexion TCP, les deux machines font un petit rituel en trois temps, appelé *3-way handshake* (poignée de main en trois étapes) :

1. La machine A dit : « Salut, je veux te parler » (message **SYN**).
2. La machine B répond : « OK, je t'entends, et toi tu m'entends ? » (message **SYN-ACK**).
3. La machine A confirme : « Oui, c'est parti » (message **ACK**).

Retiens cette séquence **SYN, SYN-ACK, ACK** : on la retrouvera en analysant du trafic, et certaines attaques consistent justement à abuser de cette poignée de main.

> À retenir : TCP est fiable et confirme chaque paquet ; UDP est rapide mais sans garantie. Toute connexion TCP commence par la poignée de main SYN, SYN-ACK, ACK.

## 2.4 L'adresse IP : l'adresse postale d'une machine

Pour qu'une machine en trouve une autre, il lui faut une **adresse**. C'est l'**adresse IP** (IP veut dire *Internet Protocol*).

Une adresse IP classique (version 4, dite IPv4) ressemble à ça :

```
192.168.1.10
```

C'est quatre nombres entre 0 et 255, séparés par des points. Chaque machine sur un réseau a la sienne, comme chaque maison a une adresse postale unique dans sa rue.

### Adresses privées et adresses publiques

Il y a deux mondes :

- Les **adresses privées** sont utilisées *à l'intérieur* d'un réseau local (ta maison, une entreprise). Elles ne sont pas visibles depuis Internet. On les reconnaît : elles commencent souvent par `192.168.`, `10.`, ou `172.16` à `172.31`. C'est comme le numéro d'un bureau à l'intérieur d'une entreprise : utile dedans, inconnu dehors.
- Les **adresses publiques** sont visibles sur Internet. C'est l'adresse que ta box présente au monde entier.

Deux adresses spéciales à connaître :

- `127.0.0.1` : c'est **toi-même**, ta propre machine. On l'appelle l'adresse de *loopback* (boucle locale). Quand un programme veut se parler à lui-même, il utilise cette adresse.
- `255.255.255.255` : c'est l'adresse de **diffusion** (*broadcast*), qui parle à tout le monde sur le réseau en même temps.

## 2.5 Le masque de sous-réseau : qui est mon voisin ?

### Le problème

Quand ta machine veut envoyer un paquet, elle doit savoir une chose : la destination est-elle **dans mon réseau** (mon voisin direct), ou **ailleurs** (il faut passer par la box) ? Pour répondre, elle utilise le **masque de sous-réseau**.

### L'analogie de l'immeuble

Pense à une adresse comme « Immeuble 192.168.1, Appartement 10 ». Le masque, c'est ce qui sépare la partie « immeuble » de la partie « appartement ». Si deux personnes sont dans le **même immeuble**, elles peuvent se parler directement dans le couloir. Si elles sont dans des immeubles différents, il faut passer par la rue (la box, qu'on appelle la *passerelle* ou *gateway*).

Un masque très courant est `255.255.255.0`, qu'on écrit aussi `/24`. Le `/24` veut dire : « les 24 premiers bits désignent l'immeuble (le réseau), le reste désigne l'appartement (la machine) ».

### Un petit calcul simple

Avec un `/24`, sur l'adresse `192.168.1.10` :

- L'**adresse du réseau** (le nom de l'immeuble) est `192.168.1.0`.
- Les **machines possibles** vont de `192.168.1.1` à `192.168.1.254`.
- L'**adresse de diffusion** (parler à tout l'immeuble) est `192.168.1.255`.

Pour calculer combien de machines un réseau peut contenir : on compte les bits laissés aux machines, et on fait « 2 puissance ce nombre, moins 2 ». Pour un `/24`, il reste 8 bits, donc 2 puissance 8 = 256, moins 2 = **254 machines**. Pourquoi moins 2 ? Parce qu'on enlève l'adresse du réseau et l'adresse de diffusion, qui ne sont pas attribuables à une vraie machine.

| Notation | Masque | Machines possibles |
| --- | --- | --- |
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |

> À retenir : le masque sépare la partie « réseau » de la partie « machine » d'une adresse IP. Il sert à savoir si une machine est ton voisin direct ou s'il faut passer par la passerelle.

## 2.6 Les protocoles et les ports : des langages et des portes

### Les protocoles, ce sont des langages

Une fois que deux machines se trouvent, encore faut-il qu'elles se comprennent. Pour ça, elles parlent un langage commun appelé **protocole** : un ensemble de règles précises. Le web parle le protocole **HTTP**, les mails parlent **SMTP**, etc.

### Les ports, ce sont des portes numérotées

Une seule machine peut faire plusieurs choses en même temps : héberger un site web, recevoir des mails, accepter des connexions à distance. Pour ne pas tout mélanger, chaque service écoute derrière une **porte numérotée** appelée **port**.

Reprends l'image de l'immeuble : l'adresse IP, c'est l'immeuble ; le port, c'est le numéro de l'appartement où vit un service précis. Le service web habite traditionnellement à l'appartement (port) 80, le service web sécurisé au 443, et ainsi de suite.

Voici les ports à connaître absolument, comme tu connais les numéros d'urgence :

| Protocole | Port | À quoi il sert | Sécurisé ? |
| --- | --- | --- | --- |
| HTTP | 80 | Naviguer sur le web | Non, en clair |
| HTTPS | 443 | Web avec cadenas | Oui, chiffré |
| SSH | 22 | Se connecter à distance | Oui |
| FTP | 21 | Transférer des fichiers | Non, vieux |
| DNS | 53 | Traduire un nom en adresse IP | À surveiller |
| SMTP | 25 | Envoyer des mails | À surveiller |
| RDP | 3389 | Bureau à distance Windows | À surveiller |

> À retenir : l'adresse IP désigne la machine, le port désigne le service sur cette machine. Quand tu entends « le port 22 est ouvert », pense aussitôt « SSH, on peut s'y connecter à distance ».

## 2.7 Le DNS : l'annuaire d'Internet

Tu ne tapes jamais `142.250.179.78` pour aller sur Google : tu tapes `google.com`. Mais les machines, elles, ne travaillent qu'avec des adresses IP. Il faut donc un **traducteur** entre les noms (faciles pour les humains) et les adresses (utiles pour les machines). Ce traducteur, c'est le **DNS** (*Domain Name System*).

Le DNS est exactement comme l'annuaire téléphonique d'autrefois : tu connais le nom de quelqu'un, l'annuaire te donne son numéro. Tu connais `google.com`, le DNS te donne l'adresse IP correspondante.

Quand tu tapes une adresse dans ton navigateur, ta machine demande discrètement au DNS « quelle est l'adresse de ce nom ? », reçoit la réponse, puis se connecte. Tout ça en une fraction de seconde, sans que tu le voies.

Comme le DNS est au cœur de tout, c'est une cible favorite des attaquants : s'ils arrivent à te mentir sur l'adresse d'un site (« non non, la vraie banque, c'est cette adresse-là »), ils peuvent t'envoyer sur un faux site. On en reparlera dans la partie défense.

## Ce qu'il faut retenir de ce chapitre

- Un réseau découpe les messages en **paquets** qui voyagent puis sont rassemblés.
- Le modèle en **couches** (OSI à 7 couches, TCP/IP à 4) répartit les rôles : application, transport, réseau, accès.
- **TCP** est fiable, **UDP** est rapide ; TCP commence par la poignée de main SYN, SYN-ACK, ACK.
- L'**adresse IP** identifie une machine ; le **masque** dit qui est dans le même réseau.
- Le **port** identifie un service ; apprends les ports courants (22, 80, 443, 53).
- Le **DNS** traduit les noms en adresses, comme un annuaire.

Au prochain chapitre, on passe à la pratique de l'observation : on va « écouter » le réseau et explorer une machine à distance.
