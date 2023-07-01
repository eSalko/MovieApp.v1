from tkinter import *

root = Tk()

# Label Entries

Label(root, width=50, text="movie title").grid(row=0, column=0)
# Data Entries
Entry(root, width=50, bg="green", fg="white").grid(row=0, column=1)
Entry(root, width=50).grid(row=1, column=0)

root.mainloop()


