# Level 09 - Solution

## Introduction

## Étape 1 : Découverte des fichiers

À la racine du répertoire home, on trouve deux fichiers :
- `level09` : Un binaire exécutable
- `token` : Un fichier contenant un texte chiffré

```bash
level09@SnowCrash:~$ ls -la
-rwsr-sr-x+ 1 flag09 level09 7640 Mar  5  2016 level09
----r--r--  1 flag09 level09   26 Mar  5  2016 token
```

Contenu du fichier token :
```bash
level09@SnowCrash:~$ cat token
f4kmm6p|=?p?n??DB?Du{??
```

## Étape 2 : Analyse du binaire

### Test du comportement

Tester le binaire avec une entrée simple :
```bash
level09@SnowCrash:~$ ./level09 aaa
abc
```

## Étape 3 : Déchiffrement du token

### Algorithme de déchiffrement

Pour déchiffrer, il faut faire l'opération inverse :
```
caractère_original[i] = caractère_chiffré[i] - i
```

### Script Python de déchiffrement

Créer un script `decrypt.py` :

```
import sys

arg = sys.argv[1]
result = ""

for i in range(len(arg)):
    result += chr(ord(arg[i]) - i)

print(result)
```

## Étape 4 : Exécution du script

### Méthode 1 : Avec le contenu du fichier token

```bash
level09@SnowCrash:~$ python3 decrypt.py "$(cat token)"
f3iji1ju5yuevaus41q1afiuq
```

## Résultat

**Flag** : `s5cAJpM8ev6XHw998pRWG728z`