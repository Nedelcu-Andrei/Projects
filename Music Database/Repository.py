from Music import *

class MusicRepository:
    def __init__(self):
        self.music = []

    def add_song(self, song):
        self.music.append(song)

    def remove_song(self, x):
        for song in self.music:
            if song.get_title() == x:
                self.music.remove(song)
                return

    def get_music(self):
        return self.music

    def songs_number(self):
        return len(self.music)


# a = Music('Titanic', '3:30', 'James Cameron', 'emo', '1997')
# b = Music('Godfather', '2:00', 'Francis Ford Coppola', 'emo', '1972')
# c = Music('JafulValeriu', '2:00', 'Francis Ford Coppola', 'emo', '1972')

# Repos = MusicRepository()

# Repos.add_song(a)
# Repos.add_song(b)
# Repos.add_song(c)
# Repos.remove_song('Titanic')

# print(Repos.songs_number())