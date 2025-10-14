Installer SQLite CLI pour manipuler la base de données en ligne de commande
Installer le CLI de SQLite pour manipuler la base de données en ligne de commande

Objectif de la session
À la fin de cette session, vous serez capable d’installer le SQLite Command-Line Interface (CLI) sur votre système d’exploitation (Linux, macOS ou Windows) afin de manipuler facilement votre base de données SQLite en ligne de commande.

Pourquoi installer le CLI SQLite ?
Même si Python embarque le package sqlite3 pour manipuler les bases SQLite dans les scripts, il est souvent beaucoup plus pratique et rapide d’utiliser le CLI pour :

Créer les tables,

Inspecter les données,

Tester les requêtes SQL,

Explorer la structure de la base de données.

Étapes d'installation selon votre système d’exploitation
Sous Linux (Debian, Ubuntu, etc.)
Ouvrez votre terminal et exécutez :

sudo apt update
sudo apt install sqlite3
Pour vérifier l’installation :

sqlite3 --version
Sous macOS
Vous avez deux options :

Via Homebrew (recommandé)

Si vous avez Homebrew installé, tapez dans votre terminal :

brew update
brew install sqlite
Puis vérifiez :

sqlite3 --version
Sans Homebrew
Rendez-vous sur le site officiel :
https://sqlite.org/download.html
Téléchargez la version précompilée pour macOS et suivez les instructions pour l’installation.

Sous Windows
Rendez-vous sur la page officielle :
https://www.sqlite.org/download.html

Téléchargez ces 2 fichiers :

sqlite-tools-win32-x86-*.zip (les outils en ligne de commande)

(Optionnel mais utile) sqlite-dll-win64-x64-*.zip

Extrayez les fichiers dans un dossier, par exemple C:\sqlite

Ajoutez ce dossier à votre PATH système :

Ouvrir Paramètres Système > Variables d’environnement

Dans la variable Path, ajoutez C:\sqlite

Ouvrez un terminal (cmd ou PowerShell) et tapez :

sqlite3 --version
Si cela vous affiche une version, c’est que l’installation est réussie

Note du formateur
Personnellement, je travaille sous Linux Ubuntu. Mais pas d’inquiétude : toutes les étapes du cours ont été pensées pour être entièrement reproductibles sous Windows et macOS.

Dans la prochaine session :
Nous allons créer ensemble la base de données SQLite en ligne de commande et y intégrer les premières tables de notre écosystème cinéphile !