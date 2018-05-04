import tkinter as teek

window = teek.Tk()

def km_to_miles():
#    print(e1_value.get())
    miles = float(e1_value.get()) * 1.6
    t1.insert(teek.END, miles)

b1 = teek.Button(window, text="Execute", command = km_to_miles)
b1.grid(row = 0, column = 0)

e1_value = teek.StringVar()
e1 = teek.Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

t1 = teek.Text(window, height = 5, width = 20)
t1.grid(row = 0, column = 2)

window.mainloop()