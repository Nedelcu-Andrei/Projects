from Movie import *

class MovieRepository:
    def __init__(self):
        self.movies = []

    def add_movie(self, x):
        self.movies.append(x)

    def remove_movie(self, x):
        for movie in self.movies:
            if movie.get_title() == x:
                self.movies.remove(movie)
                return

    def get_movies(self):
        return self.movies

    def movies_length(self):
        return len(self.movies)

# a = Movie('Titanic', '3:30', 'James Cameron', '1997')
# b = Movie('Godfather', '2:00', 'Francis Ford Coppola', '1972')
# c = Movie('JafulValeriu', '2:00', 'Francis Ford Coppola', '1972')

# m = MovieRepository()

# m.add_movie(a)
# m.add_movie(b)
# m.add_movie(c)

# print(m.movies_length())
