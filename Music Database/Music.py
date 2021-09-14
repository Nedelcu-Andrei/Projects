class Music:
    def __init__(self, title, duration, artist, genre, year):
        self.title = title
        self.duration = duration
        self.artist = artist
        self.genre = genre
        self.year = year

    def print_music(self):
        print(self.title, self.duration, self.artist, self.genre, self.year)

# a = Music('alina', '3', 'boteanu', 'emo', '2020')
# a.print_music()

# Getters

    def get_title(self):
        return self.title 
    
    def get_duration(self):
        return self.duration
    
    def get_artist(self):
        return self.artist

    def get_genre(self):
        return self.genre

    def get_year(self):
        return self.year

# Setters

    def set_title(self, new_title):
        self.title = new_title

    def set_duration(self, new_duration):
        self.duration = new_duration

    def set_artist(self, new_artist):
        self.artist = new_artist

    def set_genre(self, new_genre):
        self.genre = new_genre

    def set_year(self, new_year):
        self.year = new_year


# a = Music('alina', '3', 'boteanu', 'emo', '2020')
# a.set_title('valer')
# a.print_music()