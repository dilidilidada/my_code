import requests

# 封装/二次开发
class httpRequest():
    # 静态方法: 直接用, 不用实例化
    @staticmethod
    def request(url, json=None, headers=None, method='POST'):
        if method.lower() == 'post':
            res = requests.post(url=url, json=json, headers=headers)
        else:
            res = requests.get(url=url, json=json, headers=headers)
        return res
    
 # 防止被导入时运行下面的代码, 下面的代码都是测试代码   
if __name__ == '__main__':
    url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
    data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
    r = httpRequest.request(url=url, method='post', json=data)
    print(r.text)
    print(r)

