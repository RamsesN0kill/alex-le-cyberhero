# 📎 Annexes — Les trucs en plus pour briller

[⬅️ Semaine 8](semaine-8-mission-incident.md) · [Sommaire](README.md)

---

## 📖 A. Glossaire express

| Terme | Définition courte |
|---|---|
| **0-day** | Faille inconnue de l'éditeur, sans correctif. |
| **Payload** | Code exécuté après l'exploitation d'une faille. |
| **Pivot** | Rebondir d'une machine compromise vers une autre. |
| **Hash** | Empreinte unique d'une donnée (MD5, SHA-256). |
| **Brute-force** | Essayer toutes les combinaisons possibles. |
| **Phishing** | Hameçonnage : tromper pour voler des infos. |
| **CVE** | Identifiant public d'une vulnérabilité connue. |
| **Red team** | L'attaque (offensif). |
| **Blue team** | La défense. |
| **Purple team** | Collaboration red + blue. |
| **SOC** | Centre de supervision sécurité. |
| **IOC** | Indice de compromission. |
| **C2** | Serveur de commande et contrôle d'un attaquant. |
| **SIEM** | Centralisation + corrélation des logs de sécurité. |

---

## 🧰 B. Ta boîte à outils (récap)

- **Offensif** : Nmap, Metasploit, Burp Suite, sqlmap, Hydra, John the Ripper, Wireshark.
- **Défensif** : ufw/iptables, fail2ban, Suricata/Snort, Wazuh, Lynis, ClamAV.
- **Apprentissage** : TryHackMe, Hack The Box, PortSwigger Academy, OverTheWire, picoCTF, VulnHub.

---

## 🌐 C. Plateformes d'entraînement gratuites (à garder à vie)

- **TryHackMe** — parcours guidés, idéal pour débuter : [tryhackme.com](https://tryhackme.com/)
- **Hack The Box** (+ HTB Academy) — plus corsé : [hackthebox.com](https://www.hackthebox.com/)
- **PortSwigger Web Security Academy** — le web, gratuit et excellent : [portswigger.net/web-security](https://portswigger.net/web-security)
- **OverTheWire** — Linux/réseau par le jeu : [overthewire.org](https://overthewire.org/wargames/)
- **picoCTF** — CTF pédagogique : [picoctf.org](https://picoctf.org/)
- **Root-Me** (français !) : [root-me.org](https://www.root-me.org/)
- **CyberDefenders / Blue Team Labs Online** — investigation blue team.

---

## 📚 D. Pour aller plus loin (lectures & chaînes)

- **Livres** : *The Web Application Hacker's Handbook*, *Hacking: The Art of Exploitation*.
- **YouTube** : NetworkChuck, John Hammond, IppSec (write-ups HTB), LiveOverflow, Hak5.
- **Veille FR** : le **CERT-FR** (alertes officielles ANSSI) : [cert.ssi.gouv.fr](https://www.cert.ssi.gouv.fr/).

---

## 🎓 E. Certifications à viser (plus tard)

- **CompTIA Security+** — la base reconnue.
- **eJPT** (INE) — pentest junior, abordable.
- **OSCP** (Offensive Security) — la référence offensive, exigeante.
- **CEH** — connue des RH.
- **Blue Team Level 1 (BTL1)** — côté défense.

---

## ⚖️ F. Le code d'honneur du hacker éthique

1. Je n'attaque **que** ce qui m'appartient ou ce que j'ai l'autorisation **écrite** de tester.
2. Je ne nuis pas, je ne vole pas, je n'expose pas de données.
3. Je signale les failles de manière responsable (**responsible disclosure**).
4. Mon savoir sert à **protéger**, pas à détruire.
5. Dans le doute, je m'abstiens.

> En France, l'accès ou le maintien frauduleux dans un système (art. 323-1 et suivants du Code pénal) est puni de prison et d'amende — **même « sans rien casser »**. Ton terrain de jeu, ce sont tes VM et les plateformes prévues pour ça. **Toujours.**

---

## 📄 G. Modèle de rapport d'incident (Semaine 8)

```
==========================================================
RAPPORT D'INCIDENT DE SÉCURITÉ
==========================================================
Référence incident : INC-2026-001
Analyste            : Alexandre
Date du rapport     : JJ/MM/AAAA
Niveau de gravité   : Faible / Moyen / Élevé / Critique

1. RÉSUMÉ EXÉCUTIF
------------------
(3-4 phrases, lisibles par un non-technique : que s'est-il
passé, quel impact, est-ce résolu ?)

2. CHRONOLOGIE (horodatée)
--------------------------
JJ/MM HH:MM - Première trace suspecte (ex. pic d'échecs SSH)
JJ/MM HH:MM - Connexion réussie de l'attaquant
JJ/MM HH:MM - Création du compte malveillant "xxx"
JJ/MM HH:MM - Détection par l'analyste
JJ/MM HH:MM - Confinement (IP bannie, compte désactivé)
JJ/MM HH:MM - Éradication terminée
JJ/MM HH:MM - Retour à la normale

3. VECTEUR D'ENTRÉE
-------------------
(Comment l'attaquant est entré : service vulnérable,
mot de passe faible, etc.)

4. INDICATEURS DE COMPROMISSION (IOC)
-------------------------------------
- IP attaquante : x.x.x.x
- Compte créé   : xxx
- Tâche cron    : /etc/cron.d/xxx
- Clé SSH ajoutée à : /home/xxx/.ssh/authorized_keys

5. ACTIONS DE REMÉDIATION
-------------------------
(Confinement → éradication → récupération, étape par étape.)

6. RECOMMANDATIONS
------------------
(Comment éviter la récidive : MAJ, mots de passe forts,
fail2ban, MFA, supervision SIEM, etc.)
==========================================================
```

---

## 🏆 H. Récapitulatif des badges

| Semaine | Badge | Thème validé |
|---|---|---|
| 1 | Maître du Terminal | Linux, terminal, permissions |
| 2 | Cartographe du Réseau | OSI/TCP-IP, IP, sous-réseaux |
| 3 | Œil de Lynx Réseau | Wireshark, Nmap, DNS |
| 4 | Briseur de Requêtes | OWASP, SQLi, XSS, Burp |
| 5 | Maître de l'Exploit | Metasploit, reverse shell |
| 6 | Gardien du Système | Hardening, ufw, SSH, fail2ban |
| 7 | Sentinelle du SOC | Logs, IDS, SIEM |
| 8 | **Alex le CyberHero — Niveau Maître** 🎖️ | Réponse à incident complète |

*Bonne chance, Alexandre. On compte sur toi. — Alex le CyberHero*
