# import libraries
import time
from datetime import datetime as dt

# make varialbes, you will need to read host_path as raw string
host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
# Can be any websites you'd like
website_list = ["https://www.facebook.com"
    , "facebook.com"
    , "https://www.twitter.com"
    , "https://twitter.com"
    , "twitter.com"]

while True:
    # if just now is less than right now is less than then, go through the loop
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16):
        print("The time is {} and you should be working".format(dt.now()))
        # open the host_path using with as it will auto-close
        with open(host_path, 'r+') as file:
            # get the contents of the host file
            content = file.read()
            # for loop to add websites listed in website_list to host file
            for website in website_list:
                # if the website is already there skip it else write it
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        # work/homework hours etc are now done, you should be able to roam about freely
        print("Ok you can go there")
        # use with to open the host_path
        with open(host_path, 'r+') as file:
            # read everything in on a separate line
            content = file.readlines()
            # since we are deleting the things we added, lets start at the very beginning of the file
            file.seek(0)
            for line in content:
                # if the website is in the file skip that line and get the next
                if not any(website in line for website in website_list):
                    # write the lines you did not skip
                    file.write(line)
            # truncate the extra output
            file.truncate()
    # run again in n seconds
    time.sleep(5)