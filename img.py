import requests

x=0
while x < 115:
    url = f"https://pomf2.lain.la/img/{x}.png"
    r = requests.get(url)
    status = r.status_code
    print(f"{x}.png\t\t{status}")
    filename = f"{x}.png"
    with open(filename, 'wb') as f:
        f.write(r.content)
    x += 1

