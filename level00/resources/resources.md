# Level 00 - Solution

## Introduction
Après avoir regardé la vidéo sur l'intra (Snowcrash), on nous donne quelques indices sur la commande à exécuter `find`.

## Étape 1 : Recherche du fichier

Naviguer vers la racine du système :
```bash
cd ../../..
```

Rechercher le fichier nommé "john" :
```bash
level00@SnowCrash:/$ find . -name "john" 2>/dev/null
./usr/sbin/john
./rofs/usr/sbin/john
```

## Étape 2 : Lecture du contenu

```bash
level00@SnowCrash:/$ cat ./usr/sbin/john
cdiiddwpgswtgt
```

## Étape 3 : Décryptage

Grâce au site [decode.fr](https://www.dcode.fr) (qui est aussi donné dans la vidéo), on essaye de décrypter ce code.

En utilisant le **chiffrement César**, on trouve le mot de passe : **`nottoohardhere`**

## Étape 4 : Récupération du flag

Se connecter en tant que `flag00` :
```bash
level00@SnowCrash:/$ su flag00
Password: nottoohardhere
Don't forget to launch getflag !
```

Exécuter `getflag` pour obtenir le token :
```bash
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```

## Résultat

**Flag** : `x24ti5gi3x0ol2eh4esiuxias`

