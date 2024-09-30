class Movie:
    def __init__(self, title, year, director, imdb_rating):
        self.title = title
        self.year = year
        self.director = director
        self.imdb_rating = imdb_rating
        self.already_watched = False

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_director(self):
        return self.director

    def set_director(self, director):
        self.director = director

    def get_imdb_rating(self):
        return self.imdb_rating

    def set_imdb_rating(self, imdb_rating):
        self.imdb_rating = imdb_rating

    def get_already_watched(self):
        return self.already_watched

    def set_already_watched(self, already_watched):
        self.already_watched = already_watched