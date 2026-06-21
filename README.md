# 🚀 Alex le CyberHero — Le Guide Ultime pour Devenir un Pro de la Cyberdéfense

### Programme d'entraînement intensif — 8 semaines

*Spécialement préparé pour toi, **Alexandre**, avant ton entrée en Master Cybersécurité en septembre. 🎯*

> *Parce qu'on va faire de toi un ninja de la sécurité — mais en s'amusant. 🥷💻*

---

## 🎤 Introduction : On va s'éclater !

Salut **Alexandre** ! 👋

Ici, pas de blabla soporifique ni de cours magistral qui endort. **On va apprendre la cyberdéfense comme un jeu vidéo** : des défis, des badges à débloquer, et surtout, de la pratique direct.

Dans deux mois tu rentres en Master. Ce programme a un seul but : que tu arrives le **jour 1** déjà à l'aise avec Linux, le réseau, l'offensif ET le défensif. Pendant que les autres découvriront `ls`, toi tu monteras déjà des labos.

**Comment ça marche ?**

- **8 semaines**, une thématique par semaine, **un fichier par semaine**.
- Chaque semaine = **Cours** 📘 + **Exercices** 🎯 + **Épreuve de passage** 🎫 + **Badge** 🏆.
- Compte **~8 à 12 h par semaine**. Tu peux étaler ou condenser, mais **ne saute pas la pratique** : 70 % de ce que tu retiendras vient des exercices.

> 📖 **Le manuel d'apprentissage (PDF, 35 pages)** : pour comprendre la théorie en mots simples, avec des analogies, télécharge **[Manuel-Alex-le-CyberHero.pdf](Manuel-Alex-le-CyberHero.pdf)**. C'est ton **livre de cours** ; les fichiers de semaine ci-dessous sont ton **cahier d'exercices**. On lit un chapitre du manuel, puis on pratique dans le cahier.

---

## 🗓️ Le programme

| Semaine | Thème | Fichier |
|---|---|---|
| 1 | On installe notre terrain de jeu (VM, Linux, terminal) | [semaine-1-terrain-de-jeu.md](semaine-1-terrain-de-jeu.md) |
| 2 | Les bases du réseau (OSI, IP, sous-réseaux) | [semaine-2-reseau-bases.md](semaine-2-reseau-bases.md) |
| 3 | On observe le réseau (Wireshark & scan) | [semaine-3-observation-reseau.md](semaine-3-observation-reseau.md) |
| 4 | On passe à l'attaque web (éthique !) | [semaine-4-attaque-web.md](semaine-4-attaque-web.md) |
| 5 | Exploitation système avec Metasploit | [semaine-5-exploitation.md](semaine-5-exploitation.md) |
| 6 | On se défend comme un boss (hardening) | [semaine-6-defense.md](semaine-6-defense.md) |
| 7 | Détection : logs, IDS & SIEM | [semaine-7-detection.md](semaine-7-detection.md) |
| 8 | Le grand final : Mission Incident | [semaine-8-mission-incident.md](semaine-8-mission-incident.md) |
| 📎 | Annexes (glossaire, outils, ressources, certifs) | [annexes.md](annexes.md) |
| 📊 | **Suivi de ma progression** (checklist + tableau de bord) | [PROGRESSION.md](PROGRESSION.md) |

---

## 📊 Suivre ta progression

Deux options, au choix :
- **Checklist GitHub** : ouvre [PROGRESSION.md](PROGRESSION.md) et coche les cases au fur et à mesure.
- **Tableau de bord terminal** : lance `./progression.sh` pour un dashboard avec barre de progression et badges qui se débloquent.

```bash
chmod +x progression.sh        # une seule fois
./progression.sh               # voir le tableau de bord
./progression.sh done 1 all    # valider toute la semaine 1
```

---

## 🎫 Comment valider une semaine et débloquer un badge ?

Chaque semaine se termine par une **Épreuve de passage** à 3 niveaux. Tu débloques le badge quand les **3** sont réussis :

1. **🧠 Quiz auto-corrigé (5/5)** — tu réponds, tu vérifies toi-même avec le script `verifie.sh` (voir ci-dessous). Aucun corrigé n'est écrit en clair : seules les **empreintes SHA-256** des bonnes réponses sont dans les fichiers, donc tu ne peux pas tricher sans chercher.
2. **🚩 Défi du Boss** — une manip pratique concrète dans tes machines virtuelles.
3. **🏆 Badge officiel en ligne** — une *room* **TryHackMe** précise dont la complétion délivre un vrai badge / des points sur ton profil public. C'est ta preuve objective et partageable.

### Utiliser le vérificateur de quiz

```bash
chmod +x verifie.sh          # une seule fois
./verifie.sh "ta réponse"    # affiche l'empreinte SHA-256 de ta réponse
```

Compare l'empreinte affichée à celle du tableau de la semaine. **Identiques = bonne réponse ✅.**

> **Règle de format des réponses** : tout en **minuscules**, **sans accents** (ex. `filtre`, pas `filtré`), exactement le format demandé (espaces compris).

Exemple :
```bash
$ ./verifie.sh "pwd"
a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8
```
Si le tableau affiche la même chaîne pour cette question → c'est gagné.

---

## ⚖️ La règle d'or : l'éthique avant tout

> Tu n'attaques **JAMAIS** une machine, un site ou un réseau qui ne t'appartient pas et pour lequel tu n'as pas d'autorisation **écrite**. Tout ce qu'on fait ici se passe **dans tes machines virtuelles** ou sur des **plateformes prévues pour l'entraînement**. En France, l'accès ou le maintien frauduleux dans un système (art. 323-1 et suivants du Code pénal) est un délit — **même sans rien casser**. Le hacker éthique, c'est celui qui sait s'arrêter à la ligne jaune. **Reste du bon côté.**

---

## 🏆 Ton tableau de chasse aux badges

Coche au fur et à mesure :

- [ ] 🏆 Semaine 1 — **Maître du Terminal**
- [ ] 🏆 Semaine 2 — **Cartographe du Réseau**
- [ ] 🏆 Semaine 3 — **Œil de Lynx Réseau**
- [ ] 🏆 Semaine 4 — **Briseur de Requêtes**
- [ ] 🏆 Semaine 5 — **Maître de l'Exploit**
- [ ] 🏆 Semaine 6 — **Gardien du Système**
- [ ] 🏆 Semaine 7 — **Sentinelle du SOC**
- [ ] 🏆 Semaine 8 — **Alex le CyberHero — Niveau Maître** 🎖️

---

*Maintenant, démarre cette VM. Le jeu commence. — Alex le CyberHero*
