import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                  "Safari/537.36 Edg/111.0.1661.44"
}
response = requests.get("https://movie.douban.com/top250", headers=headers)

# print(response)
print(response.status_code)
content = response.text
soup = BeautifulSoup(content, "html.parser")
all_hd = soup.findAll("div", attrs={"class": "hd"})
# print(all_hd)
for hd in all_hd:
    movie_title = hd.a.span.string.strip()  # 使用`.string`获取子节点的文本内容
    print(movie_title)

# if response.ok:
#     print(response.text)
# else:
#     print("请求失败")
