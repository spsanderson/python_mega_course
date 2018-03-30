temp = [10,-20,-289,100]

def temp_to_txt(temp, filepath):
    with open("temp.txt","w") as file:
        for c in temp:
            if c > -273.15:
                f = c * (9/5) + 32
                file.write(str(f) + "\n")

temp_to_txt(temp, "temp.txt")
