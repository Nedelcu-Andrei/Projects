from Controller import *
from Movie import *
from Repository import *

class UI:
    def __init__(self, ctrl):
        self.ctrl = ctrl

    def show_menu(self):

        while True:
            print('Commands:')
            print('1. Add movie')
            print('2. Remove movie')
            print('3. Show movies')
            print('0. Exit')

            cmd = int(input('Command: '))
            if cmd == 1:
                self.UI_add_movie()
            if cmd == 2:
                self.UI_remove_movie()
            if cmd == 3:
                self.UI_show_movies()
            if cmd == 0:
                return

    def UI_add_movie(self):
        title = input('Enter the title of the movie: ')
        duration = input('Enter the movie duration: ')
        director = input('Enter the movie director: ')
        year = input('Enter the creation year of the movie: ')

        movie = self.ctrl.create_movie(title, duration, director, year)

        print('The movie '+ movie.get_title()+ ' has been saved!')

    def UI_remove_movie(self):
        title = input('What movie do you want to be removed?')

        self.ctrl.remove_movie(title)
        print('The movie '+ title + ' has been removed!')

    def UI_show_movies(self):
        movies = self.ctrl.get_all_movies()

        if len(movies) == 0:
            print('There are no movies in the database.')
        else:
            for movie in movies:
                print(movie.get_title() + ' ' + movie.get_duration() + ' ' + movie.get_director() + ' ' + movie.get_year())

