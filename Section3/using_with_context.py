# Typically we would use the following:
#
#    myfile = open("example.txt","w")
#    myfile.write("Something\n")
#    myfile.close()
#
# it is instead preferred to use the `with` context as it will auto close the fil
# for you, this way if you forget to use the `.close()` you're still ok

with open("example.txt","w") as myfile:
    myfile.write("Something\n")
