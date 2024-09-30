from movie import Movie

class MoviesController:
    def __init__(self, movies):
        self.movies: Movie = movies

    def order_movies(self, attribute, unwatched=False):
        movies = sorted(self.movies, key=lambda x: x.__getattribute__(attribute))
        if unwatched:
            return [movie for movie in movies if not movie.get_already_watched()]
        return movies
