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
#from book_lib_backend import Database

# Create database object
#database = Database("books.db")

class Frontend:

# Main window
    def __init__(self, window):
        
        self.window = Tk()

        self.window.wm_title("BookStore")

        # Labels / Entry Box's
        self.lbl_Title = Label(self.window, text = "Title:")
        self.lbl_Title.grid(row = 0, column = 0)
        self.e_Title = StringVar()
        self.e_Title = Entry(self.window, textvariable = self.e_Title)
        self.e_Title.grid(row = 0, column = 1)

        self.lbl_Year = Label(self.window, text = "Year:")
        self.lbl_Year.grid(row = 1, column = 0)
        self.e_Year = StringVar()
        self.e_Year = Entry(self.window, textvariable = self.e_Year)
        self.e_Year.grid(row = 1, column = 1)

        self.lbl_Author = Label(self.window, text = "Author:")
        self.lbl_Author.grid(row = 0, column = 2)
        self.e_Author = StringVar()
        self.e_Author = Entry(self.window, textvariable = self.e_Author)
        self.e_Author.grid(row = 0, column = 3)

        self.lbl_ISBN = Label(self.window, text = "ISBN:")
        self.lbl_ISBN.grid(row = 1, column = 2)
        self.e_ISBN = StringVar()
        self.e_ISBN = Entry(self.window, textvariable = self.e_ISBN)
        self.e_ISBN.grid(row = 1, column = 3)

        # List box for returned results
        self.lbox_Results = Listbox(self.window, height = 6, width = 35)
        self.lbox_Results.grid(row = 2
            , column = 0
            , rowspan = 6
            , columnspan = 2
        )

        # Scrollbar
        self.sb_Results = Scrollbar(self.window)
        self.sb_Results.grid(row = 2, column = 2, rowspan = 6)

        # Configure scroll bar to list_box_results
        self.lbox_Results.configure(yscrollcommand = self.sb_Results.set)
        self.sb_Results.configure(command = self.lbox_Results.yview)
        # List Box binding
        self.lbox_Results.bind('<<ListboxSelect>>', self.get_selected_row)

        # Buttons #####################################################################
        # View All
        self.b_ViewAll = Button(window, text = "View All", width = 12, command = view_command)
        self.b_ViewAll.grid(row = 2, column = 3)

        # Search Entry
        self.b_Search = Button(window, text = "Search Entry", width = 12, command = search_command)
        self.b_Search.grid(row = 3, column = 3)

        # Add Entry
        self.b_Add = Button(window, text = "Add Entry", width = 12, command = add_command)
        self.b_Add.grid(row = 4, column = 3)

        # Update Entry
        self.b_Update = Button(window, text = "Update Selected", width = 12, command = update_commmand)
        self.b_Update.grid(row = 5, column = 3)

        # Delete Entry
        self.b_Delete = Button(window, text = "Delete Selected", width = 12, command = delete_command)
        self.b_Delete.grid(row = 6, column = 3)

        # Close application
        self.b_Close = Button(window, text = "Close", width = 12, command = close_command)
        self.b_Close.grid(row = 7, column = 3)

        self.window.mainloop()    

    # This function allows us to get the index of the selected row
    # in order to pass it to the database
    def get_selected_row(self, event):
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

    def view_command(self):
        lbox_Results.delete(0,END)
        for row in database.view():
            lbox_Results.insert(END, row)

    def search_command(self):
        lbox_Results.delete(0, END)
        for row in database.search(e_Title.get(), e_Author.get(), e_Year.get(), e_ISBN.get()):
            lbox_Results.insert(END, row)

    def add_command(self):
        lbox_Results.delete(0, END)
        database.insert(e_Title.get(), e_Author.get(), e_Year.get(), e_ISBN.get())
        lbox_Results.insert(END, (e_Title.get(), e_Author.get(), e_Year.get(), e_ISBN.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])
        view_command()

    def update_commmand(self):
        lbox_Results.delete(0, END)
        database.update(
            selected_tuple[0]
            , e_Title.get()
            , e_Author.get()
            , e_Year.get()
            , e_ISBN.get()
        )
        view_command()

    def close_command(self):
        window.destroy()

    