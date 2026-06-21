# Chapitre 7 — Surveiller et détecter

Aucune défense n'est parfaite. Un attaquant déterminé finira peut-être par entrer. La question n'est donc pas seulement « comment l'empêcher ? », mais aussi « comment **le voir** quand il essaie, et **réagir** ? ». C'est le métier de la surveillance, le cœur du travail d'un analyste en sécurité.

## 7.1 Les journaux : la mémoire de la machine

### Tout laisse une trace

Chaque action importante sur une machine est notée quelque part : une connexion, une erreur, un programme qui démarre. Ces notes s'appellent les **journaux** (en anglais *logs*). C'est la mémoire écrite du système, comme le registre d'un hôtel où l'on note chaque entrée et sortie.

Sous Linux, les journaux vivent dans le dossier `/var/log`. Quelques fichiers importants :

| Fichier | Ce qu'il contient |
| --- | --- |
| `/var/log/auth.log` | Les connexions et tentatives de connexion |
| `/var/log/syslog` | Les messages généraux du système |
| `access.log` | Les visites d'un site web |

### Lire les journaux intelligemment

Un journal peut contenir des dizaines de milliers de lignes. On ne les lit pas une par une : on les **filtre**. Avec des commandes comme `grep` (chercher un mot), `awk` (extraire une colonne) et quelques autres, on peut par exemple sortir, en une seule ligne, la liste des adresses qui ont **échoué** à se connecter, classées de la plus insistante à la moins insistante.

C'est exactement ce que fait un analyste quand il enquête : il pose une question précise aux journaux, et les journaux répondent. Savoir lire les logs est une compétence de base ultra-recherchée.

> À retenir : les journaux sont la mémoire de la machine. Savoir les lire et les filtrer (avec grep, awk...) est la compétence fondamentale de la détection.

## 7.2 Les systèmes de détection d'intrusion (IDS / IPS)

Lire les journaux à la main, c'est bien pour enquêter, mais on ne peut pas rester les yeux dessus 24 heures sur 24. On installe donc des **gardiens automatiques**.

- Un **IDS** (*Intrusion Detection System*, système de détection d'intrusion) surveille et **donne l'alerte** quand il repère quelque chose de suspect. C'est une caméra avec alarme : elle prévient, mais n'agit pas.
- Un **IPS** (*Intrusion Prevention System*, système de prévention) va plus loin : il détecte **et bloque** automatiquement. C'est la caméra qui, en plus de sonner, ferme la grille toute seule.

Ces gardiens existent en deux saveurs : ceux qui surveillent le **réseau** (le trafic qui circule, comme Suricata ou Snort) et ceux qui surveillent une **machine** précise (ses fichiers, ses journaux).

### Deux façons de repérer le danger

- **Par signatures** : le gardien connaît une liste de « visages » d'attaques déjà répertoriées et sonne quand il en reconnaît une. Très efficace contre le connu, mais aveugle face à une attaque toute neuve.
- **Par anomalies** : le gardien apprend d'abord à quoi ressemble une journée **normale**, puis sonne dès que quelque chose sort de l'ordinaire. Capable de repérer l'inconnu, mais il se trompe parfois (fausses alertes).

## 7.3 Le SIEM : la tour de contrôle

Dans une vraie organisation, il y a des dizaines, voire des milliers de machines, chacune produisant ses journaux. Impossible de tout suivre séparément. On utilise alors un **SIEM**.

Un **SIEM** (les lettres signifient *Security Information and Event Management*) est une **tour de contrôle** qui rassemble les journaux de tout le parc au même endroit, les met en relation, et lève des alertes. Pense à la tour de contrôle d'un aéroport qui voit tous les avions sur un seul écran au lieu de surveiller chaque piste séparément.

### La magie de la corrélation

La vraie force d'un SIEM, c'est la **corrélation** : relier des événements qui, séparément, sembleraient anodins.

Un exemple : un échec de connexion, ce n'est rien. Mais **200 échecs en une minute** depuis la même adresse, **suivis d'une connexion réussie**, c'est l'histoire complète d'un mot de passe finalement deviné. Le SIEM relie ces points et lève une alerte rouge, là où un humain n'aurait vu que des lignes isolées. C'est en reliant les indices qu'on découvre une attaque.

Un SIEM open source très utilisé pour apprendre s'appelle **Wazuh**. Tu en installeras un dans le cahier d'exercices.

> À retenir : un SIEM centralise tous les journaux et **corrèle** les événements pour révéler une attaque que chaque ligne, prise seule, ne montrerait pas. C'est la tour de contrôle de la sécurité.

## 7.4 Le métier qui se cache derrière : analyste SOC

Tout ce que tu apprends dans ce chapitre porte un nom de métier : **analyste SOC**. Un **SOC** (*Security Operations Center*, centre des opérations de sécurité) est l'équipe qui surveille en permanence les systèmes d'une organisation, lit les alertes du SIEM, enquête, et réagit.

C'est l'un des **premiers postes** accessibles quand on sort d'une école de cybersécurité. En maîtrisant la lecture de journaux et le fonctionnement d'un SIEM **avant même de commencer ton Master**, tu prends une vraie longueur d'avance.

## Ce qu'il faut retenir de ce chapitre

- Les **journaux** sont la mémoire de la machine ; savoir les filtrer est une compétence clé.
- Un **IDS** alerte, un **IPS** alerte **et** bloque.
- On détecte **par signatures** (le connu) ou **par anomalies** (l'inhabituel).
- Un **SIEM** centralise les journaux et les **corrèle** pour révéler les attaques.
- Tout ça, c'est le métier d'**analyste SOC**, une excellente porte d'entrée dans la profession.

Tu sais maintenant fermer les portes ET repérer les intrus. Au dernier chapitre, on assemble tout : on gère une vraie crise du début à la fin.
