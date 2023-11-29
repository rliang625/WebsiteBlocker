import time
from datetime import datetime as dt

host_temp = r"C:\Users\rlian\Code\Python Projects\WebsiteBlocker\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.yahoo.com","yahoo.com"]

while True:
    if 9 <= dt.now().hour < 17:
        print ("Working hours...")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print ("Unpaid Working Hours")
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(60)