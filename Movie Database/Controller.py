from Movie import *
from Repository import *

class MovieController:
    def __init__(self, repos):
        self.repos = repos

    def create_movie(self, title, duration, director, year):
        movie = Movie(title, duration, director, year)
        self.repos.add_movie(movie)

        return movie 

    def remove_movie(self, title):
        self.repos.remove_movie(title)

    def get_all_movies(self):
        return self.repos.get_movies()
        

# repos = MovieRepository()
# c = MovieController(repos)


# c.create_movie('Titanic', '3:30', 'James Cameron', '1997')
