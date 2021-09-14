class Movie:
    def __init__(self, title, duration, director, year):
        self.title = title
        self.duration = duration
        self.director = director
        self.year = year

    def __str__(self):
        return self.title + ' ruleaza cu durata de ' + self.duration + ' este regizat de ' + self.director + ' si a fost lansat in anul ' + self.year


    # Getters
    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration

    def get_director(self):
        return self.director

    def get_year(self):
        return self.year

    # Setters
    def set_title(self, new_title):
        self.title = new_title

    def set_duration(self, new_duration):
        self.duration = new_duration

    def set_director(self, new_director):
        self.director = new_director

    def set_year(self, new_year):
        self.year = new_year


# a = Movie('Titanic', '3:30', 'James Cameron', '1997')
# a.set_title('Godfather')
# print(a)