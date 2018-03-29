numbers = [1,2,3]
my_txt_file = open("number_list.txt", "w")

for n in numbers:
    my_txt_file.write(str(n) + "\n")

my_txt_file.close()