class Movies:
    def __init__(self, title, release_year, director, rating, genre, cast):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast
    def __str__(self):
        return f"Title: {self.title}\nRelease Year: {self.release_year}\nDirector: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}\n"
movie1 = Movies("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins, Morgan Freeman"])
movie2 = Movies("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta, Uma Thurman, Samuel L. Jackson"])
movie3 = Movies("Dazed and Confused", 1993, "Richard Linklater", "R", "Comedy", ["Jason London, Wiley Wiggins, Matthew McConaughey"])
movie4 = Movies("The Perks of Being a Wallflower", 2012, "Stephen Chbosky", "PG-13", "Drama", ["Logan Lerman, Emma Watson, Ezra Miller"])
movie5 = Movies("Ferris Bueller's Day Off", 1986, "John Hughes", "PG-13", "Comedy", ["Matthew Broderick, Alan Ruck, Mia Sara"])
movie6 = Movies("Dead Poets Society", 1989, "Peter Weir", "PG", "Drama", ["Robin Williams, Robert Sean Leonard, Ethan Hawke"])
movie7 = Movies("The Breakfast Club", 1985, "John Hughes", "R", "Comedy", ["Molly Ringwald, Emilio Estevez, Judd Nelson"])
