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
            'Cookie': '__mta=55424788.1686576258158.1686577441430.1686577575623.6; uuid_n_v=v1; '
                      'uuid=6E3FC650092411EEB6A41DA4355E52ADD4F1C4FB8D42463590B8284BC8D0BF8F; '
                      '_csrf=e67799092b0764a329581437b857c1a8275ef3ce21de62e7b0aff901e2819ac4; '
                      '_lxsdk_cuid=188afc75b7ec8-069c80f6cdb16b-7a545470-154ac4-188afc75b7ea8; '
                      '_lxsdk=6E3FC650092411EEB6A41DA4355E52ADD4F1C4FB8D42463590B8284BC8D0BF8F; '
                      'WEBDFPID=5x580v6195xz5w2uzz50wzwu13wwx612811zuwzw73z97958vuu25476-2001937533206'
                      '-1686577530435MAIKMYEfd79fef3d01d5e9aadc18ccd4d0c95079555; '
                      'token=AgGMJHVl0SjX4ou2N-G9fOygrijKRESi_ocayau7EHyCLowaRl_HendaZ3CtYUF054'
                      '-UqaZBN8HMOAAAAAARGQAA9Qw8yuIPsMj0RXRw7JG47uXyz-jN97kHc7qCh0MQZaMsGmyDuTlFpWZLbeVNhX9n; '
                      'uid=2629196613; uid.sig=DV8-2Trs8xdqzZ-A7zgTFMJRlnc; _lxsdk_s=188afc75b80-278-67b-ca7||12',
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
