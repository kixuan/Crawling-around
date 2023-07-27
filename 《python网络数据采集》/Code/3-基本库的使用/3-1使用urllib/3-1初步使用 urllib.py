import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# 输出返回类型
print(type(response))
# 输出返回结果的状态码
print(response.status)
# 输出响应头的各数据
print(response.getheaders())
# 获取了响应头中的 Server 值，结果是 nginx，意思是服务器是用 Nginx 搭建的。
print(response.getheader('Server'))
# 输出读取信息——网页的源代码
# print(response.read().decode('utf-8'))