import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/page3.html")
bsOBj = BeautifulSoup(html,features="lxml")

# 1.处理子标签和其他后代标签children()
# 子标签时父标签的后一个   后代标签时父标签的后所有descendants()
# for child in bsOBj.find("table",{"id":"giftList"}).children:
#     print(child)

# 处理兄弟标签  --具有相同的父级标题   siblings()
# for siblings in bsOBj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(siblings)

# 处理父标签  parent()  --打印这张图片标签的父标签的兄弟标签的文字
print(bsOBj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# 正则表达式
images = bsOBj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

# 2.5 获取属性 p43
# 2.6 Lambda表达式 p43