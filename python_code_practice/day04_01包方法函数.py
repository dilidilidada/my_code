# 自定义方法
def add(a, b):  # 实参, 可以是任意数据类型, 可为空
    return a + b

c = add(50, 60)  # 调用方法
print(c)

def add2(a=50, b=20):  # 无形参则为默认值
    return a + b

c2 = add2()
c3 = add2(70, 80)
c4 = add2(a=80)
print(c2, c3, c4)
