import requests
from utils.LogTools import my_logger

# 封装/二次开发
class HttpRequest():
    # 静态方法@staticmethod: 直接用, 不用实例化
    @staticmethod
    def request(url, json=None, headers=None, method='POST'):
        # 请求之前打印请求的接口信息
        my_logger.info("==================================")
        my_logger.info("接口地址：{}".format(url))
        my_logger.info("接口参数：{}".format(json))
        my_logger.info("接口方法：{}".format(method))
        my_logger.info("接口请求头：{}".format(headers))
        
        if method.lower() == 'post':
            res = requests.post(url=url, json=json, headers=headers)
        else:
            res = requests.get(url=url, json=json, headers=headers)
        
        
        # 请求结束打印响应的信息
        my_logger.info("接口返回值：{}".format(res.text))
        my_logger.info("接口状态码：{}".format(res.status_code))
        my_logger.info("接口结果码：{}".format(res.json()["code"]))
        my_logger.info("==================================")

        return res
    
# 更好的写法: 打印的功能放到__init__()和__del__()当中    
# 保持request方法的整洁, 参数传给HttpRequestV2()类
class HttpRequestV2():
    def __init__(self, url, data={}, header={}, method='post'):
        self.url = url
        self.data = data
        self.header = header
        self.method = method
        
        my_logger.info("==================================")
        my_logger.info("接口地址：{}".format(url))
        my_logger.info("接口参数：{}".format(data))
        my_logger.info("接口方法：{}".format(method))
        my_logger.info("接口请求头：{}".format(header))

    def request(self):
        if self.method.lower() == "post":
            self.res = requests.post(url=self.url, json=self.data, headers=self.header)
        else:
            self.res = requests.get(url=self.url, json=self.data, headers=self.header)

        return self.res
        
    def __del__(self):
        my_logger.info("接口返回值：{}".format(self.res.text))
        my_logger.info("接口状态码：{}".format(self.res.status_code))
        my_logger.info("接口结果码：{}".format(self.res.json()["code"]))
        my_logger.info("==================================")

 # 防止被导入时运行下面的代码, 下面的代码都是测试代码   
if __name__ == '__main__':
    url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
    data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
    r = HttpRequest.request(url=url, method='post', json=data)
    print(r.text)

