import os
import time
from selenium import webdriver
import pickle

# 大麦网首页
damai_url = 'http://damai.cn/'
# 登录
login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
# 抢票页面
target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_6.59cb23e11qvCAL&id=701301817719'


class Concert:
    """初始化加载"""

    def __init__(self):
        self.status = 0
        self.login_method = 1
        self.driver = webdriver.Chrome()

    def set_cookies(self):
        self.driver.get(login_url)
        print("###请扫码登陆")
        time.sleep(15)
        print("###登录成功")
        pickle.dump(self.driver.get_cookies(), open('cookies.pkl', 'wb'))
        print("###cookies保存成功")
        self.driver.get(target_url)

    def get_cookie(self):
        cookies = pickle.load(open('cookies.pkl', 'rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain': '.damai.cn',
                'name': cookie.get('name'),
                'value': cookie.get('value')
            }
            self.driver.add_cookie(cookie_dict)
        print("载入cookies成功")

    def login(self):
        if self.login_method == 0:
            self.driver.get(login_url)
        elif self.login_method == 1:
            if not os.path.exists('cookies.pkl'):
                self.set_cookies()
            else:
                self.driver.get(target_url)
                self.get_cookie()

    def enter_concert(self):
        print("打开浏览器")
        self.login()
        self.driver.refresh()
        self.status = 2
        print("登录成功")

    def choose_ticket(self):
        if self.status == 2:
            print('=' * 30)
            print("选择")
            while self.driver.title.find("确认订单") == 1:
                buybutton = self.driver.find_element_by_class_name("buybtn").text
                if buybutton == '提交缺货登记':
                    self.driver.refresh()
                elif buybutton == '立即购买':
                    self.driver.find_element_by_class_name("buybtn").click()
                else:
                    self.status = 100
                title = self.driver.title


if __name__ == '__main__':
    con = Concert()
    con.enter_concert();
