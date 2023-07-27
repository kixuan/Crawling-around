import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By


# 提取每页的内容
def extract_contents(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    # 定位目标元素
    target_elements = soup.select(
        'body .sysu-contents .contents .main-content table tbody .sx_conter_item .sx_pa a')

    # 提取目标内容
    contents = []
    for element in target_elements:
        content = element.get_text()
        contents.append(content)

    print(contents)
    time.sleep(3)


def login_and_wait():
    url = "https://ehall.scnu.edu.cn/taskcenter/workflow/doing"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.86 Safari/537.36',
    }
    # 创建Chrome浏览器的实例
    driver = webdriver.Chrome()
    driver.get(url)  # 替换成实际登录页面的URL

    # 等待页面加载完成
    time.sleep(1)

    # 定位账号输入框并输入账号
    account_input = driver.find_element(By.ID, 'account')  # 替换成实际的账号输入框ID
    account_input.send_keys('账号')  # 替换成实际的账号

    password_input = driver.find_element(By.ID, 'password')  # 替换成实际的密码输入框ID
    password_input.send_keys('密码')  # 替换成实际的密码

    time.sleep(1)
    login_button = driver.find_element(By.CLASS_NAME,
                                       'btn.btn-primary.btn-block.auth-login-btn')  # 使用 By.CLASS_NAME 进行定位
    login_button.click()
    time.sleep(1)

    # 点击登录后
    print("ok")
    driver.switch_to.window(driver.window_handles[-1])
    confirm_button = driver.find_element(By.CSS_SELECTOR, 'span.login-check-comfirm a.btn.btn-danger')
    confirm_button.click()
    time.sleep(2)

    page_content = driver.page_source
    extract_contents(page_content)

    driver.quit()


# 调用函数进行登录和等待
login_and_wait()
