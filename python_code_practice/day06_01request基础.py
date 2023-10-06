# 登录的请求
# haimo登录
import requests

# 接口地址, 字符串格式 url
# 请求头 header
# 参数, 字典格式 json
# 请求方法 method
url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
# 用post方法去请求接口地址, 并且传递参数, 接收返回值
res = requests.post(url=url, json=data)
# res用于存放所有返回信息(响应头(http状态码), 返回值)
print(res.text)

