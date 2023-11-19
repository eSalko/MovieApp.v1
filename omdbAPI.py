import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# api key and url to access OMDB API
api_key = '46aa50b0'
base_url = 'http://www.omdbapi.com/'


# delete temp text in titleEntry
def temp_text(e):
    titleEntry.delete(0, "end")


# function to get movie details from OMDB API
def get_movie_details(event=None):
    title = titleEntry.get()
    parameters = {'apikey': api_key, 't': title}
    # creating response variable for JSON data from API
    response = requests.get(base_url, params=parameters)
    # data variable for gathered data in JSON format
    data = response.json()
    # checking to see if Response was succesful, then proceed to gathering data
    if data['Response'] == 'True':
        # gather and display movie data from JSON data
        titleLabel.config(text=f"Movie Title: {data['Title']}")
        yearLabel.config(text=f"Movie Year: {data['Year']}")
        runtimeLabel.config(text=f"Movie Runtime: {data['Runtime']}")
        genreLabel.config(text=f"Movie Genre: {data['Genre']}")
        plotLabel.config(text=f"Movie Plot: {data['Plot']}", wraplength=400)
        errorLabel.config(text=" ")
        # keeping track of data in console as well. just because.
        print(f"Title: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"Runtime: {data['Runtime']}")
        print(f"Genre: {data['Genre']}")
        print(f"Plot: {data['Plot']}")
        # creating variable to display movie poster.
        poster_url = data['Poster']
        # checking to see if poster exists, if so, proceed with the image.
        if poster_url != 'N/A':
            # if poster is available, send HTTP GET request to url to get image.
            response = requests.get(poster_url)
            # downloads and opends image and convert into a file-like object that Pillow library can read
            img = Image.open(BytesIO(response.content))
            # converts into a 'PhotoImage' object, necessary for displaying the image in Tkinter label widget
            photo = ImageTk.PhotoImage(img)
            # sets image attribute of the posterLabel widget to the image displaying the Image.
            posterLabel.config(image=photo)
            # stores a reference to the PhotoImage object, so it is not garbage-collected.
            posterLabel.image = photo
        else:
            # error message if poster is unavailable
            errorLabel.config(text="No poster available")

    else:
        # error message if movie is not found or any other error is detected.
        tk.Label(text="Error: Cannot find movie!").pack()
        print(f"Error: {data['Error']}")


# creates Tkinter window
window = tk.Tk()
# sets window title
window.title("OMDB Movie App")
# sets window size
window.geometry("500x800")
# Greeting label for window
greeting = tk.Label(text="Welcome to my Movie App!")
greeting.pack()

tk.Label(text="What movie would you like to search for?").pack()
titleEntry = tk.Entry(width=50)
titleEntry.insert(0, "Movie Search")
titleEntry.pack(pady=20)
# creating temporary text that disappears when you click on the entry box
titleEntry.bind("<FocusIn>", temp_text)
# allows to search by pressing the Return/Enter key
titleEntry.bind("<Return>", get_movie_details)
# button to begin searching for desired movie
tk.Button(text="Search", command=get_movie_details).pack()

titleLabel = tk.Label(text='Movie Title: ')
titleLabel.pack()

yearLabel = tk.Label(text='Movie Year: ')
yearLabel.pack()

runtimeLabel = tk.Label(text='Movie Runtime: ')
runtimeLabel.pack()

genreLabel = tk.Label(text='Movie Genre: ')
genreLabel.pack()

plotLabel = tk.Label(text='Movie Plot: ')
plotLabel.pack()

posterLabel = tk.Label(window)
posterLabel.pack()

errorLabel = tk.Label()
errorLabel.pack()

# displaying the window. Window would not run without this line
window.mainloop()
