# 🗓️ Semaine 1 — On installe notre terrain de jeu

[⬅️ Retour au sommaire](README.md) · [Semaine 2 ➡️](semaine-2-reseau-bases.md)

### 🎯 Objectifs de la semaine
- Comprendre **pourquoi** on virtualise et installer une VM propre.
- Avoir un **Kali Linux** (attaquant) qui tourne.
- Être à l'aise avec **le terminal** et les **permissions** Linux.
- Écrire ton **premier script Bash**.

---

## 📘 Cours 1.1 — La virtualisation, c'est quoi ce truc ?

**Le problème.** Tu veux tester un malware, casser un système, balancer des exploits… Tu ne vas pas faire ça sur ton PC perso (sinon adieu tes photos et ton mémoire).

**La solution : la machine virtuelle (VM).** C'est un **PC simulé dans ton PC**. Tu peux tout casser dedans : si ça part en vrille, tu **restaures un snapshot** et c'est propre.

Avantages :
- Installer **Kali Linux** sans toucher à ton système.
- **Simuler un réseau complet** (un attaquant + une cible) sur une seule machine.
- **Snapshots** : tu figes un état « propre », tu expérimentes, tu reviens en arrière en 5 secondes.

**VirtualBox vs les autres**

| Outil | On aime | On aime moins | Gratuit |
|---|---|---|---|
| **VirtualBox** | Simple, multiplateforme | Un peu lent en 3D | ✅ |
| VMware Workstation Player | Très performant | Fonctions avancées payantes | ⚠️ partiel |
| Hyper-V | Intégré à Windows Pro | Windows only, cohabite mal avec VirtualBox | ✅ |

➡️ **On part sur VirtualBox** : gratuit, simple, parfait pour apprendre.

> 💡 **Astuce snapshot** : juste après l'installation de Kali, fais un snapshot « base-propre ». À chaque expérience risquée, tu pourras y revenir. C'est ta sauvegarde de jeu vidéo.

---

## 📘 Cours 1.2 — Linux, ce système d'exploitation de ouf

**Pourquoi Linux et pas Windows ?**
- **Open source** : tu vois et modifies le code.
- **Stable et léger** : tourne bien même en VM.
- **Le paradis des outils de sécu** : Kali = 600+ outils préinstallés.
- **Scriptable** : tu automatises tout en Bash ou Python.

**Kali vs Ubuntu : le match**

| Distrib | Pour quoi faire | Pour qui |
|---|---|---|
| **Kali** | Tests d'intrusion, hacking éthique | Le futur pentester (toi cette semaine) |
| **Ubuntu Server** | Admin système, défense | La cible qu'on défendra (semaines 6-7) |

➡️ Cette semaine : **Kali**. Plus tard on ajoutera **Ubuntu** et **Metasploitable** comme cibles.

**La structure des dossiers Linux**
```
/
├── bin/    # commandes de base (ls, cd, cat…)
├── etc/    # fichiers de configuration (le cerveau du système)
├── home/   # dossiers perso des utilisateurs (ton territoire)
├── var/    # logs, bases de données (le « bordel utile »)
├── tmp/    # fichiers temporaires
└── root/   # dossier du super-utilisateur (root), prudence ici
```

---

## 📘 Cours 1.3 — Le terminal, ton nouveau meilleur pote

Le **terminal** est l'outil le plus puissant de Linux. Avec lui tu lances des programmes, gères des fichiers, automatises tout.

**Les commandes à connaître ABSOLUMENT**

| Commande | À quoi ça sert | Exemple |
|---|---|---|
| `ls` | Lister fichiers/dossiers | `ls -la` (tout, même cachés) |
| `cd` | Changer de dossier | `cd /home/kali/Documents` |
| `pwd` | Où suis-je ? | `pwd` |
| `mkdir` | Créer un dossier | `mkdir cyberhero` |
| `cp` / `mv` | Copier / déplacer | `cp a.txt b.txt` |
| `rm` | **Supprimer** (⚠️) | `rm fichier.txt`, `rm -r dossier/` |
| `cat` | Afficher un fichier | `cat notes.txt` |
| `less` | Lire un gros fichier page par page | `less /var/log/syslog` |
| `grep` | Chercher du texte | `grep "error" log.txt` |
| `nano` | Éditer un fichier | `nano script.sh` |
| `chmod` | Changer les permissions | `chmod +x script.sh` |
| `sudo` | Exécuter en super-utilisateur | `sudo apt update` |
| `man` | Le manuel d'une commande | `man ls` |
| `history` | Tes dernières commandes | `history` |

> ⚠️ **DANGER `rm -rf /`** : cette commande efface TOUT. Ne la tape jamais « pour voir ». Même dans une VM, l'erreur de réflexe se paie un jour sur une vraie machine.

**Les permissions Linux** 🔐

Chaque fichier a des droits pour 3 catégories : **propriétaire (u)**, **groupe (g)**, **autres (o)**. Trois actions : **lire (r=4)**, **écrire (w=2)**, **exécuter (x=1)**.

On additionne : `rwx = 4+2+1 = 7`, `r-x = 4+0+1 = 5`, `rw- = 4+2+0 = 6`.

| Notation | u | g | o | Sens |
|---|---|---|---|---|
| `755` | rwx | r-x | r-x | Script/programme exécutable par tous |
| `644` | rw- | r-- | r-- | Fichier lisible par tous, modifiable par toi seul |
| `600` | rw- | --- | --- | Fichier privé (clé SSH, mot de passe) |

Rendre un script exécutable : `chmod +x mon_script.sh`.

---

## 🎯 Exercices Semaine 1

### Exercice 1.1 — Installe ta VM comme un pro
1. Installe [VirtualBox](https://www.virtualbox.org/).
2. Télécharge l'image **Kali Linux pour VirtualBox** sur [kali.org/get-kali](https://www.kali.org/get-kali/) (choisis *Virtual Machines → VirtualBox*, c'est préconfiguré).
3. Importe la VM, règle : **RAM 4 Go**, **CPU 2 cœurs**, **disque 25 Go dynamique**.
4. Démarre, connecte-toi (login par défaut `kali` / `kali`).
5. Mets à jour : `sudo apt update && sudo apt full-upgrade -y`.
6. **Fais un snapshot** nommé `base-propre`.
7. **Défi bonus** : change le mot de passe par défaut (`passwd`) — un vrai pro ne laisse jamais `kali/kali`.

### Exercice 1.2 — Deviens un ninja du terminal
1. Crée `~/cyberhero/` puis un fichier `notes.txt` avec `nano` :
   ```
   Salut, c'est Alexandre !
   Aujourd'hui j'ai appris à dompter le terminal comme un boss.
   ```
2. Applique les bonnes permissions : `chmod 644 notes.txt`. Vérifie avec `ls -l`.
3. Crée un alias permanent pour `ls -la` : ajoute `alias ll='ls -la'` à la fin de `~/.bashrc`, puis `source ~/.bashrc`.
4. **Défi bonus** : trouve combien de lignes contient `/etc/passwd` avec `wc -l /etc/passwd`, et à quoi sert ce fichier (`man 5 passwd`).

### Exercice 1.3 — Ton premier script Bash
1. Crée `bienvenue.sh` :
   ```bash
   #!/bin/bash
   echo "Salut, $USER ! Bienvenue chez Alex le CyberHero."
   echo "On est le $(date '+%A %d %B %Y')."
   echo "Il est $(date +%H:%M:%S)."
   echo "Il y a $(ls -1 | wc -l) éléments dans ce dossier."
   ```
2. `chmod +x bienvenue.sh` puis `./bienvenue.sh`.
3. **Défi bonus** : ajoute une ligne qui affiche ton **adresse IP locale** (`ip a | grep inet`).

---

## 🎫 Épreuve de passage — Semaine 1

Tu débloques le badge **🏆 Maître du Terminal** quand les **3** niveaux sont réussis.

### 1. 🧠 Quiz auto-corrigé (5/5)
Réponds, puis vérifie avec `./verifie.sh "ta réponse"` (minuscules, sans accents).

| # | Question | SHA-256 de la bonne réponse |
|---|---|---|
| 1 | Quelle valeur octale correspond aux permissions `rw-r--r--` ? | `87e50b28705900bb064d1e9df1bd6cf55a7efa01cc16c6cf0703f491a1f13d44` |
| 2 | Quelle commande affiche le chemin du dossier courant ? | `a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8` |
| 3 | Chemin complet du fichier listant les comptes utilisateurs locaux ? | `74acf31844532670be412c65b8251ee55d072549080b1cffdbea6b1a192230a0` |
| 4 | Quelles deux options (collées) forment la commande `rm` la plus dangereuse à combiner avec `/` ? | `686c39acd6327bbd2c7c3aeea382e60f54645a7df75a5d90af2bc01819bbaf4c` |
| 5 | Commande + option pour rendre un script exécutable (format `xxxxx +y`) ? | `d242f67f7a76ea57e7efed57cdb24dc28c6126a64033436f399d0407067e5fc8` |

### 2. 🚩 Défi du Boss
- Ta VM Kali tourne, est à jour, le mot de passe par défaut est changé, et un snapshot `base-propre` existe.
- Ton script `bienvenue.sh` s'exécute et affiche bien la date, l'heure et le nombre de fichiers.

### 3. 🏆 Badge officiel en ligne
Termine la room gratuite **TryHackMe — « Linux Fundamentals Part 1 »** : [tryhackme.com/room/linuxfundamentalspart1](https://tryhackme.com/room/linuxfundamentalspart1)
Bonus (très formateur) : **OverTheWire — Bandit**, niveaux 0 à 10 : [overthewire.org/wargames/bandit](https://overthewire.org/wargames/bandit/)

> 🆓 **Alternative 100 % gratuite** (si tu n'as pas de compte TryHackMe) : **OverTheWire — Bandit** (jeu Linux dans le navigateur, aucun compte requis) → [overthewire.org/wargames/bandit](https://overthewire.org/wargames/bandit/), et **Root-Me** (plateforme française entièrement gratuite) → [root-me.org](https://www.root-me.org/).

➡️ Les 3 réussis ? **🏆 Badge « Maître du Terminal » débloqué.** Direction la [Semaine 2](semaine-2-reseau-bases.md) !

---

## ✅ Checklist fin de Semaine 1
- [ ] Kali tourne, à jour, mot de passe changé, snapshot fait.
- [ ] Je connais 12+ commandes de base.
- [ ] Je sais lire et poser des permissions (`644`, `755`, `600`).
- [ ] Mon script Bash s'exécute.
- [ ] Quiz 5/5 + room TryHackMe terminée.
