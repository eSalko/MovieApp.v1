import tkinter as tk
import pymongo


#               Database
# creates connection to MongoDB
conn = pymongo.MongoClient("mongodb://localhost:27017")
# creates database named "MovieShows"
db = conn["MovieShows"]
# creates collection for movies
movieCollection = db["Movies"]

# on_click function to submit data to database
def on_submit():

    movie_title = titleEntry.get()
    movie_genre = genreEntry.get()
    movie_year = yearEntry.get()
    movie_runtime = runtimeEntry.get()

    movie_data = {
        "title": movie_title,
        "genre": movie_genre,
        "year": movie_year,
        "runtime": movie_runtime
    }

    try:
        if movieCollection.count_documents({"title": movie_title}) == 0:
            movieCollection.insert_one(movie_data)
        else:
            print("A movie with the same title already exists!")
    except Exception as e:
        print(f"Error adding movie: {str(e)}")

    movieCollection.insert_one(movie_data)

    result_label.config(text="Movie details saved to MongoDB")


#               GUI Window
# creating window variable to add widgets to
window = tk.Tk()
window.geometry("500x500")
# Label widget is just a text box
greeting = tk.Label(text="Welcome to my movie app!")
# .pack() puts the label in the window where it can (using the least space possible)
greeting.pack()

# title, genre, year, runtime
tk.Label(text="Title: ").pack()
titleEntry = tk.Entry(width=50)
titleEntry.pack()

tk.Label(text="Genre: ").pack()
genreEntry = tk.Entry(width=50)
genreEntry.pack()

tk.Label(text="Year: ").pack()
yearEntry = tk.Entry(width=50)
yearEntry.pack()

tk.Label(text="Runtime(mins): ").pack()
runtimeEntry = tk.Entry(width=50)
runtimeEntry.pack()

submitBtn = tk.Button(text="Submit!", command=on_submit)
submitBtn.pack()

result_label = tk.Label(text="")
result_label.pack()





# window won't show / program won't run without this line of code
window.mainloop()
