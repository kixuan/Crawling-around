import urllib.parse
import urllib.request

# 获取hello！xxz，会传送到运行结果的word --POST模拟表单获取
#  urlencode 方法来将参数字典转化为字符串
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())