# Chapitre 3 — Observer le réseau

Maintenant que tu sais comment les machines se parlent, on va apprendre à **regarder** ce qui circule et à **explorer** une machine à distance. Ce sont les deux yeux du professionnel de la sécurité : écouter le trafic (avec Wireshark) et cartographier une cible (avec Nmap).

## 3.1 Wireshark : le microscope du réseau

### Voir l'invisible

À chaque instant, des centaines de paquets entrent et sortent de ta machine. Tu ne les vois pas. **Wireshark** est un outil qui les **capture** et te les montre un par un, en détail. C'est un microscope : il rend visible ce qui d'habitude file trop vite pour l'œil.

Concrètement, tu choisis quelle carte réseau écouter (par exemple `eth0`, ta connexion principale), tu lances la capture, et Wireshark affiche en direct chaque paquet : qui l'envoie, à qui, avec quel protocole, et ce qu'il contient.

### Trier dans le déluge : les filtres

Le problème, c'est qu'il y a *trop* de paquets. Pour t'y retrouver, Wireshark a des **filtres** : tu écris une petite condition, et il ne te montre que ce qui t'intéresse. Quelques filtres utiles :

| Filtre | Ce qu'il montre |
| --- | --- |
| `http` | Seulement le trafic web non chiffré |
| `dns` | Seulement les demandes à l'annuaire DNS |
| `ip.addr == 192.168.1.10` | Seulement les paquets d'une machine précise |
| `tcp.port == 443` | Seulement le trafic web sécurisé |

Il y a aussi une fonction très pratique appelée **Follow TCP Stream** (suivre le flux TCP) : tu cliques droit sur un paquet, et Wireshark reconstitue la **conversation complète** entre les deux machines, comme si tu lisais tout le dialogue d'un coup.

### Le moment où tu comprends pourquoi HTTPS existe

Voici l'expérience qui marque tout le monde. Si tu captures une connexion à un site en **HTTP** (le web non sécurisé, port 80) et que tu y tapes un mot de passe, tu retrouves ce mot de passe **écrit en clair** dans les paquets de Wireshark. N'importe qui qui écoute le réseau peut le lire.

Si tu refais la même chose sur un site en **HTTPS** (le web sécurisé, port 443), tu ne vois plus rien : tout est **chiffré**, transformé en charabia illisible. 

C'est ça, le fameux petit cadenas de ton navigateur : la garantie que ce que tu envoies est brouillé et que personne ne peut le lire en route.

> À retenir : en HTTP, tout circule en clair et peut être lu par qui écoute. En HTTPS, tout est chiffré. Wireshark te le montre de tes propres yeux : c'est la meilleure leçon de sécurité qui soit.

## 3.2 Nmap : explorer une machine à distance

### La reconnaissance, première étape de tout

Avant d'attaquer (ou de défendre) une machine, il faut la **connaître** : quelle est son adresse, quels services elle fait tourner, quelles portes sont ouvertes. Cette phase d'exploration s'appelle la **reconnaissance**. C'est comme un cambrioleur honnête qui ferait d'abord le tour de la maison pour noter les portes et fenêtres — sauf qu'ici, c'est avec autorisation, pour réparer les faiblesses.

L'outil roi de la reconnaissance s'appelle **Nmap** (*Network Mapper*, le cartographe de réseau).

### Ce que Nmap sait faire

Nmap envoie de petits paquets à une machine et déduit beaucoup de choses des réponses :

- Quelles **machines** sont allumées sur un réseau.
- Quels **ports** sont ouverts (donc quels services tournent).
- Quelle **version** de logiciel se cache derrière chaque service.
- Parfois même quel **système d'exploitation** tourne.

Quelques exemples de commandes :

| Commande | Ce qu'elle fait |
| --- | --- |
| `nmap 192.168.1.10` | Scan de base des ports d'une machine |
| `nmap -sV 192.168.1.10` | Trouve la version des services |
| `nmap -p- 192.168.1.10` | Teste les 65535 ports |
| `nmap -A 192.168.1.10` | Scan complet : OS, versions, scripts |
| `nmap -sn 192.168.1.0/24` | Liste les machines allumées du réseau |

### Comment Nmap devine l'état d'un port

C'est plus simple qu'il n'y paraît. Nmap frappe à la porte (envoie un paquet) et écoute la réponse :

- Si la machine répond « entre » (un paquet SYN-ACK), le port est **ouvert** (*open*) : un service écoute derrière.
- Si la machine répond « va-t'en » (un paquet RST), le port est **fermé** (*closed*) : personne n'écoute.
- Si la machine ne répond **rien du tout**, le port est **filtré** (*filtered*) : un pare-feu bloque silencieusement. C'est souvent le signe d'une machine bien protégée.

Retiens bien ces trois mots anglais : **open, closed, filtered**. Ce sont les réponses que Nmap t'affichera.

> À retenir : Nmap est ton explorateur. Il révèle les machines vivantes, les ports ouverts et les services. Tu ne scannes JAMAIS une machine sans permission : utilise tes propres VM, ou la cible publique d'entraînement scanme.nmap.org.

## 3.3 Plonger dans le DNS

On a vu que le DNS traduit les noms en adresses. En tant que futur professionnel, tu dois savoir l'**interroger** toi-même, car il regorge d'informations sur une cible.

Le DNS ne stocke pas qu'une simple correspondance nom vers adresse. Il garde plusieurs **types d'enregistrements** :

- **A** : le nom vers une adresse IPv4 (le plus courant).
- **AAAA** : le nom vers une adresse IPv6 (la nouvelle génération d'adresses).
- **MX** : les serveurs qui reçoivent les **mails** de ce domaine.
- **NS** : les serveurs DNS responsables du domaine.
- **TXT** : des informations diverses, souvent liées à la sécurité des mails.

L'outil principal pour interroger le DNS s'appelle `dig`. Par exemple, `dig google.com` te donne l'adresse, et `dig MX gmail.com` te dit quels serveurs reçoivent les mails de Gmail. Un autre outil, `whois`, te dit **qui possède** un nom de domaine et depuis quand.

Pourquoi un attaquant s'intéresse au DNS ? Parce qu'en interrogeant l'annuaire d'une entreprise, il peut découvrir ses serveurs, ses sous-domaines, son fournisseur de mail — bref, dessiner la carte de sa cible sans même la toucher directement. C'est de la reconnaissance « discrète ».

## Ce qu'il faut retenir de ce chapitre

- **Wireshark** capture et affiche les paquets : c'est ton microscope. Les **filtres** t'aident à trier.
- En **HTTP** tout est en clair, en **HTTPS** tout est chiffré : Wireshark te le prouve.
- **Nmap** explore une cible : machines vivantes, ports ouverts, services, versions.
- Un port est **ouvert**, **fermé** ou **filtré** selon la réponse de la machine.
- Le **DNS** s'interroge avec `dig` et `whois` ; il révèle beaucoup sur une cible.
- On n'observe et on ne scanne **que** ce qu'on a le droit de toucher.

Tu as maintenant les yeux. Au prochain chapitre, on apprend à se servir de ce qu'on voit : on attaque un site web (dans un laboratoire, bien sûr).
