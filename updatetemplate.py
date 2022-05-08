from datetime import date
from tkinter import W

curdate = date.today().strftime("%Y/%-m/%d")
curdate = str(curdate)
curdate = curdate.replace('-', '/')
url = f"https://wol.jw.org/en/wol/h/r1/lp-e/{curdate}"
with open("/mnt/c/Users/akaza/Documents/Notes/DailyText/template.md", W) as file:
    file.write(f"---\nlink: {url}\n---\n##[Daily Text] {url}")