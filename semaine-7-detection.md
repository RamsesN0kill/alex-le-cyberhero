# 🗓️ Semaine 7 — Détection : logs, IDS & SIEM

[⬅️ Semaine 6](semaine-6-defense.md) · [Sommaire](README.md) · [Semaine 8 ➡️](semaine-8-mission-incident.md)

### 🎯 Objectifs de la semaine
- Lire et exploiter les **logs** Linux.
- Mettre en place un **IDS** (détection d'intrusion).
- Découvrir un **SIEM** et la **corrélation d'événements**.
- Détecter une attaque que tu lances toi-même.

---

## 📘 Cours 7.1 — Les logs, la mémoire du système

Sous Linux, presque tout laisse une trace. Fichiers clés :

| Fichier | Contenu |
|---|---|
| `/var/log/auth.log` | Authentifications, sudo, SSH |
| `/var/log/syslog` | Messages système généraux |
| `journalctl` | Journal systemd (`journalctl -u ssh`) |
| `/var/log/apache2/access.log` | Requêtes web (repérer SQLi/XSS) |

Compétences clés : filtrer avec `grep`, `awk`, `tail -f` (suivre en temps réel).
Exemple — repérer les échecs SSH et classer les IP attaquantes :
```bash
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr
```

---

## 📘 Cours 7.2 — IDS / IPS

- **IDS** (Intrusion Detection System) : **détecte** et alerte.
- **IPS** (Intrusion Prevention System) : détecte **et bloque**.
- **NIDS** (réseau, ex. **Snort**, **Suricata**) : analyse le trafic.
- **HIDS** (hôte, ex. **OSSEC**, **Wazuh**) : surveille fichiers, logs, intégrité d'une machine.

Deux approches de détection :
- **Par signatures** : on reconnaît des motifs connus (efficace, mais aveugle au 0-day).
- **Par anomalies** : on apprend le « normal » et on alerte sur l'écart (détecte l'inconnu, plus de faux positifs).

---

## 📘 Cours 7.3 — Le SIEM

Un **SIEM** (Security Information and Event Management) **centralise** les logs de tout le SI, les **corrèle** et **alerte**. C'est la tour de contrôle du **SOC** (Security Operations Center).

Exemples : **Wazuh** (open source, parfait pour apprendre), **Splunk**, **Elastic Security (ELK)**, **Graylog**.

La **corrélation**, c'est la magie : un échec SSH = anodin ; 200 échecs en 1 min depuis une IP + une connexion réussie ensuite = **alerte rouge** (brute-force réussi). Le SIEM relie les points qu'un humain ne verrait pas.

> 🎓 **Pour ton Master** : lire des logs et comprendre un SIEM, c'est exactement le métier d'**analyste SOC**, l'un des premiers postes accessibles en sortie d'école. Tu pars avec une longueur d'avance.

---

## 🎯 Exercices Semaine 7

### Exercice 7.1 — Détective des logs
1. Depuis Kali, relance un brute-force SSH (`hydra`) contre ton Ubuntu.
2. Sur Ubuntu, identifie l'attaque dans `/var/log/auth.log`.
3. Écris une commande `grep|awk` qui sort le **top 5 des IP attaquantes** et le nombre de tentatives.
4. **Défi bonus** : transforme-la en script `detect_bruteforce.sh` qui alerte si une IP dépasse 10 échecs.

### Exercice 7.2 — Suricata en sentinelle
1. Installe **Suricata** sur Ubuntu (ou Snort).
2. Lance un `nmap -A` agressif depuis Kali.
3. Vérifie que l'IDS a généré des alertes (`/var/log/suricata/fast.log`).

### Exercice 7.3 — Ton premier SIEM (Wazuh)
1. Installe **Wazuh** (la single-node via Docker est la plus simple) : [documentation.wazuh.com](https://documentation.wazuh.com/).
2. Enrôle ton Ubuntu comme **agent**.
3. Rejoue une attaque (brute-force, scan) et observe les **alertes** dans le dashboard.
4. **Défi bonus** : crée une règle qui alerte sur l'usage de `sudo` par un compte inattendu.

---

## 🎫 Épreuve de passage — Semaine 7

Badge **🏆 Sentinelle du SOC** = 3 niveaux réussis.

### 1. 🧠 Quiz auto-corrigé (5/5)
`./verifie.sh "ta réponse"` (minuscules, sans accents).

| # | Question | SHA-256 de la bonne réponse |
|---|---|---|
| 1 | Chemin complet du fichier de log des authentifications sous Debian/Ubuntu ? | `0d1af57f863ec17d744cbcc9efb1a12eb58daceea0bcd978c0cb0f8b01755122` |
| 2 | Acronyme du système qui détecte **ET bloque** les intrusions ? | `081fe58fff095ab919510370c6eb18096d918869d263d8fcabff80d6cfce85db` |
| 3 | Nom du SIEM open source utilisé dans le programme ? | `88195721bd4c437cf5e1b197f1513b5610cc96b2d919b348e38192da5ea45487` |
| 4 | Cite un IDS réseau (NIDS) vu cette semaine (autre que Snort) ? | `c2f3826a1cb8c3c29eba0d1fd23d55898da013f1057fc9e4116e83fbc790ef89` |
| 5 | Acronyme des « indices de compromission » ? | `7354a0024740d89096dc6137ff3bb47df328ab8ea22f20e88c059d387e58aeae` |

### 2. 🚩 Défi du Boss
- Tu as **détecté un brute-force dans les logs** et sorti le **top 5 des IP attaquantes** via `grep|awk`.
- Un **SIEM Wazuh** centralise tes logs et **remonte une alerte** sur une attaque que tu rejoues.

### 3. 🏆 Badge officiel en ligne
Attaque le parcours **TryHackMe — « SOC Level 1 »** (logs, SIEM, Splunk, Wazuh) : [tryhackme.com/path/outline/soclevel1](https://tryhackme.com/path/outline/soclevel1)
Pour t'entraîner en investigation : **CyberDefenders** ([cyberdefenders.org](https://cyberdefenders.org/)) et **Blue Team Labs Online** ([blueteamlabs.online](https://blueteamlabs.online/)).

> 🆓 **Alternative 100 % gratuite** : **LetsDefend** (plateforme d'analyste SOC, tier *Basic* gratuit avec de vraies alertes à traiter et des cours « SOC Fundamentals », « Splunk », « Phishing Email Analysis ») → [letsdefend.io](https://letsdefend.io/), et les challenges blue team gratuits de **CyberDefenders** → [cyberdefenders.org](https://cyberdefenders.org/).

➡️ **🏆 Badge « Sentinelle du SOC » débloqué.** Prêt pour le grand final ? [Semaine 8](semaine-8-mission-incident.md) !

---

## ✅ Checklist fin de Semaine 7
- [ ] Je lis `auth.log`/`journalctl` et j'extrais les IP attaquantes.
- [ ] Un IDS détecte mes scans.
- [ ] Un SIEM (Wazuh) alerte sur une attaque.
- [ ] Je distingue signatures/anomalies, IDS/IPS, et le rôle d'un SOC.
- [ ] Quiz 5/5 + parcours TryHackMe entamé.
