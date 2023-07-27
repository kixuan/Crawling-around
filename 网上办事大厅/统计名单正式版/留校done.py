import sys
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def login_and_wait():
    url = "https://ehall.scnu.edu.cn/taskcenter/workflow/done"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)

    # 登录
    account_input = driver.find_element(By.ID, 'account')
    account_input.send_keys('账号')
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('密码')

    login_button = driver.find_element(By.CLASS_NAME, 'btn.btn-primary.btn-block.auth-login-btn')
    login_button.click()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[-1])
    confirm_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span.login-check-comfirm a.btn.btn-danger'))
    )
    confirm_button.click()
    time.sleep(2)

    auto_paginate(driver)

    driver.quit()


def auto_paginate(driver):
    current_page = 1
    while True:
        # 处理当前页的内容
        page_content = driver.page_source
        click_link(page_content, driver)

        # 在这里判断是否还有下一页
        try:
            next_a = driver.find_element(By.XPATH, "//div[@class='fy_num current']/following-sibling::div//a")
            # 使用JavaScript点击下一页按钮
            driver.execute_script("arguments[0].click();", next_a)
            time.sleep(1)
            current_page += 1
        except NoSuchElementException:
            break


def click_link(page_content, driver):
    # 解析页面内容，点击链接
    soup = BeautifulSoup(page_content, 'html.parser')
    target_items = soup.select('.sx_conter_item')

    for item in target_items:
        link = item.select_one('.sx_pa a')
        link_text = link.get_text()

        # 替换成范围内最后一个数据
        if link_text == "学生离校外出申请_xxx_计算机学院_广州校区石牌校园_[佛山市]_[顺德区]_市外(省内)__2022级":
            print("已提取全部数据")
            sys.exit()

        if link and link_text.startswith("寒暑假留校申请") and link_text.endswith("2021级") and link:
            link_url = link['href']
            print(link_text)

            # 在新窗口中打开链接
            driver.execute_script(f"window.open('{link_url}', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])

            # 等待新页面加载完成
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

            # 提取数据
            table_data = extract_table_data(driver.page_source)
            if table_data:
                save_data_to_file(table_data)

            # 关闭新窗口，回到原始页面
            driver.close()
            driver.switch_to.window(driver.window_handles[0])


def extract_table_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find('table')
    if table:
        tbody = table.find('tbody')
        if tbody:
            tr_tags = tbody.find_all('tr')
            # 指定需要提取的tr索引
            target_indexes = [4, 5, 6, 7, 10, 12,13]
            data = []
            for index, tr in enumerate(tr_tags):
                if index in target_indexes:
                    td_tags = tr.find_all('td')
                    if index == 4 or index==13:
                        tr_data = [td_tags[1].get_text(), td_tags[3].get_text()]
                    elif index == 5:
                        tr_data = [td_tags[3].get_text()]
                    elif index == 7 or index == 6 or index == 12:
                        tr_data = [td_tags[1].get_text()]
                    elif index == 10:
                        tr_data = [td_tags[1].get_text(), td_tags[2].get_text(), td_tags[3].get_text(),
                                   td_tags[4].get_text()]
                    data.append(tr_data)
            return data


# 保存数据到文件
def save_data_to_file(data):
    with open('2021留校申请.txt', 'a', encoding='utf-8') as file:
        count = 0
        for item in data:
            file.write('\t'.join(item))
            count += 1
            if count % 7 == 0:
                file.write('\n')
            else:
                file.write('\t')


# 调用登录函数和等待函数
login_and_wait()
