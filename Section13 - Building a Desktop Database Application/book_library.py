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

# Labels / Entry Box's
lbl_Title = Label(window, text = "Title:")
lbl_Title.grid(row = 0, column = 0)
e_Title = StringVar()
e_Title = Entry(window, textvariable = e_Title)
e_Title.grid(row = 0, column = 1)

lbl_Year = Label(window, text = "Year:")
lbl_Year.grid(row = 1, column = 0)
e_Year = StringVar()
e_Year = Entry(window, textvariable = e_Year)
e_Year.grid(row = 1, column = 1)

lbl_Author = Label(window, text = "Author:")
lbl_Author.grid(row = 0, column = 2)
e_Author = StringVar()
e_Author = Entry(window, textvariable = e_Author)
e_Author.grid(row = 0, column = 3)

lbl_ISBN = Label(window, text = "ISBN:")
lbl_ISBN.grid(row = 1, column = 2)
e_ISBN = StringVar()
e_ISBN = Entry(window, textvariable = e_ISBN)
e_ISBN.grid(row = 1, column = 3)

window.mainloop()