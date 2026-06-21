# Chapitre 4 — Attaquer un site web (en laboratoire)

Les sites web sont partout, et ce sont les cibles les plus fréquentes. Dans ce chapitre, tu vas comprendre comment fonctionnent les failles web les plus courantes : pourquoi elles existent, comment elles marchent, et comment on les corrige. Tout se fait sur des sites **volontairement troués**, installés chez toi pour l'entraînement.

> À retenir : tout ce chapitre se pratique sur des applications faites exprès pour ça (DVWA, OWASP Juice Shop), installées dans ta machine virtuelle. On n'attaque jamais un vrai site. Jamais.

## 4.1 Comment marche un site web, en deux minutes

Pour attaquer (ou défendre) un site, il faut comprendre le va-et-vient de base.

- Ton **navigateur** (Chrome, Firefox) est le **client**. Il demande des pages.
- Le **serveur** est l'ordinateur, quelque part, qui héberge le site et répond.
- Souvent, derrière le serveur, il y a une **base de données** : un grand classeur où sont rangés les comptes, les mots de passe, les commandes, les messages.

Quand tu te connectes à un site, voici ce qui se passe en gros : ton navigateur envoie ton identifiant et ton mot de passe au serveur ; le serveur va vérifier dans la base de données si ça correspond ; si oui, il te laisse entrer. Les failles web viennent presque toujours d'un serveur qui fait **trop confiance** à ce que le navigateur lui envoie.

## 4.2 L'OWASP Top 10 : la liste des dangers

Une organisation appelée **OWASP** (un groupe mondial d'experts de la sécurité web) publie régulièrement la liste des **10 risques les plus graves** pour les sites web. C'est la référence que tout professionnel connaît. On l'appelle l'**OWASP Top 10**.

Tu n'as pas besoin de tout mémoriser aujourd'hui, mais retiens que les deux failles les plus emblématiques, celles qu'on étudie ici, en font partie : l'**injection** (notamment l'injection SQL) et le **XSS**. Voyons-les en détail.

## 4.3 L'injection SQL : faire dire à la base ce qu'on veut

### D'abord, c'est quoi SQL ?

La base de données comprend un langage appelé **SQL**. C'est avec ce langage qu'on lui pose des questions. Par exemple, quand tu te connectes, le serveur pose à la base une question qui ressemble à : « donne-moi l'utilisateur dont le nom est *Alexandre* et le mot de passe est *xyz* ». En SQL, ça s'écrit à peu près :

```
SELECT * FROM users WHERE name = 'Alexandre' AND password = 'xyz';
```

### Le problème : mélanger les instructions et les données

Voici la faille. Souvent, le serveur **fabrique** cette question en collant directement ce que tu as tapé dans le champ. Si tu tapes ton nom, il colle ton nom. Mais que se passe-t-il si, au lieu d'un nom, tu tapes un bout de langage SQL ?

C'est ça, l'**injection SQL** : tu glisses du code SQL dans un champ de formulaire pour modifier la question que le serveur pose à la base.

### L'exemple classique

Imagine que dans le champ « nom », au lieu d'écrire ton nom, tu écris :

```
' OR '1'='1
```

Le serveur, qui colle bêtement, fabrique alors cette question :

```
SELECT * FROM users WHERE name = '' OR '1'='1' AND password = '...';
```

Regarde le morceau `OR '1'='1'`. Il veut dire « OU BIEN si 1 égale 1 ». Or, 1 égale toujours 1 ! La condition est donc **toujours vraie**, et la base répond « oui, c'est bon, entre ». Tu viens de te connecter **sans connaître le mot de passe**. C'est exactement comme un videur à qui tu dirais « laisse-moi entrer SI je suis invité OU BIEN si le ciel est bleu » — et le ciel est toujours un peu bleu.

### Ce qu'on peut en faire, et comment on s'en protège

Avec des injections plus avancées, on peut faire bien pire : lire toute la base, extraire les mots de passe de tous les utilisateurs, etc. Un outil appelé `sqlmap` automatise ce travail pour tester si un site est vulnérable.

La **défense** est simple à dire : il ne faut **jamais coller** ce que l'utilisateur tape directement dans une question SQL. On utilise des **requêtes préparées**, une technique où les données restent toujours séparées des instructions. La base sait alors que `' OR '1'='1` est juste un texte bizarre tapé comme nom, pas une instruction.

> À retenir : l'injection SQL exploite un serveur qui mélange les données de l'utilisateur avec ses instructions à la base. La parade, c'est de toujours séparer les deux (requêtes préparées).

## 4.4 Le XSS : injecter du code dans la page

### L'idée

**XSS** veut dire *Cross-Site Scripting*. Le principe : au lieu de viser la base de données, tu injectes du **code JavaScript** (le langage qui anime les pages web) dans une page. Ce code s'exécutera ensuite dans le navigateur des **autres visiteurs**.

### Comment ça arrive

Imagine un site avec une zone de commentaires. Tu écris un commentaire, il s'affiche pour tout le monde. Maintenant, que se passe-t-il si, au lieu d'un texte normal, tu écris un morceau de JavaScript dans le commentaire ? Si le site est mal protégé, il va **afficher** ton commentaire en l'exécutant comme du code. Chaque visiteur qui ouvre la page exécute ton script sans le savoir.

Un test inoffensif classique consiste à faire apparaître une petite fenêtre d'alerte :

```
<script>alert('XSS par Alexandre')</script>
```

Si une boîte de dialogue s'affiche, la faille est confirmée.

### Les trois familles de XSS

- **Reflected** (réfléchi) : le code est renvoyé tout de suite, généralement via un lien piégé qu'on t'envoie.
- **Stored** (stocké) : le code est **enregistré** sur le site (dans un commentaire, un profil) et frappe **tous** les visiteurs. C'est le plus dangereux.
- **DOM-based** : la faille est dans le JavaScript déjà présent sur la page.

### Pourquoi c'est grave

Avec un XSS, un attaquant peut voler les **cookies de session** des visiteurs. Un cookie de session, c'est le petit jeton que le site te donne après ta connexion pour se souvenir que c'est toi. Si l'attaquant le vole, il peut se faire passer pour toi sans connaître ton mot de passe. Il peut aussi rediriger les visiteurs, enregistrer ce qu'ils tapent, ou défigurer la page.

La **défense** consiste à toujours « échapper » ce que les utilisateurs écrivent, c'est-à-dire l'afficher comme du texte inoffensif et jamais comme du code.

> À retenir : le XSS injecte du JavaScript qui s'exécute chez les visiteurs. Le XSS stocké est le pire car il touche tout le monde. La parade : ne jamais afficher l'entrée d'un utilisateur comme du code.

## 4.5 Burp Suite : voir et modifier les requêtes

Quand tu navigues, ton navigateur envoie des **requêtes** au serveur. Normalement, tu ne les vois pas. **Burp Suite** est un outil qui se place **entre** ton navigateur et le site (on appelle ça un *proxy*, un intermédiaire) et te montre chaque requête. Mieux : tu peux les **modifier** avant qu'elles partent.

L'analogie : Burp, c'est comme intercepter une lettre à la poste, l'ouvrir, changer un mot, la refermer et la laisser repartir. Pour tester un site, c'est extrêmement puissant : tu peux changer un prix, un identifiant, un paramètre, et voir comment le serveur réagit.

Le module le plus utile pour débuter s'appelle **Repeater** (le répéteur) : il te permet de renvoyer une même requête autant de fois que tu veux, en la modifiant à chaque essai, pour observer les réponses.

## Ce qu'il faut retenir de ce chapitre

- Les failles web viennent d'un serveur qui fait **trop confiance** à ce que le navigateur envoie.
- L'**OWASP Top 10** liste les 10 risques web majeurs ; l'injection et le XSS en font partie.
- L'**injection SQL** glisse du code SQL dans un formulaire pour tromper la base de données.
- Le **XSS** injecte du JavaScript qui s'exécute chez les visiteurs ; le stocké est le plus grave.
- **Burp Suite** intercepte et modifie les requêtes : un outil d'analyse indispensable.
- Les défenses existent et sont simples à nommer : séparer données et instructions, et échapper les sorties.

Tu sais maintenant attaquer un site. Au prochain chapitre, on monte d'un cran : on prend le contrôle d'une machine entière.
