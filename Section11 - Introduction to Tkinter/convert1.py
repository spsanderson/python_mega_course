import tkinter as teek

window = teek.Tk()

def convert():
    a = "Hello World"
    #print("Hello World")
    grams.insert(teek.END, a)
    pounds.insert(teek.END, a)

# Button
b1 = teek.Button(window, text = "Convert", command = convert)
b1.grid(row = 0, column = 2)

# Enter values
entryText = teek.StringVar()
entryText.set("Enter a number of Kilograms")
entryDir = teek.Label(window, textvariable = entryText, height = 4)
entryDir.grid(row = 0, column = 0)

e1_value = teek.StringVar()
e1 = teek.Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

# Text boxes
    # Grams Label
gramsText = teek.StringVar()
gramsText.set("Grams:")
gramsDir = teek.Label(window, textvariable = gramsText, height = 4)
gramsDir.grid(row = 1, column = 0)
    # Grams text box where answer will be linked to
grams = teek.Text(window, height = 1, width = 20)
grams.grid(row = 1, column = 1)

    # Pounds Label
poundsText = teek.StringVar()
poundsText.set("Pounds/lbs:")
poundsDir = teek.Label(window, textvariable = poundsText, height = 4)
poundsDir.grid(row = 2, column = 0)
    # Pounds text box where answer will be linked to
pounds = teek.Text(window, height = 1, width = 20)
pounds.grid(row = 2, column = 1)

    # Ounces Label
ouncesText = teek.StringVar()
ouncesText.set("Ounces:")
ouncesDir = teek.Label(window, textvariable = ouncesText, height = 4)
ouncesDir.grid(row = 3, column = 0)
    # Ounces text box where answer will be linked to
ounces = teek.Text(window, height = 1, width = 20)
ounces.grid(row = 3, column = 1)

window.mainloop()