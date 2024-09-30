import json

from movie import Movie
from movies_controller import MoviesController

if __name__ == "__main__":
    # Load the movies from movies.json
    with open("movies.json", 'r', encoding='utf-8') as file:
        movies = json.load(file)

    # Create a list of Movie objects
    movies = [Movie(movie["title"], movie["year"], movie["director"], movie["imdb_rating"]) for movie in movies]

    movies_controller = MoviesController(movies)

    # Order by imdb_rating
    ordered_movies = movies_controller.order_movies("year", True)
    print("\nMovies ordered by imdb_rating:")
    for movie in ordered_movies:
        print(movie.get_title())