from turtle import title

import requests
from html2text import HTML2Text
from lxml import etree
from html import unescape
import os

"""
requirements
打了箭头的才需要手动安装，其余是自动安装的依赖库
certifi==2021.10.8
charset-normalizer==2.0.7
cssselect==1.1.0
html2text==2020.1.16  --  <--
idna==3.3
lxml==4.6.3  -----------  <--
requests==2.26.0 -------  <--
urllib3==1.26.7
"""


def crawl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/95.0.4638.54 Safari/537.36",
    }
    print("在爬了...")
    # 配置header破反爬
    response = requests.get(url, headers=headers)
    # 200就继续
    if response.status_code == 200:
        html = response.content.decode("utf8")
        # print(html)
        tree = etree.HTML(html)
        # 找到需要的html块
        title = tree.xpath('//*[@id="articleContentId"]/text()')[0]
        block = tree.xpath('//*[@id="content_views"]')
        # html
        ohtml = unescape(etree.tostring(block[0]).decode("utf8"))

        print("title:", title)
        save(ohtml, title)
        # 完成！
        print("爬完噜!")
    else:
        print("错了错了!")


def save(html, title):
    if "output" not in os.listdir():
        # 不存在输出文件夹就创建
        os.mkdir("output")
    with open(f"output/{title}.html", 'w', encoding='utf8') as html_file:
        # 保存html
        html_file.write(html)

    with open(f"output/{title}.md", 'w', encoding='utf8') as md_file:
        # 保存markdown
        text_maker = HTML2Text()
        # md转换
        md_text = text_maker.handle(html)
        md_file.write(md_text)


if __name__ == '__main__':
    # 你想要爬取的文章url
    url = "https://blog.csdn.net/LW_20180806/article/details/123718853?spm=1001.2014.3001.5502"
    crawl(url)
