import requests

def staticfilesnumbered(ispadded):
    x=0
    while x < 115:
        y = x
        if ispadded:
            x = str(x)
            x = x.zfill(3)
        #url = f"https://pomf2.lain.la/img/{x}.png"
        url = f"https://zz.ht/render/miku/{x}.png"
        r = requests.get(url)
        status = r.status_code
        print(f"{x}.png\t\t{status}")
        filename = f"{x}.png"
        with open(filename, 'wb') as f:
            f.write(r.content)
        x = y
        x += 1

def allimgsinsite(url):
    from bs4 import BeautifulSoup, Soupstrainer
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    for imglink in soup.find_all('img'):
        print(imglink.get('src'))


staticfilesnumbered(True)
