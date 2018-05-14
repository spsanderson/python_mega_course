"""
A program that stores certain book information:
    1. Title
    2. Author
    3. Year
    4. ISBN

The user can perform the following:
    1. View all records
    2. Search and entry
    3. Add and entry
    4. Update and entry
    5. Delete and entry
    6. Close the program

"""

from tkinter import *
# Main window
window = Tk()

# Labels
lbl_Title = Label(window, text = "Title:")
lbl_Title.grid(row = 0, column = 0)

lbl_Year = Label(window, text = "Year:")
lbl_Year.grid(row = 1, column = 0)

lbl_Author = Label(window, text = "Author:")
lbl_Author.grid(row = 0, column = 2)

lbl_ISBN = Label(window, text = "ISBN:")
lbl_ISBN.grid(row = 1, column = 2)

window.mainloop()