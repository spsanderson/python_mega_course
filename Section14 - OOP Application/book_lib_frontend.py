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

# This function allows us to get the index of the selected row
# in order to pass it to the database
def get_selected_row(event):
    global selected_tuple
    try:
        index = lbox_Results.curselection()[0]
        selected_tuple = lbox_Results.get(index)
        e_Title.delete(0, END)
        e_Title.insert(END, selected_tuple[1])
        e_Author.delete(0, END)
        e_Author.insert(END, selected_tuple[2])
        e_Year.delete(0, END)
        e_Year.insert(END, selected_tuple[3])
        e_ISBN.delete(0, END)
        e_ISBN.insert(END, selected_tuple[4])
        return(selected_tuple)
    except:
        pass

def view_command():
    lbox_Results.delete(0,END)
    for row in book_lib_backend.view():
        lbox_Results.insert(END, row)

def search_command():
    lbox_Results.delete(0, END)
    for row in book_lib_backend.search(e_Title.get(), e_Author.get(), e_Year.get(), e_ISBN.get()):
        lbox_Results.insert(END, row)

def add_command():
    lbox_Results.delete(0, END)
    book_lib_backend.insert(e_Title.get(), e_Author.get(), e_Year.get(), e_ISBN.get())
    lbox_Results.insert(END, (e_Title.get(), e_Author.get(), e_Year.get(), e_ISBN.get()))

def delete_command():
    book_lib_backend.delete(selected_tuple[0])
    view_command()

def update_commmand():
    lbox_Results.delete(0, END)
    book_lib_backend.update(
        selected_tuple[0]
        , e_Title.get()
        , e_Author.get()
        , e_Year.get()
        , e_ISBN.get()
    )
    view_command()

def close_command():
    window.destroy()

# Main window
window = Tk()

window.wm_title("BookStore")

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
# List Box binding
lbox_Results.bind('<<ListboxSelect>>', get_selected_row)

# Buttons #####################################################################
# View All
b_ViewAll = Button(window, text = "View All", width = 12, command = view_command)
b_ViewAll.grid(row = 2, column = 3)

# Search Entry
b_Search = Button(window, text = "Search Entry", width = 12, command = search_command)
b_Search.grid(row = 3, column = 3)

# Add Entry
b_Add = Button(window, text = "Add Entry", width = 12, command = add_command)
b_Add.grid(row = 4, column = 3)

# Update Entry
b_Update = Button(window, text = "Update Selected", width = 12, command = update_commmand)
b_Update.grid(row = 5, column = 3)

# Delete Entry
b_Delete = Button(window, text = "Delete Selected", width = 12, command = delete_command)
b_Delete.grid(row = 6, column = 3)

# Close application
b_Close = Button(window, text = "Close", width = 12, command = close_command)
b_Close.grid(row = 7, column = 3)

window.mainloop()