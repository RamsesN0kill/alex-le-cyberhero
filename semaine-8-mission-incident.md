# 🗓️ Semaine 8 — Le grand final : Mission Incident

[⬅️ Semaine 7](semaine-7-detection.md) · [Sommaire](README.md) · [Annexes 📎](annexes.md)

### 🎯 Objectifs de la semaine
- Tout assembler : **red team + blue team** dans un scénario complet.
- Appliquer un **processus de réponse à incident**.
- Produire un **rapport** professionnel.
- Valider toutes tes compétences.

---

## 📘 Cours 8.1 — Le cycle de réponse à incident (NIST)

Quand une organisation se fait attaquer, on suit un processus structuré (cadre **NIST SP 800-61**) :

1. **Préparation** — outils, procédures, sauvegardes prêtes AVANT l'incident.
2. **Détection & Analyse** — repérer l'incident, en évaluer la portée.
3. **Confinement** — isoler pour limiter la casse (court puis long terme).
4. **Éradication** — supprimer la cause (malware, compte compromis, faille).
5. **Récupération** — restaurer les services proprement, surveiller la rechute.
6. **Leçons apprises** — post-mortem : qu'est-ce qui a marché, qu'améliorer ?

> 🧠 **Le réflexe pro** : on ne « débranche pas tout en panique ». On **documente** chaque action (horodatée) — vital pour le rapport, l'analyse forensique et d'éventuelles suites légales. La **chaîne de preuve** compte.

---

## 📘 Cours 8.2 — Forensic & IOC

- **IOC (Indicators of Compromise)** : traces d'une intrusion (IP malveillante, hash de malware, fichier suspect, compte créé, port en écoute anormal).
- **Forensic de base** : qui s'est connecté (`last`, `lastb`), quels processus tournent (`ps aux`, `ss -tulpn`), quels fichiers modifiés récemment (`find / -mtime -1`), quelles tâches planifiées suspectes (`crontab -l`, `/etc/cron*`).
- **Persistance** de l'attaquant à chasser : nouveaux utilisateurs, clés SSH ajoutées, services/cron créés, binaires SUID anormaux.

---

## 🚨 Le Grand Défi — Mission Incident

**Scénario.** *« Tu es l'analyste sécu d'une PME. Le serveur Ubuntu (celui des semaines 6-7) a un comportement anormal : connexions étranges, un nouveau compte est apparu. À toi de gérer la crise. »*

### Phase RED (joue l'attaquant) — Jour 1-2
1. Depuis Kali, compromets ton Ubuntu **volontairement re-fragilisé** (reverse shell, ou brute-force SSH sur un compte faible).
2. Établis ta **persistance** : crée un utilisateur caché, ajoute une clé SSH, pose une tâche cron qui rouvre un reverse shell.
3. **Documente** ce que tu as fait (ce sera ton corrigé).

### Phase BLUE (deviens le défenseur) — Jour 3-5
4. **Détection** : repère l'intrusion via les logs et le SIEM Wazuh.
5. **Analyse** : identifie les **IOC** (compte créé, cron suspect, clé SSH ajoutée, connexions).
6. **Confinement** : coupe l'accès (bannir l'IP, désactiver le compte, fermer le port).
7. **Éradication** : supprime persistance, compte, cron, clés ; corrige la faille d'entrée.
8. **Récupération** : restaure un état sain, re-durcis, re-teste avec Nmap.

### 📄 Livrable — Rapport d'incident
Rédige un rapport (1 à 3 pages) avec :
- **Résumé exécutif** (3-4 phrases compréhensibles par un non-technique).
- **Chronologie** horodatée des événements.
- **Vecteur d'entrée** et **IOC** identifiés.
- **Actions de remédiation** menées.
- **Recommandations** pour éviter la récidive.

*(Un modèle de rapport t'attend dans les [annexes](annexes.md).)*

---

## 🎫 Épreuve de passage — Semaine 8 (finale !)

Badge **🏆 Alex le CyberHero — Niveau Maître** 🎖️ = 3 niveaux réussis.

### 1. 🧠 Quiz auto-corrigé (5/5)
`./verifie.sh "ta réponse"` (minuscules, sans accents).

| # | Question | SHA-256 de la bonne réponse |
|---|---|---|
| 1 | Combien d'étapes compte le cycle de réponse à incident NIST (tel que présenté ici) ? | `e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683` |
| 2 | Phase qui consiste à **isoler** pour limiter la casse ? | `eba4bfec00d14352e35223b99219104b22863cdaee10de1a1f81e475e82a4462` |
| 3 | Phase qui **supprime la cause** (malware, compte compromis) (sans accent) ? | `61dd7c220bd859c27809034fb7e9ef0de4fc433a8b6bf52f05b1eaa6a486233b` |
| 4 | Comment appelle-t-on l'équipe **défensive** (un mot, anglais) ? | `16477688c0e00699c6cfa4497a3612d7e83c532062b64b250fed8908128ed548` |
| 5 | Quel est le **préfixe des drapeaux** de ce programme ? | `12101374575d3c80179a52ae0e7fb4b8f126740687dcecd0ae613bc17512d3b9` |

### 2. 🚩 Défi du Boss (le vrai test)
- Tu as mené **l'intrusion complète** (phase RED) puis tu l'as **détectée, confinée et éradiquée** (phase BLUE).
- Tu as produit un **rapport d'incident** structuré (résumé exécutif + chronologie + IOC + remédiation + recommandations).

### 3. 🏆 Badge officiel en ligne
Termine **TryHackMe — « Incident Response Fundamentals »** / parcours **« Cyber Defense »**. Puis, pour réviser TOUT le programme de façon ludique : **picoCTF** ([picoctf.org](https://picoctf.org/)) — vise au moins 5 challenges résolus.

➡️ **🏆 Badge final débloqué. Tu es officiellement Alex le CyberHero — Niveau Maître. 🎖️**

---

## 🏁 Le mot de la fin

Alexandre, si tu boucles ces 8 semaines, tu n'arrives pas en Master comme un débutant : tu arrives avec un **labo monté**, des **réflexes offensifs ET défensifs**, et un **vocabulaire de pro**. Tu auras attaqué, défendu, détecté et géré une crise — le cycle complet du métier.

Tu n'as pas besoin d'être un génie. Juste **curieux et régulier**. Une heure par jour vaut mieux qu'un marathon le dimanche.

**Maintenant, démarre cette VM. Le jeu commence. 🥷💻**

*— Alex le CyberHero*

---

## ✅ Checklist finale
- [ ] J'ai mené une intrusion complète puis l'ai détectée et éradiquée.
- [ ] Je connais le cycle de réponse à incident (NIST, 6 étapes).
- [ ] J'ai produit un rapport d'incident professionnel.
- [ ] Quiz 5/5 + parcours TryHackMe + picoCTF entamé.
- [ ] **J'ai débloqué les 8 badges.** 🏆
