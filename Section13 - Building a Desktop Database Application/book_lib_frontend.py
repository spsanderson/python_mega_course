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
import book_lib_backend

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

# List box for returned results
lbox_Results = Listbox(window, height = 6, width = 35)
lbox_Results.grid(row = 2
    , column = 0
    , rowspan = 6
    , columnspan = 2
)

# Scrollbar
sb_Results = Scrollbar(window)
sb_Results.grid(row = 2, column = 2, rowspan = 6)

# Configure scroll bar to list_box_results
lbox_Results.configure(yscrollcommand = sb_Results.set)
sb_Results.configure(command = lbox_Results.yview)

# Buttons
# View All
b_ViewAll = Button(window, text = "View All", width = 12)
b_ViewAll.grid(row = 2, column = 3)

# Search Entry
b_Search = Button(window, text = "Search Entry", width = 12)
b_Search.grid(row = 3, column = 3)

# Add Entry
b_Add = Button(window, text = "Add Entry", width = 12)
b_Add.grid(row = 4, column = 3)

# Update Entry
b_Update = Button(window, text = "Update Selected", width = 12)
b_Update.grid(row = 5, column = 3)

# Delete Entry
b_Delete = Button(window, text = "Delete Selected", width = 12)
b_Delete.grid(row = 6, column = 3)

# Close application
b_Close = Button(window, text = "Close", width = 12)
b_Close.grid(row = 7, column = 3)

window.mainloop()