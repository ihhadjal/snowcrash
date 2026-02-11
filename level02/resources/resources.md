# Level 02 - Solution

## Introduction
On remarque qu'il y a un fichier `level02.pcap` dans le répertoire home. Ce fichier contient une capture réseau qu'il faut analyser avec Wireshark.

## Étape 1 : Transfert du fichier avec SCP

Pour analyser le fichier PCAP, on doit le transférer sur notre machine hôte en utilisant la commande `scp` :

```bash
scp -P 4242 level02@10.14.200.6:~/level02.pcap ~/sgoinfre/snowcrash
```

**Explication des paramètres :**
- `-P 4242` : Spécifie le port SSH
- `level02@10.14.200.6` : Utilisateur et adresse IP de la machine SnowCrash
- `~/level02.pcap` : Chemin du fichier source
- `~/sgoinfre/snowcrash` : Répertoire de destination

## Étape 2 : Analyse avec Wireshark

Une fois le fichier transféré, on l'ouvre avec Wireshark et on analyse le flux réseau.

### 🔍 Recherche du mot de passe

En suivant le flux TCP, on obtient :

```
..%
..%
..&..... ..#..'..$
..&..... ..#..'..$
.. .....#.....'.........
.. .38400,38400....#.SodaCan:0....'..DISPLAY.SodaCan:0......xterm..
........"........!
........"..".....b........b....	B.
..............................1.......!
.."....
.."....
..!..........."
........"
..".............	..
.....................
Linux 2.6.38-8-generic-pae (::ffff:10.1.1.2) (pts/10)

..wwwbugs login: 
l
.l
e
.e
v
.v
e
.e
l
.l
X
.X


..
Password: 
ft_wandr...NDRel.L0L

.
..
Login incorrect
wwwbugs login: 
```

### 💡 Analyse du mot de passe

On voit clairement la tentative de connexion :
```
Password: ft_wandr...NDRel.L0L
```

**Point important :** Wireshark affiche les caractères **backspace** (suppression) comme des **points (`.`)**

En analysant la séquence :
- `ft_wandr...NDRel.L0L`
- Les 3 points représentent 3 backspaces qui effacent `ndr`
- Le mot de passe réel est donc : **`ft_waNDReL0L`**

## Étape 3 : Récupération du flag

Se connecter en tant que `flag02` avec le mot de passe trouvé :
```bash
su flag02
Password: ft_waNDReL0L
Don't forget to launch getflag !
```

Exécuter `getflag` pour obtenir le token :
```bash
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
```

## Résultat

**Flag** : `kooda2puivaav1idi4f57q8iq`