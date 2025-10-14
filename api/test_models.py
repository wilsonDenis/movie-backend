from database import SessionLocal
from models import Movie, Rating, Tag, Link

db=SessionLocal()
# Récupérer les 5 premiers films de la base de données
movies = db.query(Movie).limit(5).all()
for movie in movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")
    
# Récupere 
# films du genre action
action_movies1=db.query(Movie).filter(Movie.genres.like('%Action%')).limit(5).all()
action_movies2=db.query(Movie).filter(Movie.genres.contains('Action')).limit(5).all()
for movie in action_movies1:
    print(f"Action Movie 1 - ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")
for movie in action_movies2:
    print(f"Action Movie 2 - ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")    
    
# Récupérer les 5 premiers ratings
ratings =db.query(Rating).limit(5).all()

for rating in ratings:
    print(f"Rating - User ID: {rating.userId}, Movie ID: {rating.movieId}, Rating: {rating.rating}, Timestamp: {rating.timestamp}")

#films dont note >= 4.5
high_rated_movies1=db.query(Movie.title, Rating.rating).join(Rating).filter(Rating.rating >= 4.5).all()
for title, rating in high_rated_movies1:
    print(f"High Rated Movie - Title: {title}, Rating: {rating}")
high_rated_movies2=db.query(Movie.title, Rating.rating).join(Rating).filter(Rating.rating >= 4.5,Movie.movieId==Rating.movieId).limit(5).all()
for title, rating in high_rated_movies2:
    print(f"High Rated Movie - Title: {title}, Rating: {rating}")

#Récuperer les tags pour un film spécifique
tags=db.query(Tag).filter(Tag.movieId==1).all()
for tag in tags:
    print(f"Tag - User ID: {tag.userId}, Movie ID: {tag.movieId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")
    
    
#Récuperer le lien pour un film spécifique
link=db.query(Link).filter(Link.movieId==1).first()
#tester de recuperer le lien de classe Link

Links=db.query(Link).limit(5).all()
for link in Links:
    print(f"Link - Movie ID: {link.movieId}, IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")
    
    
#fermer la session
db.close()