import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def extract_contents(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    target_elements = soup.select('body .sysu-contents .contents .main-content table tbody .sx_conter_item .sx_pa a')
    contents = []
    for element in target_elements:
        content = element.get_text()
        contents.append(content)
    return contents


def fetch_page(url,headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def auto_paginate(headers):
    base_url = "https://ehall.scnu.edu.cn/taskcenter/api/me/processes/doing?limit=10&start="
    page_number = 10

    while True:
        print(f"Processing page {page_number}")
        url = f"{base_url}{page_number}"
        page_content = fetch_page(url,headers)
        if page_content is None:
            break

        contents = extract_contents(page_content)
        print(contents)

        page_number += 10


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
    # account_input.send_keys('20211131028')
    account_input.send_keys('账号')
    password_input = driver.find_element(By.ID, 'password')
    # password_input.send_keys('Kixuan950827!')
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

    auto_paginate(headers)

    driver.quit()




login_and_wait()
