class DavidTao:
    # 类的专有方法
    # __init__: 构造函数, 在生成对象时调用
    def __init__(self, name, hobby):
        self.name = name  # 新增成员变量name并赋值
        self.hobby = hobby  # 新增成员变量hobby并赋值

    # __del__: 析构函数, 在释放对象时调用
    def __del__(self):
        print('哈哈, 你也想那个吗? 哦啊啊诶诶啊啊')    

# 给init方法传参: 用来初始化类的成员变量
dt = DavidTao('陶喆', '猛干大经理')
print(dt.name, dt.hobby)
