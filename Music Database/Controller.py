from Music import *
from Repository import *

class MusicController:
    def __init__(self, R):
        self.R = R

    def create_song(self, title, duration, artist, genre, year):
        song = Music(title, duration, artist, genre, year)
        self.R.add_song(song)

        return song

    def remove_song(self, title):
        self.R.remove_song(title)

    def get_all_music(self):
        return self.R.get_music()


# R = MusicRepository()
# C = MusicController(R)



