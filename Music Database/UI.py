from Controller import *
from Music import *
from Repository import *

class UI:
    
    def __init__(self, ctrl):
        self.ctrl = ctrl

    def show_menu(self):

        while True:
            print('Commands:')
            print('1. Add song')
            print('2. Remove song')
            print('3. Display songs')
            print('0. Exit')

            cmd = int(input('Command: '))
            if cmd == 1:
                self.UI_add_song()
            if cmd == 2:
                self.UI_remove_song()
            if cmd == 3:
                self.UI_display_songs()
            if cmd == 0:
                return


    def UI_add_song(self):
        title = input('Enter the title of the song: ')
        duration = input('Enter the song duration: ')
        artist = input('Enter the artist of the song: ')
        genre = input('Enter the song genre: ')
        year = input('Enter the year when the song was relesed: ')

        song = self.ctrl.create_song(title, duration, artist, genre, year)

        print('The song ' + song.get_title() + ' has been saved !')

    def UI_remove_song(self):
        title = input('What song do you want to be removed? ')

        self.ctrl.remove_song(title)
        print('The song ' + title + ' has been removed!')

    def UI_display_songs(self):
        song = self.ctrl.get_all_music()

        if len(song) == 0:
            print('There are no songs in the database.')
        else:
            for music in song:
                print(music.get_title() + ' ' + music.get_duration() + ' ' + music.get_artist() + ' ' + music.get_genre() + ' ' + music.get_year())
    