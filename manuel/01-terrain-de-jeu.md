# Chapitre 1 — On installe notre terrain de jeu

Dans ce chapitre, tu vas comprendre trois choses : ce qu'est une *machine virtuelle*, pourquoi on utilise *Linux*, et comment parler à un ordinateur en écrivant du texte dans un *terminal*. À la fin, tu auras un véritable laboratoire de hacker sur ton ordinateur, sans aucun risque pour tes fichiers personnels.

## 1.1 La machine virtuelle : un ordinateur dans ton ordinateur

### Le problème qu'on veut résoudre

Pour apprendre la sécurité, tu vas faire des choses « dangereuses » : lancer des programmes d'attaque, casser des systèmes, tester des virus. Si tu fais ça directement sur ton ordinateur de tous les jours, tu risques de tout casser : tes photos, tes documents, ton système.

La solution s'appelle la **machine virtuelle**, qu'on abrège **VM** (de l'anglais *Virtual Machine*).

### L'analogie du simulateur de vol

Un pilote d'avion ne s'entraîne pas à atterrir en tempête avec de vrais passagers à bord. Il utilise un **simulateur** : un faux cockpit où il peut tout rater, s'écraser dix fois, sans aucun danger. Le lendemain, le simulateur est comme neuf.

Une machine virtuelle, c'est exactement ça : un **faux ordinateur** qui vit *à l'intérieur* de ton vrai ordinateur. C'est un programme qui fait semblant d'être un PC complet, avec son propre disque dur, sa propre mémoire, son propre système. Tu peux tout casser dedans : tu fermes la fenêtre, tu redémarres, et tout est propre.

### Comment c'est possible ?

Ton ordinateur est puissant. Il peut « prêter » une partie de sa puissance (par exemple 4 Go de mémoire et 2 cœurs de processeur) à un programme spécial appelé **hyperviseur**. Cet hyperviseur crée un espace isolé et y fait tourner un autre système d'exploitation, comme si c'était une vraie machine.

L'hyperviseur qu'on va utiliser s'appelle **VirtualBox**. Il est gratuit et fonctionne sur Windows, Mac et Linux.

> À retenir : une machine virtuelle est un ordinateur complet simulé par un logiciel. Ce qui se passe dedans reste dedans. C'est ton bac à sable : tu peux tout y casser sans danger.

### Le super-pouvoir : les instantanés (snapshots)

VirtualBox sait prendre une **photo** de l'état complet de ta machine virtuelle à un instant donné. On appelle ça un *snapshot* (instantané). 

Imagine un point de sauvegarde dans un jeu vidéo. Avant un passage difficile, tu sauvegardes. Si tu meurs, tu recharges la sauvegarde. Ici, c'est pareil : avant de tester quelque chose de risqué, tu prends un snapshot. Si ça tourne mal, tu reviens à l'instantané en quelques secondes, comme si rien ne s'était passé.

## 1.2 Linux : le système des informaticiens

### Trois systèmes d'exploitation, trois philosophies

Un **système d'exploitation** (en anglais *OS*, pour *Operating System*) est le programme principal qui fait tourner ton ordinateur : Windows, macOS et Linux sont des systèmes d'exploitation. C'est le chef d'orchestre qui gère l'écran, le clavier, les fichiers, les autres programmes.

Tu connais sûrement Windows. En sécurité, on utilise surtout **Linux**. Pourquoi ?

- **Linux est ouvert (open source).** Cela veut dire que n'importe qui peut lire le code qui le compose. Rien n'est caché. Pour des gens dont le métier est la confiance et la sécurité, c'est précieux.
- **Linux est gratuit et léger.** Il tourne très bien dans une machine virtuelle, même avec peu de mémoire.
- **Linux est le pays des outils de sécurité.** La plupart des outils de hacking sont faits d'abord pour Linux.
- **Linux s'automatise facilement.** On peut écrire de petits programmes (des *scripts*) qui font le travail répétitif à ta place.

### Kali : la trousse à outils du pentester

Linux existe en plusieurs versions, qu'on appelle des **distributions** (ou *distros*). C'est comme une même voiture vendue en plusieurs finitions.

- **Kali Linux** est une distribution faite *spécialement* pour la sécurité offensive. Elle arrive avec plus de 600 outils déjà installés. C'est la trousse à outils du hacker éthique. C'est celle qu'on installe cette semaine.
- **Ubuntu** est une distribution généraliste, simple, qu'on utilise souvent comme *serveur* à défendre. On l'ajoutera plus tard, dans la partie défense.

### Comment Linux range ses fichiers

Sous Windows, tu as l'habitude des lecteurs `C:` et `D:`. Sous Linux, c'est différent : **tout part d'un seul point**, qu'on appelle la **racine** et qu'on note avec une simple barre oblique : `/`.

À partir de cette racine, tout est rangé dans des dossiers. Voici les plus importants :

- `/bin` : les commandes de base du système (les outils livrés avec).
- `/etc` : tous les fichiers de **réglage** (la configuration). C'est le cerveau des réglages.
- `/home` : les dossiers personnels des utilisateurs. Ton territoire à toi.
- `/var` : les fichiers qui grossissent avec le temps, surtout les **journaux** (*logs*). On y reviendra beaucoup en semaine 7.
- `/root` : le dossier personnel du super-chef du système (l'utilisateur *root*).

> À retenir : sous Linux, tout descend d'un seul dossier racine noté `/`. Les réglages sont dans `/etc`, tes fichiers dans `/home`, et les traces du système dans `/var`.

## 1.3 Le terminal : parler à la machine avec des mots

### Cliquer, c'est bien ; écrire, c'est puissant

Tu as l'habitude de cliquer sur des icônes avec ta souris. C'est confortable, mais limité : tu ne peux faire que ce que les boutons proposent.

Le **terminal** (cette fenêtre noire avec du texte qui fait peur au début) est une autre façon de commander l'ordinateur : tu **écris** ce que tu veux, et la machine le fait. C'est plus puissant parce que tu peux tout faire, combiner des actions, et les automatiser.

### L'analogie du restaurant

Cliquer sur des boutons, c'est comme choisir un menu en pointant les photos du doigt : pratique, mais tu es limité aux photos affichées. Le terminal, c'est comme **parler directement au chef** et lui décrire exactement le plat que tu veux. Au début c'est intimidant, mais tu obtiens précisément ce que tu demandes.

Chaque ligne que tu écris s'appelle une **commande**. Tu tapes la commande, tu appuies sur Entrée, la machine répond.

### Les commandes de survie

Voici les commandes que tu utiliseras tous les jours. Apprends-les comme tu as appris l'alphabet.

| Commande | Ce qu'elle fait | Exemple |
| --- | --- | --- |
| `pwd` | Affiche où tu te trouves (le dossier courant) | `pwd` |
| `ls` | Liste ce qu'il y a dans le dossier | `ls -la` |
| `cd` | Change de dossier (se déplacer) | `cd /home` |
| `mkdir` | Crée un nouveau dossier | `mkdir test` |
| `cat` | Affiche le contenu d'un fichier | `cat notes.txt` |
| `nano` | Ouvre un éditeur pour écrire dans un fichier | `nano notes.txt` |
| `rm` | Supprime un fichier (attention, définitif) | `rm vieux.txt` |
| `cp` | Copie un fichier | `cp a.txt b.txt` |
| `mv` | Déplace ou renomme un fichier | `mv a.txt b.txt` |
| `sudo` | Exécute une commande en mode super-chef | `sudo apt update` |
| `man` | Affiche le mode d'emploi d'une commande | `man ls` |

Petite explication de deux d'entre elles, parce qu'elles reviennent sans arrêt :

- `ls -la` : le `ls` liste les fichiers. Le `-la` ajoute des **options** : `l` pour afficher les détails (taille, date, droits) et `a` pour montrer *aussi* les fichiers cachés. En Linux, un fichier dont le nom commence par un point (comme `.bashrc`) est caché par défaut.
- `sudo` veut dire « *super user do* », c'est-à-dire « fais ceci en tant que super-utilisateur ». Certaines actions (installer un programme, modifier le système) demandent les droits du chef. `sudo` te les donne le temps d'une commande. C'est comme passer une carte d'accès « administrateur » devant un lecteur.

### Le danger à connaître par cœur

Une commande peut effacer des fichiers. La plus dangereuse de toutes est celle-ci :

```
rm -rf /
```

Décortiquons-la pour comprendre pourquoi elle est terrible. `rm` supprime. `-r` veut dire « et tout ce qu'il y a à l'intérieur, en descendant dans tous les sous-dossiers ». `-f` veut dire « force, ne me pose aucune question ». Et `/` est la racine, c'est-à-dire **tout le système**. Cette commande dit donc : « supprime absolument tout, sans rien me demander ». 

> À retenir : ne tape jamais `rm -rf /` « pour voir ». Même dans une machine virtuelle, prends l'habitude de te méfier de `rm`. Un mauvais réflexe pris dans le bac à sable peut un jour coûter cher sur une vraie machine.

## 1.4 Les permissions : qui a le droit de faire quoi

### Pourquoi des permissions ?

Sur un ordinateur, plusieurs personnes (ou plusieurs programmes) peuvent vivre ensemble. On ne veut pas que n'importe qui puisse lire le journal intime de n'importe qui, ni modifier les réglages du système. Linux gère donc des **permissions** : pour chaque fichier, il note qui a le droit de quoi.

### Les trois droits et les trois groupes

Il y a **trois droits** possibles sur un fichier :

- **lire** (en anglais *read*, abrégé `r`) : voir le contenu.
- **écrire** (*write*, abrégé `w`) : modifier le contenu.
- **exécuter** (*execute*, abrégé `x`) : lancer le fichier s'il s'agit d'un programme.

Et ces droits sont donnés à **trois catégories** de personnes :

- le **propriétaire** du fichier (celui qui l'a créé),
- le **groupe** (une équipe d'utilisateurs),
- les **autres** (tout le reste du monde).

### Les chiffres magiques (644, 755...)

Tu verras souvent des permissions écrites avec trois chiffres, comme `644` ou `755`. Voici l'astuce pour les lire. On donne une valeur à chaque droit : lire vaut **4**, écrire vaut **2**, exécuter vaut **1**. On additionne pour obtenir le chiffre d'une catégorie.

- Lire + écrire + exécuter = 4 + 2 + 1 = **7** (tous les droits).
- Lire + écrire = 4 + 2 = **6**.
- Lire + exécuter = 4 + 1 = **5**.
- Lire seul = **4**.

On met ensuite un chiffre par catégorie, dans l'ordre propriétaire / groupe / autres.

| Permission | Propriétaire | Groupe | Autres | Quand l'utiliser |
| --- | --- | --- | --- | --- |
| `644` | lire + écrire (6) | lire (4) | lire (4) | Un fichier de texte normal |
| `755` | tous (7) | lire + exécuter (5) | lire + exécuter (5) | Un programme que tout le monde peut lancer |
| `600` | lire + écrire (6) | rien (0) | rien (0) | Un fichier secret (mot de passe, clé) |

Pour changer les permissions, on utilise la commande `chmod` (de *change mode*). Par exemple, pour rendre un script lançable : `chmod +x mon_script.sh`. Le `+x` ajoute le droit d'exécution.

> À retenir : 4 = lire, 2 = écrire, 1 = exécuter. On additionne, et on écrit un chiffre par catégorie (propriétaire, groupe, autres). `chmod +x` rend un fichier exécutable.

## 1.5 Ton premier script

Un **script** est un fichier qui contient une liste de commandes. Au lieu de taper les commandes une par une, tu les écris dans un fichier et tu lances le fichier : toutes les commandes s'exécutent d'un coup. C'est ta première automatisation.

Un script commence toujours par une ligne spéciale appelée *shebang* :

```
#!/bin/bash
```

Cette ligne dit à l'ordinateur : « le programme qui doit lire ce fichier s'appelle `bash` » (bash est le nom du terminal Linux le plus courant). Ensuite, tu écris tes commandes, une par ligne. Pour pouvoir lancer le script, tu le rends exécutable avec `chmod +x`, puis tu l'appelles avec `./mon_script.sh` (le `./` veut dire « le fichier qui est ici, dans le dossier courant »).

Tu mettras tout ça en pratique dans le cahier d'exercices de la semaine 1.

## Ce qu'il faut retenir de ce chapitre

- Une **machine virtuelle** est un ordinateur simulé : ton bac à sable sans risque.
- Les **snapshots** sont des points de sauvegarde : prends-en avant chaque expérience risquée.
- **Linux** est le système des pros de la sécurité ; **Kali** est sa version « trousse à outils ».
- Le **terminal** te laisse commander la machine en écrivant ; c'est plus puissant que la souris.
- Les **permissions** (`644`, `755`, `600`) décident qui peut lire, écrire ou exécuter.
- Un **script** automatise une série de commandes.

Passe maintenant au cahier d'exercices de la semaine 1 pour installer ta VM et fabriquer ton premier script. Quand tu reviens, on attaque le réseau.
