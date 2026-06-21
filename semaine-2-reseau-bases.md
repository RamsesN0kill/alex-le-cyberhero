# 🗓️ Semaine 2 — Les bases du réseau, comme un pro

[⬅️ Semaine 1](semaine-1-terrain-de-jeu.md) · [Sommaire](README.md) · [Semaine 3 ➡️](semaine-3-observation-reseau.md)

### 🎯 Objectifs de la semaine
- Comprendre **OSI** et **TCP/IP**.
- Lire une **adresse IP**, un **masque**, calculer un **sous-réseau**.
- Connaître les **protocoles et ports** essentiels.
- Manipuler `ping`, `ip`, `ss`, `dig`.

---

## 📘 Cours 2.1 — Les modèles OSI et TCP/IP

**Le modèle OSI : 7 couches, comme un gâteau** 🍰

| # | Couche | Rôle (version simple) | Exemple |
|---|---|---|---|
| 7 | Application | Là où vit ton navigateur/appli | HTTP, FTP, SMTP, DNS |
| 6 | Présentation | Chiffrement, compression, format | SSL/TLS |
| 5 | Session | Gère l'ouverture/fermeture de connexion | NetBIOS |
| 4 | Transport | Livraison fiable ou rapide | TCP, UDP |
| 3 | Réseau | Trouve le chemin (le GPS) | IP, ICMP |
| 2 | Liaison | Communication entre voisins directs | Ethernet, MAC |
| 1 | Physique | Câbles, Wi-Fi, signaux | RJ45, Wi-Fi |

**Moyen mnémotechnique** : *« All People Seem To Need Data Processing »* (couche 7→1).

**Le modèle TCP/IP : la version qu'on utilise vraiment** (4 couches)

| Couche TCP/IP | Couches OSI | Protocoles |
|---|---|---|
| Application | 7,6,5 | HTTP, DNS, SSH |
| Transport | 4 | TCP, UDP |
| Internet | 3 | IP, ICMP |
| Accès réseau | 2,1 | Ethernet, Wi-Fi |

> 🧠 **Pourquoi c'est utile en sécu ?** Quand tu analyses une attaque, tu dois savoir **à quelle couche** elle frappe : un SYN flood = couche 4 ; un XSS = couche 7 ; un ARP spoofing = couche 2. OSI, c'est ta carte mentale.

**TCP vs UDP**

| | TCP | UDP |
|---|---|---|
| Fiabilité | Garantie (accusés de réception) | Aucune garantie |
| Vitesse | Plus lent | Très rapide |
| Usage | Web, mail, SSH | Streaming, DNS, jeux |

Le **3-way handshake** TCP (à connaître par cœur) : **SYN → SYN-ACK → ACK**. C'est la poignée de main qui ouvre toute connexion TCP.

---

## 📘 Cours 2.2 — Les adresses IP

Une **IP** = l'adresse postale de ta machine. Format IPv4 : 4 nombres de 0 à 255 (`192.168.1.10`).

**Les classes (culture générale)**

| Classe | Plage | Usage |
|---|---|---|
| A | 1.0.0.0 – 126.255.255.255 | Très grands réseaux |
| B | 128.0.0.0 – 191.255.255.255 | Réseaux moyens |
| C | 192.0.0.0 – 223.255.255.255 | Petits réseaux (ta box) |

**IP privées** (réseau local) : `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
**IP spéciales** : `127.0.0.1` = toi-même (loopback) ; `255.255.255.255` = broadcast.

**Le masque de sous-réseau** 🎭

Exemple : IP `192.168.1.10`, masque `255.255.255.0` = **/24**.
- Adresse réseau : `192.168.1.0`
- Plage d'hôtes : `192.168.1.1` → `192.168.1.254`
- Broadcast : `192.168.1.255`

**Calcul express** :
- Bits hôtes = `32 − bits du masque`.
- Hôtes utilisables = `2^(bits hôtes) − 2` (on retire l'adresse réseau et le broadcast).

| CIDR | Masque | Hôtes utilisables |
|---|---|---|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /30 | 255.255.255.252 | 2 |

---

## 📘 Cours 2.3 — Protocoles & ports essentiels

| Protocole | Port | Rôle | Sécurisé ? |
|---|---|---|---|
| HTTP | 80 | Web | ❌ en clair |
| HTTPS | 443 | Web chiffré | ✅ |
| FTP | 21 | Transfert de fichiers | ❌ obsolète |
| SSH | 22 | Connexion distante | ✅ |
| Telnet | 23 | Connexion distante | ❌ à bannir |
| SMTP | 25 | Envoi de mail | ⚠️ |
| DNS | 53 | Nom → IP | ⚠️ |
| DHCP | 67/68 | Attribution d'IP automatique | — |
| RDP | 3389 | Bureau à distance Windows | ⚠️ |

> 🧠 Apprends ce tableau par cœur. En pentest, « port 22 ouvert » doit te faire penser « SSH » sans réfléchir.

---

## 🎯 Exercices Semaine 2

### Exercice 2.1 — Cartographie ton propre réseau
1. `ip a` → note ton IP et ton masque (`/xx`).
2. `ip route` → identifie ta **passerelle** (souvent `.1`).
3. Calcule **à la main** : adresse réseau, plage d'hôtes, broadcast. Vérifie avec `ipcalc TON_IP/MASQUE` (`sudo apt install ipcalc`).
4. **Défi bonus** : combien de machines ton sous-réseau peut-il contenir ?

### Exercice 2.2 — Les outils réseau de base
1. `ping -c4 8.8.8.8` puis `ping -c4 google.com`. Que t'apprend la différence sur le DNS ?
2. `traceroute google.com` : combien de routeurs entre toi et Google ?
3. `dig google.com` puis `dig MX gmail.com`.
4. `ss -tuln` : liste les ports en écoute sur ta machine.

### Exercice 2.3 — Le défi du sous-réseau (papier)
Calcule pour chacun : adresse réseau, premier hôte, dernier hôte, broadcast. Vérifie avec `ipcalc`.
- `10.0.0.45 /24`
- `192.168.10.130 /25`
- `172.16.5.200 /26`

---

## 🎫 Épreuve de passage — Semaine 2

Badge **🏆 Cartographe du Réseau** = 3 niveaux réussis.

### 1. 🧠 Quiz auto-corrigé (5/5)
`./verifie.sh "ta réponse"` (minuscules, sans accents).

| # | Question | SHA-256 de la bonne réponse |
|---|---|---|
| 1 | Combien de couches compte le modèle OSI ? | `7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451` |
| 2 | Quel protocole de transport est **fiable** (accusés de réception) ? | `00645195b93272275b50a6c935a23fb62e3e793e8476e83414fed0fcdfee8b41` |
| 3 | Sur quel port standard tourne SSH ? | `785f3ec7eb32f30b90cd0fcf3657d388b5ff4297f2f9716ff66e9b69c05ddd09` |
| 4 | Sur quel port standard tourne HTTPS ? | `6d05621ab7cb7b4fb796ca2ffbe1a141e0d4319d3deb6a05322b9de85d69b923` |
| 5 | Combien d'hôtes **utilisables** dans un réseau /26 ? | `81b8a03f97e8787c53fe1a86bda042b6f0de9b0ec9c09357e107c99ba4d6948a` |

### 2. 🚩 Défi du Boss
- Tu as cartographié ton réseau (`ip a`, `ip route`, `ss -tuln`) et calculé ton sous-réseau, confirmé par `ipcalc`.
- Tu sais resortir de mémoire OSI (7) et 8 ports/protocoles.

### 3. 🏆 Badge officiel en ligne
Termine **TryHackMe — « What is Networking? »** puis **« Intro to LAN »** : [tryhackme.com/module/network-fundamentals](https://tryhackme.com/module/network-fundamentals)
Entraînement chronométré au sous-réseau : [subnettingpractice.com](https://subnettingpractice.com/)

> 🆓 **Alternative 100 % gratuite** : les épreuves **Réseau** de **Root-Me** (en français, gratuit) → [root-me.org](https://www.root-me.org/), et l'entraînement chronométré au sous-réseau **subnettingpractice.com** (déjà gratuit, sans compte).

➡️ **🏆 Badge « Cartographe du Réseau » débloqué.** Cap sur la [Semaine 3](semaine-3-observation-reseau.md) !

---

## ✅ Checklist fin de Semaine 2
- [ ] Je récite OSI (7) et TCP/IP (4).
- [ ] Je calcule un /24, /25, /26 sans calculatrice.
- [ ] Je connais 10 ports/protocoles.
- [ ] J'ai cartographié mon réseau.
- [ ] Quiz 5/5 + module TryHackMe terminé.
