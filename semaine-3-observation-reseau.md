# 🗓️ Semaine 3 — On observe le réseau (Wireshark & scan)

[⬅️ Semaine 2](semaine-2-reseau-bases.md) · [Sommaire](README.md) · [Semaine 4 ➡️](semaine-4-attaque-web.md)

### 🎯 Objectifs de la semaine
- **Capturer et lire** du trafic avec Wireshark.
- **Scanner** un réseau et des ports avec Nmap.
- Comprendre **DNS** en profondeur.
- Voir « en vrai » pourquoi HTTP en clair, c'est dangereux.

---

## 📘 Cours 3.1 — Wireshark : voir l'invisible

**Wireshark** est un **analyseur de paquets** : il capture tout ce qui passe sur ta carte réseau et te le montre, couche par couche. C'est le microscope du réseau.

Concepts clés :
- **Interface de capture** : choisis `eth0`.
- **Filtres d'affichage** les plus utiles :
  - `http` → uniquement le web
  - `dns` → résolutions de noms
  - `ip.addr == 192.168.1.10` → trafic d'une machine
  - `tcp.port == 443` → trafic HTTPS
  - `tcp.flags.syn == 1 && tcp.flags.ack == 0` → les SYN (débuts de connexion)
- **Follow TCP Stream** : reconstitue une conversation entière (clic droit sur un paquet).

> 🔒 **Le déclic sécu** : en capturant une connexion **HTTP** (port 80), tu verras le **mot de passe en clair**. En **HTTPS** (443), tout est chiffré. C'est LE moment où tu comprends pourquoi le « petit cadenas » compte.

---

## 📘 Cours 3.2 — Nmap : le scanner de référence

**Nmap** découvre les machines vivantes, les **ports ouverts**, les **services** et leurs **versions**. C'est la première étape de tout pentest : la **reconnaissance**.

| Commande | Effet |
|---|---|
| `nmap 192.168.1.0/24` | Quelles machines sont vivantes ? |
| `nmap -sn 192.168.1.0/24` | Ping scan (découverte d'hôtes seulement) |
| `nmap -sV 192.168.1.10` | Détecte les **versions** des services |
| `nmap -p- 192.168.1.10` | Scanne **les 65535 ports** |
| `nmap -A 192.168.1.10` | Agressif : OS, versions, scripts |
| `nmap -sS 192.168.1.10` | SYN scan (discret, half-open) |
| `nmap --script vuln 192.168.1.10` | Cherche des vulnérabilités connues |

**Comment ça marche ?** Nmap envoie des paquets et déduit l'état du port :
- **SYN-ACK** reçu → port **ouvert** (`open`).
- **RST** reçu → port **fermé** (`closed`).
- **Rien** → port **filtré** (`filtered`, un pare-feu bloque).

> ⚖️ **Éthique** : tu ne scannes QUE tes propres VM ou la cible légale d'entraînement `scanme.nmap.org`. Scanner un réseau tiers peut être illégal.

---

## 📘 Cours 3.3 — DNS en profondeur

Le **DNS** traduit `google.com` → `142.250.x.x`. C'est l'annuaire d'Internet.

Types d'enregistrements à connaître :
- **A** : nom → IPv4
- **AAAA** : nom → IPv6
- **MX** : serveurs de mail
- **NS** : serveurs de noms du domaine
- **CNAME** : alias
- **TXT** : infos diverses (SPF, vérifications)

Attaques liées (culture) : **DNS spoofing**, **cache poisoning**, **tunneling DNS** (exfiltration). On en reparlera en défense.

Outils : `dig`, `nslookup`, `host`, `whois`.

---

## 🎯 Exercices Semaine 3

### Exercice 3.1 — Capture un mot de passe (sur TA machine)
1. Lance Wireshark, capture sur `eth0`.
2. Va sur un site de test HTTP volontairement non chiffré : `http://testphp.vulnweb.com` (site légal Acunetix) et soumets un faux login.
3. Filtre `http.request.method == "POST"`, fais **Follow TCP Stream**, retrouve les identifiants en clair.
4. Recommence sur un site **HTTPS** : constate que tu ne vois rien.

### Exercice 3.2 — Scanne une cible légale
1. `nmap -sV scanme.nmap.org`.
2. Identifie les ports ouverts et les versions.
3. `nmap -A scanme.nmap.org` : note l'OS deviné.
4. **Défi bonus** : `nmap localhost`. Quels services tournent sur ton Kali ?

### Exercice 3.3 — Enquête DNS
1. `dig +short A wikipedia.org` et `dig MX wikipedia.org`.
2. `whois wikipedia.org` : qui possède le domaine ?
3. **Défi bonus** : trouve l'enregistrement **TXT** de `google.com` et sa politique **SPF**.

---

## 🎫 Épreuve de passage — Semaine 3

Badge **🏆 Œil de Lynx Réseau** = 3 niveaux réussis.

### 1. 🧠 Quiz auto-corrigé (5/5)
`./verifie.sh "ta réponse"` (minuscules, sans accents).

| # | Question | SHA-256 de la bonne réponse |
|---|---|---|
| 1 | Filtre Wireshark pour n'afficher que les résolutions de noms ? | `dd75a9d6fb309c4399fe425cd5f90ff95eba135d6924fb91766ee5d3726b168a` |
| 2 | Option Nmap pour un *ping scan* (découverte d'hôtes seule) ? | `a3ba30081655ce871a84c9f5cba682e750f404a41b4e91008030dd5e5378105f` |
| 3 | Type d'enregistrement DNS pointant vers les serveurs de mail ? | `d7f890c4f72a3d49b69870b2dc2850c698e7b841eb2dd7cd21e4de551a29f4c4` |
| 4 | Port standard du DNS ? | `2858dcd1057d3eae7f7d5f782167e24b61153c01551450a628cee722509f6529` |
| 5 | Mot anglais (sortie Nmap) pour un port qui ne répond pas car bloqué par un pare-feu ? | `13a30363eb940c6c473c642531153b12d80078449bee3a8648db0575fb7de52d` |

### 2. 🚩 Défi du Boss
- Tu as **capturé et retrouvé un mot de passe HTTP en clair** dans Wireshark (Follow TCP Stream), et vérifié qu'en HTTPS il est invisible.
- Tu as scanné `scanme.nmap.org` avec `-sV` et sais lire `open`/`closed`/`filtered`.

### 3. 🏆 Badge officiel en ligne
Termine **TryHackMe — « Nmap »** ([tryhackme.com/room/furthernmap](https://tryhackme.com/room/furthernmap)) et **« Wireshark: The Basics »** ([tryhackme.com/room/wiresharkthebasics](https://tryhackme.com/room/wiresharkthebasics)).

> 🆓 **Alternative 100 % gratuite** : analyse de **vraies captures réseau** sur **Malware-Traffic-Analysis.net** (gratuit, sans compte) → [malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/), et les épreuves **Réseau** (analyse de PCAP) de **Root-Me** → [root-me.org](https://www.root-me.org/).

➡️ **🏆 Badge « Œil de Lynx Réseau » débloqué.** En route pour la [Semaine 4](semaine-4-attaque-web.md) !

---

## ✅ Checklist fin de Semaine 3
- [ ] J'ai capturé et lu du trafic, retrouvé un mot de passe HTTP.
- [ ] Je lance 5 types de scans Nmap et j'interprète open/closed/filtered.
- [ ] Je manipule `dig` (A/MX/NS/TXT).
- [ ] Quiz 5/5 + 2 rooms TryHackMe terminées.
