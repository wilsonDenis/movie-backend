"""
Tests pour les fonctions query_helpers.py
Ce fichier teste toutes les fonctions de requête SQLAlchemy
"""
from database import SessionLocal
from query_helpers import *


def print_separator(title: str):
    """Affiche un séparateur visuel avec un titre."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)


# Créer une session de base de données
db = SessionLocal()

# ============================================================
# TEST 1 : Récupérer un film par ID
# ============================================================
print_separator("TEST 1 : get_movie(db, movie_id=1)")
movie = get_movie(db, movie_id=1)
if movie is None:
    print("Film non trouvé.")
else:
    print(f" Film trouvé :")
    print(f"   ID: {movie.movieId}")
    print(f"   Titre: {movie.title}")
    print(f"   Genres: {movie.genres}")


# ============================================================
# TEST 2 : Récupérer plusieurs films (pagination)
# ============================================================
print_separator("TEST 2 : get_movies(db, limit=5)")
movies = get_movies(db, limit=5)
print(f" {len(movies)} films récupérés :")
for idx, movie in enumerate(movies, 1):
    print(f"   {idx}. [{movie.movieId}] {movie.title} - {movie.genres}")


# ============================================================
# TEST 3 : Rechercher des films par titre
# ============================================================
print_separator("TEST 3 : get_movies(db, title='Toy Story', limit=3)")
movies = get_movies(db, title="Toy Story", limit=3)
print(f" {len(movies)} films contenant 'Toy Story' :")
for movie in movies:
    print(f"   [{movie.movieId}] {movie.title}")


# ============================================================
# TEST 4 : Rechercher des films par genre
# ============================================================
print_separator("TEST 4 : get_movies(db, genre='Comedy', limit=5)")
movies = get_movies(db, genre="Comedy", limit=5)
print(f"{len(movies)} films de comédie :")
for movie in movies:
    print(f"   [{movie.movieId}] {movie.title} - {movie.genres}")


# ============================================================
# TEST 5 : Récupérer une évaluation spécifique
# ============================================================
print_separator("TEST 5 : get_rating(db, user_id=1, movie_id=1)")
rating = get_rating(db, user_id=1, movie_id=1)
if rating is None:
    print("Évaluation non trouvée.")
else:
    print(f" Évaluation trouvée :")
    print(f"   Utilisateur: {rating.userId}")
    print(f"   Film: {rating.movieId}")
    print(f"   Note: {rating.rating}/5")
    print(f"   Timestamp: {rating.timestamp}")


# ============================================================
# TEST 6 : Récupérer les évaluations d'un film
# ============================================================
print_separator("TEST 6 : get_ratings(db, movie_id=1, limit=5)")
ratings = get_ratings(db, movie_id=1, limit=5)
print(f"{len(ratings)} évaluations pour le film #1 :")
for rating in ratings:
    print(f"   User {rating.userId} → {rating.rating}/5")


# ============================================================
# TEST 7 : Récupérer les évaluations d'un utilisateur
# ============================================================
print_separator("TEST 7 : get_ratings(db, user_id=1, limit=5)")
ratings = get_ratings(db, user_id=1, limit=5)
print(f"{len(ratings)} évaluations par l'utilisateur #1 :")
for rating in ratings:
    print(f"   Film {rating.movieId} → {rating.rating}/5")


# ============================================================
# TEST 8 : Filtrer les évaluations par note minimale
# ============================================================
print_separator("TEST 8 : get_ratings(db, min_rating=4.5, limit=5)")
ratings = get_ratings(db, min_rating=4.5, limit=5)
print(f" {len(ratings)} évaluations avec note ≥ 4.5 :")
for rating in ratings:
    print(f"   User {rating.userId} → Film {rating.movieId} : {rating.rating}/5")


# ============================================================
# TEST 9 : Récupérer les tags d'un film
# ============================================================
print_separator("TEST 9 : get_tags(db, movie_id=1, limit=5)")
tags = get_tags(db, movie_id=1, limit=5)
if len(tags) == 0:
    print(" Aucun tag trouvé pour ce film.")
else:
    print(f"{len(tags)} tags pour le film #1 :")
    for tag in tags:
        print(f"   User {tag.userId} → '{tag.tag}'")


# ============================================================
# TEST 10 : Récupérer les tags d'un utilisateur
# ============================================================
print_separator("TEST 10 : get_tags(db, user_id=2, limit=5)")
tags = get_tags(db, user_id=2, limit=5)
if len(tags) == 0:
    print("  Aucun tag trouvé pour cet utilisateur.")
else:
    print(f" {len(tags)} tags créés par l'utilisateur #2 :")
    for tag in tags:
        print(f"   Film {tag.movieId} → '{tag.tag}'")


# ============================================================
# TEST 11 : Récupérer un tag spécifique
# ============================================================
print_separator("TEST 11 : get_tag(db, user_id=2, movie_id=60756, tag_text='funny')")
tag = get_tag(db, user_id=2, movie_id=60756, tag_text="funny")
if tag is None:
    print(" Tag non trouvé.")
else:
    print(f" Tag trouvé :")
    print(f"   User: {tag.userId}, Film: {tag.movieId}, Tag: '{tag.tag}'")


# ============================================================
# TEST 12 : Récupérer les liens d'un film
# ============================================================
print_separator("TEST 12 : get_link(db, movie_id=1)")
link = get_link(db, movie_id=1)
if link is None:
    print("Liens non trouvés.")
else:
    print(f" Liens trouvés :")
    print(f"   IMDB ID: {link.imdbId}")
    print(f"   TMDB ID: {link.tmdbId}")


# ============================================================
# TEST 13 : Récupérer plusieurs liens
# ============================================================
print_separator("TEST 13 : get_links(db, limit=5)")
links = get_links(db, limit=5)
print(f" {len(links)} liens récupérés :")
for link in links:
    print(f"   Film {link.movieId} → IMDB: {link.imdbId}, TMDB: {link.tmdbId}")


# ============================================================
# TEST 14 : Statistiques - Compter les films
# ============================================================
print_separator("TEST 14 : get_movie_count(db)")
movie_count = get_movie_count(db)
print(f" Nombre total de films : {movie_count}")


# ============================================================
# TEST 15 : Statistiques - Compter les évaluations
# ============================================================
print_separator("TEST 15 : get_rating_count(db)")
rating_count = get_rating_count(db)
print(f" Nombre total d'évaluations : {rating_count}")


# ============================================================
# TEST 16 : Statistiques - Compter les tags
# ============================================================
print_separator("TEST 16 : get_tag_count(db)")
tag_count = get_tag_count(db)
print(f" Nombre total de tags : {tag_count}")


# ============================================================
# TEST 17 : Statistiques - Compter les liens
# ============================================================
print_separator("TEST 17 : get_link_count(db)")
link_count = get_link_count(db)
print(f" Nombre total de liens : {link_count}")


# Fermer la session
db.close()
print_separator("TESTS TERMINÉS")
print(" Tous les tests ont été exécutés avec succès !")
  
  

     
