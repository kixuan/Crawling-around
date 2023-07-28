import json
import requests
from requests.exceptions import RequestException
import re
import time
from selenium import webdriver

# 1.获取首页代码内容
def get_one_page(url):
    try:
        headers = {
            'Cookie': '',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.86 Safari/537.36'
        }

        # 创建Chrome浏览器的实例
        driver = webdriver.Chrome()
        driver.get(url)
        # 等待页面加载完成
        time.sleep(5)
        # 获取页面内容
        content = driver.page_source
        driver.quit()
        return content
    except RequestException:
        return None
    #     response = requests.get(url, headers=headers)
    #     if response.status_code == 200:
    #         return response.text
    # except RequestException:
    #     return None


# 2.正则获取相关内容，并进行格式处理
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {'index': item[0],
               'image': item[1],
               'title': item[2],
               'actor': item[3].strip()[3:],
               'time': item[4].strip()[5:],
               'score': item[5] + item[6]
               }


# 3.写进文件
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 调用main方法
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


# 分页爬取
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        # 速度过快，则会无响应
        time.sleep(1)
