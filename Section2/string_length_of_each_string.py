mylist = open("fruits.txt","r")
fruits = mylist.read()
fruits = fruits.splitlines()
mylist.close()

for each_fruit in fruits:
    print(len(each_fruit))