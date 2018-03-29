mylist = open("fruits.txt","r")
fruits = mylist.read()
fruits = fruits.splitlines()
print(fruits)

for each_fruit in fruits:
    name_length = len(each_fruit)
    print(each_fruit)
    print(name_length)