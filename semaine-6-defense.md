# 🗓️ Semaine 6 — On se défend comme un boss (hardening)

[⬅️ Semaine 5](semaine-5-exploitation.md) · [Sommaire](README.md) · [Semaine 7 ➡️](semaine-7-detection.md)

### 🎯 Objectifs de la semaine
- Passer **côté défense (blue team)**.
- **Durcir** un serveur Linux (Ubuntu).
- Configurer **pare-feu (ufw)**, **SSH sécurisé**, **fail2ban**.
- Comprendre la **gestion des comptes et des accès**.

---

## 📘 Cours 6.1 — Le hardening, c'est quoi ?

**Durcir (hardening)** = réduire la **surface d'attaque** d'un système. Principes :
- **Moindre privilège** : chacun a juste les droits nécessaires.
- **Désactiver l'inutile** : moins de services = moins de portes.
- **Mettre à jour** : la majorité des intrusions exploitent des failles **connues et corrigées**.
- **Défense en profondeur** : plusieurs couches (pare-feu + auth forte + logs + monitoring).

> 🧠 **Renversement de perspective** : en semaine 5 tu attaquais Metasploitable. Cette semaine, tu sécurises un **Ubuntu Server** pour qu'il **résiste** à ces mêmes attaques. Pentester et défenseur sont deux faces de la même pièce.

---

## 📘 Cours 6.2 — Le pare-feu

Le **pare-feu** filtre le trafic selon des règles (autoriser/bloquer par IP, port, protocole, sens).

**ufw** (Uncomplicated Firewall) :
```bash
sudo ufw default deny incoming     # on bloque tout en entrée par défaut
sudo ufw default allow outgoing    # on autorise les sorties
sudo ufw allow 22/tcp              # on garde SSH
sudo ufw enable
sudo ufw status verbose
```

**iptables** (le moteur sous-jacent) : bon à connaître pour comprendre ce que `ufw` fait réellement (chaînes `INPUT`, `OUTPUT`, `FORWARD`).

Principe d'or : **politique par défaut = tout bloquer**, puis on ouvre seulement le nécessaire (liste blanche, pas liste noire).

---

## 📘 Cours 6.3 — Sécuriser SSH

SSH (port 22) est la cible n°1 du brute-force sur Internet. Durcissements (`/etc/ssh/sshd_config`) :
- `PermitRootLogin no` — interdire la connexion root directe.
- `PasswordAuthentication no` — **authentification par clé** uniquement.
- `Port 2222` — changer le port (réduit le bruit ; sécurité « par obscurité » bonus, pas suffisante seule).
- `AllowUsers alexandre` — limiter qui peut se connecter.

**Clé SSH** : `ssh-keygen -t ed25519`, puis `ssh-copy-id user@serveur`. La clé privée reste **chez toi** (permissions `600`), la publique sur le serveur.
Après modif : `sudo systemctl restart ssh`.

---

## 📘 Cours 6.4 — fail2ban : le videur du club 🚪

**fail2ban** lit les logs et **bannit automatiquement** les IP qui multiplient les échecs de connexion (brute-force).
```bash
sudo apt install fail2ban
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
# Dans jail.local : activer la "jail" [sshd], régler maxretry, bantime
sudo systemctl restart fail2ban
sudo fail2ban-client status sshd   # voir les IP bannies
```

---

## 🎯 Exercices Semaine 6

### Exercice 6.1 — Installe ta cible défensive
1. Installe une VM **Ubuntu Server** (même réseau Host-Only que Kali).
2. Mets-la à jour, crée un utilisateur non-root, installe `openssh-server`.
3. Snapshot `serveur-base`.

### Exercice 6.2 — Verrouille le pare-feu
1. Configure `ufw` : tout bloquer en entrée sauf SSH.
2. Depuis Kali, `nmap` la cible **avant** et **après** : compare la surface d'attaque.

### Exercice 6.3 — Durcis SSH + clé
1. Génère une paire de clés, déploie la clé publique sur Ubuntu.
2. Désactive `PasswordAuthentication` et `PermitRootLogin`.
3. Vérifie : connexion par mot de passe refusée, par clé acceptée.

### Exercice 6.4 — fail2ban en action
1. Installe et active fail2ban (jail `sshd`, `maxretry = 3`).
2. Depuis Kali, tente un brute-force SSH avec `hydra` (`hydra -l alexandre -P liste.txt ssh://IP`).
3. Constate ton IP **bannie** : `sudo fail2ban-client status sshd`.
4. **Défi bonus** : règle un `bantime` de 1 h et un `ignoreip` pour ne pas te bannir toi-même.

---

## 🎫 Épreuve de passage — Semaine 6

Badge **🏆 Gardien du Système** = 3 niveaux réussis.

### 1. 🧠 Quiz auto-corrigé (5/5)
`./verifie.sh "ta réponse"` (minuscules, sans accents).

| # | Question | SHA-256 de la bonne réponse |
|---|---|---|
| 1 | Nom du pare-feu simplifié d'Ubuntu (3 lettres) ? | `948b0ea85700f2c1a8c0d3eaad142134d7d311878711d97cf7441623fd71c297` |
| 2 | Outil qui bannit automatiquement les IP après trop d'échecs de connexion ? | `db693ea4e168c178ed7cf38224ae20ea59171238ddda09ce0187ce8dc326efa2` |
| 3 | Directive de `sshd_config` qui interdit la connexion root (un seul mot) ? | `e8da7db0895e420ed35179b666779cd0032c44c71791840f5871253f62faf58e` |
| 4 | Principe : donner à chacun juste les droits nécessaires (3 mots, sans accents) ? | `3751d8b6a0dfe9dfb000b7be21d16795a6d89f149c08dec4a116415163be1ed1` |
| 5 | Outil d'audit de durcissement Linux lancé en ligne de commande ? | `75b1644706ce4f6d34253ccc47cd3ac5860a2a1b7d9fa47e9aa31e0dad286615` |

> 💡 Question 4 : la réponse attendue est `moindre privilege` (sans accent).

### 2. 🚩 Défi du Boss
- Ton Ubuntu est durci : pare-feu actif, **surface d'attaque réduite vérifiée à Nmap** (avant/après).
- SSH par **clé uniquement**, root interdit, et **fail2ban bannit ton brute-force Hydra** pour de vrai.

### 3. 🏆 Badge officiel en ligne
Termine **TryHackMe — « Defensive Security Intro »** ([tryhackme.com/room/defensivesecurityintro](https://tryhackme.com/room/defensivesecurityintro)) et lance un audit local : `sudo apt install lynis && sudo lynis audit system` (note ton *hardening index*).

> 🆓 **Alternative 100 % gratuite (et en français !)** : les **guides de durcissement officiels de l'ANSSI** (notamment *ANSSI-BP-028 : recommandations de configuration d'un système GNU/Linux*) → [cyber.gouv.fr](https://cyber.gouv.fr/) et le hub **CERT-FR Durcissement** → [cert.ssi.gouv.fr/dur](https://www.cert.ssi.gouv.fr/dur/). Applique le niveau « minimal » à ton Ubuntu, puis re-scanne avec **Lynis** et compare ton score.

➡️ **🏆 Badge « Gardien du Système » débloqué.** Place à la détection : [Semaine 7](semaine-7-detection.md) !

---

## ✅ Checklist fin de Semaine 6
- [ ] Ubuntu durci, pare-feu actif, surface réduite (vérifiée à Nmap).
- [ ] SSH par clé uniquement, root interdit.
- [ ] fail2ban bannit un brute-force réel.
- [ ] Audit Lynis lancé et score lu.
- [ ] Quiz 5/5 + room TryHackMe terminée.
