# 循环/遍历: 取出所有元素的值

# 固定语法, for ... in ,,,:
# ...是变量
# 元组/数组/列表的循环相似
s1 = '回首向来萧瑟处'
for i in s1:
    print(i)

# range(开始值, 终止值, 步长)
for i in range(0, 11, 2):
    print(i)

for i in range(1,5):  # 配合序列生成器range()使用
    print(i)

# 字典
data = {'name': 'tom', 'sex': 'male', 'height': '185'}
for i in data:
    print(i)  # 只会取到键
print('\n')

for i in data: 
    print(data[i])
print('\n')  

for i in data:    
    print('{} : {}'.format(i, data[i]))


for i in range(len(s1)):
    print(i,s1[i])

a = ['abcdefg']
b = ['a','b','c','d','e']
c = '何妨吟啸且徐行'
print(a[0])
print(b[1])
print(c[5])
print(len(a), len(b), len(c))
# 语言只是一层皮, 真正核心的还是算法+数据结构

