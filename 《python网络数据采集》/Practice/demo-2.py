from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开豆瓣电影top250页面
driver.get("https://movie.douban.com/top250")

# 模拟滚动加载更多电影
while True:
    # 滚动到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待页面加载

    # 判断是否已经滚动到底部
    current_height = driver.execute_script("return document.body.scrollHeight")
    new_height = current_height
    while True:
        # 再次滚动到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # 等待页面加载
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == current_height:
            break
        current_height = new_height

    # 检查是否已经加载完所有电影
    if driver.find_element_by_css_selector("div.paginator").find_element_by_css_selector("span.next"):
        break

# 使用 BeautifulSoup 解析页面内容
soup = BeautifulSoup(driver.page_source, "html.parser")
all_hd = soup.findAll("div", attrs={"class": "hd"})
for hd in all_hd:
    movie_title = hd.a.span.string.strip()
    print(movie_title)

# 关闭浏览器
driver.quit()
