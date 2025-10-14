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





# MovieLens API

Bienvenue dans l’API **MovieLens** – une API RESTful développée avec **FastAPI** pour explorer la base de données MovieLens. Elle vous permet d'interroger des informations sur les films, les évaluations, les utilisateurs, les tags et les liens vers des bases de données externes (IMDB, TMDB).

## Fonctionnalités principales

- Recherche de films par titre, genre, ou ID
- Consultation des évaluations par utilisateur et par film
- Gestion des tags associés aux films
- Récupération des identifiants IMDB / TMDB
- Statistiques globales de la base

---

## Prérequis

- Python ≥ 3.12
- Un client HTTP comme `httpx` ou `requests`

Installation rapide de `httpx` :

```bash
pip install httpx
```

---

## Démarrer avec l'API

L'API est accessible à l'adresse suivante :

```
http://localhost:8000
```

L'interface Swagger est disponible ici :

```
http://localhost:8000/docs
```

---

## Endpoints essentiels

| Méthode | URL                                 | Description |
|--------|--------------------------------------|-------------|
| GET    | `/`                                  | Vérifie le bon fonctionnement de l’API |
| GET    | `/movies`                            | Liste paginée des films avec filtres |
| GET    | `/movies/{movie_id}`                 | Détail d’un film |
| GET    | `/ratings`                           | Liste paginée des évaluations |
| GET    | `/ratings/{user_id}/{movie_id}`      | Évaluation d’un film par un utilisateur |
| GET    | `/tags`                              | Liste des tags |
| GET    | `/tags/{user_id}/{movie_id}/{tag}`   | Détail d’un tag |
| GET    | `/links`                             | Liste des identifiants IMDB/TMDB |
| GET    | `/links/{movie_id}`                  | Identifiants pour un film donné |
| GET    | `/analytics`                         | Statistiques de la base |

---

## Exemples d’utilisation avec `httpx`

### Lister les films

```python
import httpx

response = httpx.get("http://localhost:8000/movies", params={"limit": 5})
print(response.json())
```

### Obtenir un film spécifique

```python
movie_id = 1
response = httpx.get(f"http://localhost:8000/movies/{movie_id}")
print(response.json())
```

### Rechercher les évaluations pour un film donné

```python
response = httpx.get("http://localhost:8000/ratings", params={"movie_id": 1})
print(response.json())
```

### Récupérer un tag spécifique

```python
response = httpx.get("http://localhost:8000/tags/5/1/superbe")
print(response.json())
```

### Obtenir des statistiques globales

```python
response = httpx.get("http://localhost:8000/analytics")
print(response.json())
```

---

## Conditions d'utilisation

- Cette API est conçue à des fins pédagogiques et expérimentales.
- Merci de ne pas effectuer d'appels massifs sans contrôle de fréquence (rate-limiting non implémenté pour l’instant).
- Vous pouvez l’intégrer à des notebooks, applications ou projets de dataviz pour visualiser les données de MovieLens.

---

## Contribuer

Les contributions sont les bienvenues !

- Corriger des bugs
- Améliorer les performances des requêtes
- Ajouter de nouveaux endpoints
- Rendre l’API disponible sur un hébergeur public

---

## Ressources utiles

- Swagger UI : [http://localhost:8000/docs](http://localhost:8000/docs)
- Documentation technique : disponible via Swagger
- Base de données MovieLens : [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)

---

## Software Development Kit (SDK)

*A venir*

---

## URL publique (Cloud) de l'API


