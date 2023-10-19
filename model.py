import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017")
# creates connection to MongoDB
db = conn["MovieShows"]
# creates database named "MovieShows"
movieCollection = db["Movies"]
# creates collection for movies

# showCollection = db["Shows"]
# creates collection for shows


class MenuFunctions:

    def make_menu(self):
        print("Welcome to my Movie App!")
        print("1. Add a movie")
        print("2. Edit a movie")
        print("3. Print movie list")
        print("4. Remove a movie")
        print("5. Exit")

    def add_movie(self):
        print("Adding a movie...")
        title = input("What is the title? ")
        genre = input("What genre is the movie? ")
        year = input("What year did it come out? ")
        time = input("How long is the movie(mins)? ")

        movie_data = {
            "title": title,
            "genre": genre,
            "year": year,
            "runtime": time
        }
        try:
            movieCollection.insert_one(movie_data)
            print("Movie added successfully!")
        except Exception as e:
            print(f"Error adding movie: {str(e)}")

    def edit_movie(self):
        print("edit movie")

    def print_movies(self):
        print("Printing Movies...")
        myquery = input("Searching for: ")
        try:
            mydoc = movieCollection.find(myquery)
        except Exception as e:
            print(f"Error searching... {str(e)}")
    def delete_movie(self):
        print("delete movie")
