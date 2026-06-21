# 🗓️ Semaine 4 — On passe à l'attaque web (éthique !)

[⬅️ Semaine 3](semaine-3-observation-reseau.md) · [Sommaire](README.md) · [Semaine 5 ➡️](semaine-5-exploitation.md)

### 🎯 Objectifs de la semaine
- Comprendre le **Top 10 OWASP**.
- Exploiter **SQLi** et **XSS** dans un lab volontairement vulnérable.
- Utiliser **Burp Suite** pour intercepter des requêtes.

> ⚖️ **Rappel éthique** : tout se passe dans **DVWA** ou **OWASP Juice Shop**, des applis volontairement vulnérables que tu installes chez toi. On n'attaque rien d'autre. Jamais.

---

## 📘 Cours 4.1 — Le Top 10 OWASP

L'**OWASP Top 10** est la liste de référence des risques web les plus critiques :

1. **Broken Access Control** — accès à des ressources non autorisées.
2. **Cryptographic Failures** — données sensibles mal protégées.
3. **Injection** — SQLi, commandes (notre focus).
4. **Insecure Design** — failles de conception.
5. **Security Misconfiguration** — config par défaut, services exposés.
6. **Vulnerable & Outdated Components** — librairies obsolètes.
7. **Identification & Authentication Failures** — auth faible.
8. **Software & Data Integrity Failures**.
9. **Security Logging & Monitoring Failures** — pas de détection.
10. **Server-Side Request Forgery (SSRF)**.

Réf : [owasp.org/Top10](https://owasp.org/www-project-top-ten/)

---

## 📘 Cours 4.2 — L'injection SQL (SQLi)

**Le principe.** Une appli construit une requête SQL avec ce que tu tapes, sans la nettoyer. Tu injectes du SQL qui change le sens de la requête.

Requête vulnérable typique :
```sql
SELECT * FROM users WHERE name = '$input' AND password = '$pass';
```
Si tu mets dans le champ nom : `' OR '1'='1`, la requête devient :
```sql
SELECT * FROM users WHERE name = '' OR '1'='1' AND password = '...';
```
`'1'='1'` est **toujours vrai** → tu passes l'authentification. 💥

Types de SQLi :
- **In-band** (UNION-based, error-based) : résultat visible directement.
- **Blind** (booléenne, temporelle) : pas de résultat visible, tu déduis via vrai/faux ou des délais (`SLEEP(5)`).

**La défense** (qu'on creusera) : **requêtes préparées** (paramétrées), jamais de concaténation. Outil offensif d'audit : `sqlmap`.

---

## 📘 Cours 4.3 — Le Cross-Site Scripting (XSS)

**Le principe.** Tu injectes du **JavaScript** dans une page ; il s'exécute dans le navigateur des victimes.

Test classique : `<script>alert('XSS par Alexandre')</script>`

Trois familles :
- **Reflected** : le script est renvoyé immédiatement (via un lien piégé).
- **Stored** : le script est stocké en base (commentaire, profil) et frappe tous les visiteurs. **Le plus dangereux.**
- **DOM-based** : la faille est dans le JS côté client.

Impact réel : **vol de cookies de session**, défiguration, keylogging, redirection. Défense : **échappement des sorties**, **Content-Security-Policy**, validation des entrées.

---

## 📘 Cours 4.4 — Burp Suite, le couteau suisse du web

**Burp Suite** (édition Community, gratuite, dans Kali) s'intercale entre ton navigateur et le site (**proxy**). Tu vois, modifies et rejoues chaque requête.

Modules clés :
- **Proxy** : intercepte/modifie les requêtes à la volée.
- **Repeater** : renvoie une requête modifiée autant de fois que tu veux.
- **Intruder** : automatise (fuzzing) — limité en Community.

---

## 🎯 Exercices Semaine 4

### Exercice 4.1 — Monte ton lab web
- Option A : **DVWA** → `sudo apt install docker.io` puis `docker run --rm -it -p 80:80 vulnerables/web-dvwa`.
- Option B : **OWASP Juice Shop** → `docker run --rm -p 3000:3000 bkimminich/juice-shop`.
- Fais un **snapshot** avant de commencer.

### Exercice 4.2 — Ta première injection SQL (DVWA, niveau Low)
1. Va dans **SQL Injection**.
2. Entre `1' OR '1'='1` → observe toutes les données qui sortent.
3. Récupère la version de la base : `1' UNION SELECT null, version() #`.
4. **Défi bonus** : dump les hash de la table `users`, casse-les avec `john` ou [crackstation.net](https://crackstation.net/).
5. Passe DVWA en **Medium** : que faut-il adapter dans ton injection ?

### Exercice 4.3 — XSS stocké
1. Dans DVWA → **XSS (Stored)**, poste `<script>alert(document.cookie)</script>`.
2. Recharge : le script s'exécute à chaque visite. Tu affiches le cookie de session.
3. **Défi bonus** : explique en 3 lignes comment transformer ce `alert` en **vol de session** réel.

### Exercice 4.4 — Intercepte avec Burp
1. Configure ton navigateur pour passer par Burp (`127.0.0.1:8080`).
2. Intercepte un login DVWA, modifie un paramètre, renvoie-le via **Repeater**.

---

## 🎫 Épreuve de passage — Semaine 4

Badge **🏆 Briseur de Requêtes** = 3 niveaux réussis.

### 1. 🧠 Quiz auto-corrigé (5/5)
`./verifie.sh "ta réponse"` (minuscules, sans accents).

| # | Question | SHA-256 de la bonne réponse |
|---|---|---|
| 1 | Acronyme de la fondation derrière le « Top 10 » des risques web ? | `1ec32ca39b427db9f1eb69a2c43f6aadb055d665340177848b00c24554251b09` |
| 2 | Acronyme de l'attaque qui injecte du JavaScript dans une page ? | `58e0413224af6b6d3505dd1819d02491c34588de7a4dc6a9ad48a8f7e08e2f7b` |
| 3 | Outil en ligne de commande pour automatiser l'audit d'injections SQL ? | `44b5a25dfad00357b11b2515f85217ecbcc302794bfa6d4fc888fa0a45cecb07` |
| 4 | Module de Burp Suite pour renvoyer une requête modifiée à volonté ? | `ccb0a11184488754162d88ec8e19789a9c57f6c84d5d347481e5399c089408c4` |
| 5 | Famille de XSS stockée en base, la plus dangereuse (mot anglais) ? | `87b04e58961f9a99d853d4046a0b5b793e7c3e4bbd21f5aca8fb17c20cdb1d8b` |

### 2. 🚩 Défi du Boss
- Sur DVWA : tu as réussi un **bypass d'authentification SQLi** + une requête **UNION** révélant la version de la base.
- Tu as placé un **XSS stocké** qui s'exécute, et intercepté/rejoué une requête avec **Burp Repeater**.

### 3. 🏆 Badge officiel en ligne
Termine **TryHackMe — « OWASP Top 10 »** ([tryhackme.com/room/owasptop10](https://tryhackme.com/room/owasptop10)).
Incontournable : crée un compte gratuit sur **PortSwigger Web Security Academy** et fais les premiers labs **SQL injection** + **XSS** : [portswigger.net/web-security](https://portswigger.net/web-security)

➡️ **🏆 Badge « Briseur de Requêtes » débloqué.** Direction la [Semaine 5](semaine-5-exploitation.md) !

---

## ✅ Checklist fin de Semaine 4
- [ ] Je récite l'OWASP Top 10.
- [ ] SQLi réussie (auth bypass + UNION) sur DVWA.
- [ ] XSS stocké placé, impact compris.
- [ ] Interception/rejeu avec Burp.
- [ ] Quiz 5/5 + room TryHackMe + premiers labs PortSwigger.
