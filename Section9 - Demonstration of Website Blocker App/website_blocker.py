# import modules/libraries
import time
from datetime import datetime as dt

# set variables, host_path, redirect address and website_list
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16):
        print("The time is {} and you should not be at that website".format(dt.now()))
        time.sleep(5)
        break
    else:
        print("Ok you can go there")
    time.sleep(5)