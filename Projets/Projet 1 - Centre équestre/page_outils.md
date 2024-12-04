Outils des bases de données : Prérequis, Installations, Exécutions
==================================================================


:dart: Objectifs du document
-----------

- [x] [Comprendre les prérequis d'utilisations]
- [x] [Etre guidé dans l'installation des outils]
- [x] [Etre capable d'éxécuter les outils mis à disposition]


:notebook: Documentation de référence 
-----------

- [x] [La base de données sqlite](https://www.sqlite.org)
- [x] [Usage de sqlite3 avec Python](https://docs.python.org/3/library/sqlite3.html)
- [x] [Outils en ligne de commande pour la manipulation de la base de données](https://www.sqlite.org/cli.html)
- [x] [Outils graphique pour la manipulation de la base de données (sqlitebrowser) ](https://sqlitebrowser.org)


:computer: Prérequis & Arborescence de départ 
-----------

1. Avoir une clé USB

2. La clé USB est associé au lecteur `D:`

3. Créer sur la clé un répertoire `Applis` dans `D:`
  - Vous aurez donc un répertoire `D:\Applis`
  
4. Créer sur la clé un répertoire `Exercices-bdd` dans `D:`
  - Vous aurez donc un répertoire `D:\Exercices-bdd`
  
5. Créer sur la clé un répertoire `Projets` dans `D:`
  - Vous aurez donc un répertoire `D:\Projets`
  
6. Créer sur la clé un répertoire `ProjetCentreEquestre` dans `D:\Projets`
  - Vous aurez donc un répertoire `D:\Projets\ProjetCentreEquestre`
  
7. Créer sur la clé un répertoire `bdd` dans `D:\Projets\ProjetCentreEquestre`
  - Vous aurez donc un répertoire `D:\Projets\ProjetCentreEquestre\bdd`


:computer: Instructions d'installations 
-----------

### Installation de la base de données

1. Aller sur : [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)

2. Aller dans la sous-section : Precompiled Binaries for Windows

3. Télécharger le fichier `sqlite-tools-win-x64-<version>.zip`

*Note : C'est un ensemble d'outils en ligne de commande pour la gestion des fichiers de base de données SQLite.*

4. Le fichier est téléchargé dans le répertoire `Téléchargements` de votre session utilisateur
  - Le nom du fichier est : `sqlite-tools-win-x64-3470100.zip`

5. Déplacer le fichier sur votre clé USB dans `D:\Applis` - j'ai dit de le **déplacer** et non pas de le décompresser pour l'instant ... :smiling_imp:

6. Aller dans D:\Applis
  - Le fichier `sqlite-tools-win-x64-3470100.zip` est un fichier compressé
  - Faire un clic droit sur le fichier -> 7-Zip -> Extraire vers "sqlite-tools-win-x64-3470100\"
  
7. Renommer le répertoire `sqlite-tools-win-x64-3470100` en `sqlite`

Ce qui permet d'avoir l'arborescence suivante :

```txt
D:\Applis\sqlite
|_sqldiff.exe
|_sqlite3.exe
|_sqlite3_analyzer.exe
|_sqlite3_rsync.exe
```

8. Aller sur [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/)

9. Aller dans la sous-section : Windows PortableApp

10. Cliquer sur `DB Browser for SQLite - PortableApp`

11. Le fichier est téléchargé dans le répertoire `Téléchargements` de votre session utilisateur
  - Le nom du fichier est : `SQLiteDatabaseBrowserPortable_3.12.2_English.paf.exe`

12. Déplacer le fichier sur votre clé USB dans `D:\Applis`

13. Renommer le fichier `SQLiteDatabaseBrowserPortable_3.12.2_English.paf.exe` en `SQLiteDatabaseBrowser`

14. Double cliquer sur `SQLiteDatabaseBrowser.exe`
 - Cliquer sur le bouton Next
 - Contrôler que le répertoire de destination est bien : `D:\Applis\SQLiteDatabaseBrowserPortable`
 - Cliquer sur le bouton Install
 - Le programme s'installe dans `D:\Applis\SQLiteDatabaseBrowserPortable`


:bicyclist: Execution 
-----------

### Création de la base de données
 
Cas d'usage :
- [x] Première utilisation
- [x] Réinitialisation complète de la base de données

1. Lancer l'invite de commande Windows

2. Exécuter la commande `D:`

3. Exécuter la commande `cd D:\Projets\ProjetCentreEquestre\bdd`

4. Exécuter la commande `C:\Applis\Sqlite\sqlite3.exe`

5. Utilisez la commande .open pour créer et ouvrir une nouvelle base de données :

  - `.open centreEquestre.db`

6. Fermer la base de données :

  - `.exit`
  
7. Maintenant nous avons une base de données dans :

  - `D:\Projets\ProjetCentreEquestre\bdd\centreEquestre.db`
  
  
  
  
### Manipulation de la base de données

#### A) En utilisant l'invite de commande

1. Lancer l'invite de commande Windows

2. Exécuter la commande `D:`

3. Exécuter la commande `cd D:\Projets\ProjetCentreEquestre\bdd`

4. Exécuter la commande `C:\Applis\Sqlite\sqlite3.exe`

5. Utilisez la commande `.open centreEquestre.db` pour ouvrir la base de données

6. Lancer les commandes SQL dont vous avez besoin ...

7. Sinon vous pouvez créer un fichier SQL et le faire executer dans la base de données :

  - Exemple --> Executer les commandes SQL du fichier schema.sql se trouvant dans `D:\Exercices-bdd` : `.read D:\Exercices-bdd\schema.sql`



#### B) En utilisant le logiciel sqlitebrowser

1. Aller dans `D:\Applis\SQLiteDatabaseBrowserPortable`
2. Double cliquer sur :  `SQLiteDatabaseBrowserPortable.exe`
3. Fichier -> Ouvrir une Base de Données...
4. Choisir une base de données à ouvrir ( Ex: `D:\Projets\ProjetCentreEquestre\bdd`)
5. Accéder à l'onglet Exécuter le SQL
6. Cliquer sur le bouton Executer
![image](https://github.com/user-attachments/assets/38402b9f-38df-469f-9ae8-192554b7a3c0)




:floppy_disk: Procédure de sauvegarde des données 
-----------
La commande .dump dans SQLite permet de prendre un cliché de votre base de données.

1. Lancer l'invite de commande Windows

2. Exécuter la commande `cd D:\Projets\ProjetCentreEquestre\bdd`

3. Exécuter la commande `D:\Applis\Sqlite\sqlite3.exe`

4. Exécuter les commandes suivantes :

```txt
.open centreEquestre.db
.output backup.sql
.dump
.output stdout
.exit
```
