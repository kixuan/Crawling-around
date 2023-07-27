import requests

r = requests.get("https://github.com/favicon.ico")
# wb：二进制写的形式打开
with open('favicon.ico', 'wb') as f:
    f.write(r.content)