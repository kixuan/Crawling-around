from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开豆瓣电影top250页面
driver.get("https://movie.douban.com/top250")

# 循环翻页并获取电影信息
while True:
    # 使用 BeautifulSoup 解析页面内容
    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_hd = soup.findAll("div", attrs={"class": "hd"})
    for hd in all_hd:
        movie_title = hd.a.span.string.strip()
        print(movie_title)

    # 检查是否已经加载完所有电影
    next_page = driver.find_element(By.CSS_SELECTOR, "div.paginator span.next")
    if "disabled" in next_page.get_attribute("class"):
        break

    # 点击翻页按钮
    next_page.click()
    time.sleep(2)  # 等待页面加载

# 关闭浏览器
driver.quit()
