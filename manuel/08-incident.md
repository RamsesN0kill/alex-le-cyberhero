# Chapitre 8 — Gérer une crise : la réponse à incident

Voici le grand final. Tu vas assembler tout ce que tu as appris pour faire face à une vraie situation : une machine a été piratée, et c'est à toi de gérer. Ce chapitre t'explique la méthode des professionnels pour traiter un incident calmement et efficacement.

## 8.1 Garder la tête froide : un incident se gère par étapes

Quand une attaque est découverte, le réflexe du débutant est de paniquer : tout débrancher, tout effacer, dans le désordre. C'est une erreur. Les professionnels suivent une **méthode** en étapes, définie par un organisme de référence américain (le NIST). Retiens ces six phases :

1. **Préparation.** Avant même qu'un incident arrive, on s'équipe : outils prêts, procédures écrites, sauvegardes à jour. On ne s'organise pas pendant l'incendie, mais avant.
2. **Détection et analyse.** On repère l'incident (souvent grâce au SIEM du chapitre 7) et on mesure son ampleur : qu'est-ce qui est touché, et jusqu'où ?
3. **Confinement.** On **isole** la zone touchée pour empêcher la propagation, comme on ferme une porte coupe-feu. Par exemple : couper l'accès de l'attaquant, débrancher la machine du réseau.
4. **Éradication.** On **supprime la cause** : le programme malveillant, le compte créé par l'attaquant, la faille qu'il a utilisée.
5. **Récupération.** On remet les services en marche proprement, à partir d'un état sain, et on surveille de près pour vérifier que l'attaquant ne revient pas.
6. **Leçons apprises.** Après la crise, on fait le bilan : qu'est-ce qui a marché, qu'est-ce qu'on améliore pour la prochaine fois ?

> À retenir : un incident se gère en six phases (préparation, détection, confinement, éradication, récupération, leçons apprises). On ne débranche pas tout en panique : on suit la méthode.

## 8.2 La règle d'or : tout documenter

Pendant un incident, **chaque action doit être notée, avec l'heure**. Pourquoi est-ce si important ?

- Pour **comprendre** ce qui s'est passé et le raconter ensuite.
- Pour ne pas se contredire ni oublier une étape.
- Parce qu'un incident peut avoir des **suites judiciaires** : les traces que tu collectes peuvent devenir des **preuves**. Si tu les manipules n'importe comment, elles perdent leur valeur.

On parle de **chaîne de preuve** : comme dans une enquête de police, chaque indice doit être collecté, noté et conservé proprement, sinon il ne vaut plus rien au tribunal.

## 8.3 Mener l'enquête : les indices de compromission

Pour comprendre une intrusion, on cherche des **indices de compromission** (en anglais *IOC*, *Indicators of Compromise*). Ce sont les traces que l'attaquant a laissées : 

- une **adresse IP** inhabituelle qui s'est connectée,
- un **compte utilisateur** qui est apparu sans qu'on l'ait créé,
- une **tâche programmée** suspecte qui se lance toute seule,
- une **clé** ajoutée pour permettre un retour discret,
- un **fichier** ou un programme étrange.

Sur une machine Linux, quelques commandes simples permettent d'enquêter : voir qui s'est connecté récemment, quels programmes tournent, quels fichiers ont été modifiés dans les dernières 24 heures, et quelles tâches automatiques sont programmées. C'est le travail du détective : relever les empreintes.

### La persistance : la porte de derrière de l'attaquant

Un attaquant malin ne se contente pas d'entrer : il installe de quoi **revenir** même si on change le mot de passe. On appelle ça la **persistance**. Cela peut être un compte caché, une clé d'accès ajoutée, ou un programme qui rouvre une connexion à intervalles réguliers. Lors de l'éradication, c'est précisément ce qu'il faut traquer et supprimer, sinon l'attaquant reviendra par sa porte de derrière.

> À retenir : on cherche les indices de compromission (comptes créés, tâches suspectes, connexions étranges) et on traque la persistance, ces portes de derrière que l'attaquant laisse pour revenir.

## 8.4 Le livrable du pro : le rapport d'incident

À la fin, un professionnel produit un **rapport d'incident**. Ce document raconte l'histoire complète et sert à la fois aux chefs, aux techniciens et, parfois, à la justice. Un bon rapport contient :

- Un **résumé pour les non-techniciens** (3 ou 4 phrases : que s'est-il passé, quel impact, est-ce réglé).
- Une **chronologie** des événements, avec les heures.
- Le **point d'entrée** de l'attaquant et les **indices** trouvés.
- Les **actions menées** pour régler le problème.
- Des **recommandations** pour que ça ne se reproduise pas.

Savoir écrire clairement est une compétence aussi importante que savoir hacker. Un rapport confus rend inutile le meilleur travail technique. Un modèle de rapport t'attend dans les annexes du dépôt.

## 8.5 Ton épreuve finale

Dans le cahier d'exercices de la semaine 8, tu joueras les **deux rôles** sur ta propre machine de test :

- D'abord **l'attaquant** : tu compromets ta machine Ubuntu, tu y installes une persistance, et tu notes tout ce que tu fais (ce sera ton corrigé secret).
- Puis le **défenseur** : tu repars de zéro, tu **détectes** l'intrusion dans les journaux et le SIEM, tu **confines**, tu **éradiques**, tu **récupères**, et tu rédiges ton **rapport**.

C'est l'exercice qui réunit tout : Linux, réseau, attaque, défense, surveillance. Si tu le réussis, tu auras fait, en miniature, le travail réel d'un professionnel de la cybersécurité.

## Ce qu'il faut retenir de ce chapitre

- Un incident se gère en **six phases**, avec méthode et sans panique.
- On **documente tout, avec l'heure** : les traces sont des preuves (chaîne de preuve).
- On cherche les **indices de compromission** et on traque la **persistance**.
- On termine par un **rapport** clair, lisible par tous.
- L'épreuve finale réunit toutes tes compétences : attaque, défense, détection, réaction.

## Le mot de la fin

Alexandre, si tu as lu ce manuel jusqu'ici et pratiqué les exercices, tu n'arrives pas en Master comme un débutant. Tu arrives avec un laboratoire monté, des réflexes des deux côtés de la barrière, et un vocabulaire de professionnel.

Tu n'as pas besoin d'être un génie. Juste d'être **curieux et régulier**. Une heure par jour vaut mieux qu'une nuit blanche une fois par mois. 

Maintenant, démarre cette machine virtuelle. Le jeu commence pour de vrai.
