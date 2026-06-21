# 📊 Ma progression — Alexandre

> Deux façons de suivre ton avancement :
> - **Sur GitHub** : coche les cases ci-dessous (modifie ce fichier, les `[ ]` deviennent `[x]`).
> - **Dans le terminal** : lance `./progression.sh` pour un tableau de bord animé avec barre de progression et badges. *(Voir le mode d'emploi en bas.)*

Un badge se débloque quand ses **3 étapes** sont cochées : 🧠 Quiz (5/5) · 🚩 Défi du Boss · 🏆 Room TryHackMe (ou alternative gratuite).

---

## 🗓️ Semaine 1 — [Terrain de jeu](semaine-1-terrain-de-jeu.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss
- [ ] 🏆 Room en ligne
- [ ] **🏅 Badge « Maître du Terminal »**

## 🗓️ Semaine 2 — [Bases du réseau](semaine-2-reseau-bases.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss
- [ ] 🏆 Room en ligne
- [ ] **🏅 Badge « Cartographe du Réseau »**

## 🗓️ Semaine 3 — [Observation réseau](semaine-3-observation-reseau.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss
- [ ] 🏆 Room en ligne
- [ ] **🏅 Badge « Œil de Lynx Réseau »**

## 🗓️ Semaine 4 — [Attaque web](semaine-4-attaque-web.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss
- [ ] 🏆 Room en ligne
- [ ] **🏅 Badge « Briseur de Requêtes »**

## 🗓️ Semaine 5 — [Exploitation](semaine-5-exploitation.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss
- [ ] 🏆 Room en ligne
- [ ] **🏅 Badge « Maître de l'Exploit »**

## 🗓️ Semaine 6 — [Défense / hardening](semaine-6-defense.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss
- [ ] 🏆 Room en ligne
- [ ] **🏅 Badge « Gardien du Système »**

## 🗓️ Semaine 7 — [Détection](semaine-7-detection.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss
- [ ] 🏆 Room en ligne
- [ ] **🏅 Badge « Sentinelle du SOC »**

## 🗓️ Semaine 8 — [Mission Incident](semaine-8-mission-incident.md)
- [ ] 🧠 Quiz 5/5
- [ ] 🚩 Défi du Boss (intrusion + détection + rapport)
- [ ] 🏆 Room en ligne
- [ ] **🎖️ Badge final « Alex le CyberHero — Niveau Maître »**

---

## 🖥️ Le tableau de bord terminal (`progression.sh`)

```bash
chmod +x progression.sh        # une seule fois

./progression.sh               # affiche le tableau de bord
./progression.sh done 1 quiz   # valide le quiz de la semaine 1
./progression.sh done 1 boss   # valide le défi du Boss
./progression.sh done 1 badge  # valide la room/badge en ligne
./progression.sh done 1 all    # valide les 3 d'un coup
./progression.sh undo 1 quiz   # annule une validation
./progression.sh reset         # remet tout à zéro
```

Quand les 3 étapes d'une semaine sont validées, le badge se débloque automatiquement 🏆 et la barre de progression monte. Ton avancement est sauvegardé en local (fichier `.progression.state`, personnel, non partagé).

*Allez Alexandre, remplis-moi ces cases ! 💪*
