import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By


def extract_contents(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    target_elements = soup.select('body .sysu-contents .contents .main-content table tbody .sx_conter_item .sx_pa a')
    contents = []
    for element in target_elements:
        content = element.get_text()
        contents.append(content)
    return contents


def login_and_wait():
    url = "https://ehall.scnu.edu.cn/taskcenter/workflow/doing"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.86 Safari/537.36',
    }
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    # 登录
    account_input = driver.find_element(By.ID, 'account')
    account_input.send_keys('账号')
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('密码')
    time.sleep(1)

    login_button = driver.find_element(By.CLASS_NAME, 'btn.btn-primary.btn-block.auth-login-btn')
    login_button.click()
    time.sleep(1)

    print("ok")
    driver.switch_to.window(driver.window_handles[-1])
    confirm_button = driver.find_element(By.CSS_SELECTOR, 'span.login-check-comfirm a.btn.btn-danger')
    confirm_button.click()
    time.sleep(2)

    auto_paginate(driver)

    driver.quit()


def auto_paginate(driver):
    current_page = 1
    while True:
        # 处理当前页的内容
        page_content = driver.page_source
        contents = extract_contents(page_content)
        print(contents)
        time.sleep(1)

        # 在这里判断是否还有下一页
        current_div = driver.find_element(By.CSS_SELECTOR, "div.fy_num.current")
        next_a = current_div.find_element(By.XPATH, "./following-sibling::div//a")

        # 使用JavaScript点击下一页按钮
        next_a.click()
        time.sleep(1)


# 调用函数进行登录和等待
login_and_wait()
