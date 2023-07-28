from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/warandpeace.html")
bsOBj = BeautifulSoup(html,features="lxml")
nameList = bsOBj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())

length = bsOBj.findAll(text="the prince")
print(len(length))