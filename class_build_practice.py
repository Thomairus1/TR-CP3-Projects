class Movies:
    def __init__(self, title, release_year, director, rating, genre, cast):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast
        
        
# prints the info about the movies        
    def __repr__(self):
        return f"Title: {self.title}\nRelease Year: {self.release_year}\nDirector: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}\n"
    
    def __lt__(self, other):
        if sort_ch == "title":
            return self.title < other.title
        elif sort_ch == "release year":
            return self.release_year < other.release_year
        else: 
            print("Invalid Response")

        
movie_list = [
    Movies("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins, Morgan Freeman"]),
    Movies("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta, Uma Thurman, Samuel L. Jackson"]),
    Movies("Dazed and Confused", 1993, "Richard Linklater", "R", "Comedy", ["Jason London, Wiley Wiggins, Matthew McConaughey"]),
    Movies("The Perks of Being a Wallflower", 2012, "Stephen Chbosky", "PG-13", "Drama", ["Logan Lerman, Emma Watson, Ezra Miller"]),
    Movies("Ferris Bueller's Day Off", 1986, "John Hughes", "PG-13", "Comedy", ["Matthew Broderick, Alan Ruck, Mia Sara"]),
    Movies("Dead Poets Society", 1989, "Peter Weir", "PG", "Drama", ["Robin Williams, Robert Sean Leonard, Ethan Hawke"]),
    Movies("The Breakfast Club", 1985, "John Hughes", "R", "Comedy", ["Molly Ringwald, Emilio Estevez, Judd Nelson"]),
    Movies("The Truman Show", 1998, "Peter Weir", "PG", "Drama", ["Jim Carrey, Laura Linney, Noah Emmerich"]),
    Movies("Alien", 1979, "Ridley Scott", "R", "Horror", ["Sigourney Weaver, Tom Skerritt, John Hurt"]),
    Movies("Back to the Future", 1985, "Robert Zemeckis", "PG", "Adventure", ["Michael J. Fox, Christopher Lloyd, Lea Thompson"]),
    Movies("The Terminator", 1984, "James Cameron", "R", "Sci-Fi", ["Arnold Schwarzenegger, Linda Hamilton, Michael Biehn"]),
    Movies("Braveheart", 1995, "Mel Gibson", "R", "Biography", ["Mel Gibson, Sophie Marceau, Patrick McGoohan"]),
    Movies("Memento", 2000, "Christopher Nolan", "R", "Thriller", ["Guy Pearce, Carrie-Anne Moss, Joe Pantoliano"]),
    Movies("The Usual Suspects", 1995, "Bryan Singer", "R", "Mystery", ["Kevin Spacey, Gabriel Byrne, Chazz Palminteri"]),
    Movies("The Sixth Sense", 1999, "M. Night Shyamalan", "PG-13", "Thriller", ["Bruce Willis, Haley Joel Osment, Toni Collette"]),
    Movies("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey, Kate Winslet, Kirsten Dunst"]),
    Movies("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood, Ian McKellen, Orlando Bloom"]),
    Movies("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio, Matt Damon, Jack Nicholson"]),
    Movies("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill, Laura Dern, Jeff Goldblum"]),
    Movies("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks, Matt Damon, Tom Sizemore"])
]

# tests print method 
print(movie_list[0])

print("-----------\n")

sort_ch = input("Do you want to sort movies by title or release year? ")
if sort_ch == "title":
    sorted_list = sorted(movie_list)
    print(sorted_list)
elif sort_ch == "release year":
    sorted_list1 = sorted(movie_list)
    print(sorted_list1)
    

print("-----------\n")

parameter = input("Do you want to search movies with genre, director or cast? ")
if parameter == "genre":
    search = input("Which genre are you looking for? (Drama, Crime, Comedy, Horror, Adventure, Sci-fi, Biography, Thriller, Mystery, Fantasy, or War)")
    search_list = []
    for movie in movie_list:
        if movie.genre == search:
            search_list.append(movie)
    print(search_list)
elif parameter == "director":
    search2 = input("Which director are you looking for?")
    search_list2 = []
    for movie in movie_list:
        if movie.genre == search2:
            search_list2.append(movie)
    print(search_list2)
elif parameter == "cast":
    search3 = input("Which director are you looking for?")
    search_list3 = []
    for movie in movie_list:
        if movie.cast == search3:
            search_list3.append(movie)
    print(search_list3)
