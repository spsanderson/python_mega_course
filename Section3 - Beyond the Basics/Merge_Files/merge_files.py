# Import glob2 to read files in director
import glob2
from datetime import datetime

# create a variable to hold file names
f = glob2.glob("file*.txt")
# use the with context to create and write to a file so you don't need to worry about using clos()
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%F") + ".txt","w") as myfile:
    # iterate through the files that are placed in the var f
    for file in f:
        # use with context to open the files in f
        with open(file,"r") as fname:
            # write the contents of f to myfile
            myfile.write(fname.read() + "\n")

