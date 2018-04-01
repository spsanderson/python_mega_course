import glob2
from datetime import datetime

f = glob2.glob("file*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%F") + ".txt","w") as myfile:
    for file in f:
        with open(file,"r") as fname:
            myfile.write(fname.read() + "\n")

