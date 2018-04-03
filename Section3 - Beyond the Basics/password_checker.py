correct_password = "python123"
name = input("Enter your name: ")
password = input("Enter password please: ")

while correct_password != password:
    password = input("Enter password please: ")

message = ("Hi {0}, you are logged in".format(name))
print(message)
