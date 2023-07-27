from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建 ChromeOptions 对象，并设置无界面模式
chrome_options = Options()
chrome_options.add_argument('--headless')  # 启用无界面模式

# 创建 Chrome WebDriver，将 ChromeOptions 作为参数传递
browser = webdriver.Chrome(options=chrome_options)

browser.get('https://www.baidu.com')
print(browser.current_url)

browser.quit()  # 关闭浏览器
