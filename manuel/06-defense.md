# Chapitre 6 — Se défendre comme un boss

Changement de camp. Jusqu'ici tu jouais l'attaquant, pour comprendre comment pensent les méchants. Maintenant, tu deviens le **défenseur** (la *blue team*). Ton but : prendre une machine et la rendre **difficile à attaquer**. On appelle ça le **durcissement** (en anglais *hardening*).

## 6.1 L'état d'esprit du défenseur

### Réduire la surface d'attaque

Imagine ta machine comme un château. Chaque porte, chaque fenêtre, chaque service qui tourne est une **entrée possible** pour un attaquant. L'ensemble de ces entrées s'appelle la **surface d'attaque**. Tout le travail de défense consiste à **réduire** cette surface : moins il y a de portes ouvertes, moins il y a de risques.

### Les quatre grands principes

- **Le moindre privilège.** Chaque utilisateur, chaque programme ne reçoit que les droits **strictement nécessaires**, rien de plus. Le stagiaire n'a pas les clés du coffre-fort. Si un compte est piraté, les dégâts restent limités.
- **Désactiver l'inutile.** Un service que tu n'utilises pas est une porte ouverte pour rien. On l'éteint.
- **Mettre à jour.** La grande majorité des attaques exploitent des failles **déjà connues et déjà corrigées**. Mettre à jour, c'est fermer ces portes. C'est l'action de sécurité la plus rentable qui existe.
- **La défense en profondeur.** On ne met pas une seule serrure, mais plusieurs barrières successives : pare-feu, mots de passe forts, surveillance. Si une barrière tombe, les autres tiennent encore.

> À retenir : durcir une machine, c'est réduire le nombre de portes ouvertes et empiler les protections. Mettre à jour est l'action la plus rentable de toutes.

## 6.2 Le pare-feu : le videur de la machine

Le **pare-feu** (en anglais *firewall*) est le videur à l'entrée de ta machine. Il regarde chaque paquet qui veut entrer ou sortir et décide, selon des **règles**, s'il le laisse passer ou non.

La bonne stratégie est claire et tient en une phrase : **tout bloquer par défaut, puis n'ouvrir que le strict nécessaire.** C'est la règle de la « liste blanche » : on interdit tout, et on autorise seulement ce qu'on connaît. C'est bien plus sûr que d'essayer d'interdire au cas par cas les choses dangereuses (on en oublierait toujours une).

Sous Ubuntu, l'outil simple pour gérer le pare-feu s'appelle **ufw** (*Uncomplicated Firewall*, le pare-feu sans complications). Quelques commandes typiques :

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable
```

En français : on bloque tout ce qui entre, on autorise tout ce qui sort, on ouvre quand même le port 22 (pour pouvoir se connecter à distance en SSH), puis on active le pare-feu. Après ça, si tu refais un scan Nmap depuis Kali, tu verras la différence : presque tous les ports apparaissent maintenant comme **filtrés**. La surface d'attaque a fondu.

## 6.3 Sécuriser l'accès à distance (SSH)

**SSH** est le service qui permet de se connecter à une machine à distance, en ligne de commande. Il est extrêmement utile... et donc extrêmement visé. Sur Internet, des robots tentent en permanence de deviner les mots de passe SSH de toutes les machines qu'ils trouvent. Il faut donc le blinder.

Voici les réglages essentiels (ils se trouvent dans un fichier de configuration appelé `sshd_config`) :

- **Interdire la connexion directe du super-utilisateur.** Le compte *root* est le plus puissant ; on interdit de s'y connecter directement (`PermitRootLogin no`). Un attaquant doit ainsi deviner deux choses au lieu d'une.
- **Se connecter par clé plutôt que par mot de passe.** Plutôt qu'un mot de passe (qu'on peut deviner), on utilise une **paire de clés** : une clé privée que tu gardes secrète sur ta machine, et une clé publique que tu déposes sur le serveur. Pour entrer, il faut posséder la clé privée. C'est comme une serrure ultra-spéciale dont une seule clé existe au monde, dans ta poche. On désactive alors le mot de passe (`PasswordAuthentication no`).

L'analogie de la clé : un mot de passe, c'est un code que quelqu'un peut deviner ou voir par-dessus ton épaule. Une clé privée, c'est un objet physique unique : sans l'avoir, impossible d'entrer, même en connaissant tout le reste.

> À retenir : SSH doit être blindé. Interdis la connexion root directe, et préfère l'authentification par clé au mot de passe. Une clé bien protégée vaut mille mots de passe.

## 6.4 fail2ban : bannir automatiquement les intrus

Même avec SSH bien réglé, des robots vont essayer encore et encore de se connecter. **fail2ban** est un petit gardien automatique : il **surveille les journaux** de la machine et, dès qu'une même adresse IP échoue trop de fois à se connecter (par exemple 3 fois), il la **bannit** : il la bloque au niveau du pare-feu pendant un certain temps.

C'est exactement le videur qui dit : « tu t'es trompé de mot de passe trois fois, dehors, et tu reviens dans une heure ». L'attaquant automatique, qui voulait essayer des milliers de mots de passe, se fait jeter après trois essais. Son attaque devient inutile.

Tu pourras le tester toi-même : depuis Kali, tu lanceras un outil qui tente plein de mots de passe (`hydra`), et tu verras ton adresse se faire bannir au bout de quelques essais. Sensation très satisfaisante.

## 6.5 Vérifier son travail : l'audit

Comment savoir si ta machine est bien durcie ? On utilise un outil d'**audit** qui passe le système en revue et note ce qui va et ce qui ne va pas. Un outil gratuit et excellent s'appelle **Lynis** : il analyse des centaines de points et te donne un score de durcissement, avec des conseils d'amélioration.

Il existe aussi des **guides officiels** de référence : les **CIS Benchmarks** (internationaux) et, en France, les **guides de durcissement de l'ANSSI** (l'agence nationale de cybersécurité). Ce sont des documents qui listent, point par point, comment configurer un système proprement. En connaître l'existence et savoir les appliquer fait partie du métier.

> À retenir : on ne devine pas si une machine est sûre, on le mesure. Lynis audite ta machine ; les guides ANSSI et CIS te donnent la marche à suivre officielle.

## Ce qu'il faut retenir de ce chapitre

- Défendre, c'est **réduire la surface d'attaque** : moins de portes ouvertes, plus de barrières.
- Les quatre principes : **moindre privilège, désactiver l'inutile, mettre à jour, défense en profondeur**.
- Le **pare-feu** bloque tout par défaut et n'ouvre que le nécessaire ; `ufw` le rend simple.
- **SSH** se blinde : pas de root direct, connexion par **clé**.
- **fail2ban** bannit automatiquement les machines qui s'acharnent.
- On **mesure** sa sécurité avec un audit (**Lynis**) et on suit les guides (**ANSSI**, **CIS**).

Tu sais maintenant fermer les portes. Mais que faire si quelqu'un entre quand même ? Au prochain chapitre : surveiller et détecter.
