# 类: 具有相同属性的方法集合体
# class 类名():
# ()可省略

class realMan():
    # 定义基本属性
    name = '蔡徐坤'
    sex = '女'

    # 双下划线定义私有属性
    __fav = '唱跳rap篮球'

    # 定义构造方法
    # 类方法必须包含self参数(按照惯例命名为self)且为第一个参数
    # 实例化类时会自动调用__init__()构造方法
    # __init__()可以有参数, 参数通过__init__传递到类的实例化操作上
    # 可以返回值
    def sing(self, sth='鸡'):
        print('{}你太美'.format(sth))
        print('我是{}'.format(self.name))
        print('我爱{}'.format(self.__fav))
        self.rap()
        self.hate = '讨厌小黑子'  # self.xxx: 方法中新增类中不存在的变量, 若存在则修改

    def rap(self):
        print('多一眼看一眼就会爆炸')

# 实例化
man = realMan()
man.sing()
man.sing('叽叽叽叽')
print(realMan.name, '性别', realMan.sex, man.name, man.hate)


