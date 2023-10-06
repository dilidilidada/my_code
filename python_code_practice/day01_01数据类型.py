print ('hello world')
# name = input('请输入:')
# print(name)

# 数据类型 
# 整型
a = 123

# 浮点数
b = 3.1415926

# 空值/None
c = None

# 布尔/bool
t = True
f = False

# 字符串
s1 = 'abcd'
s2 = '1234'
s3 = '甲乙丙丁'
s = s1 + s2  # 字符串拼接format()
print(s)

ss = '赵钱孙李{}{}{}{}'.format(s3,s2,c,b)
print(ss)

index = ss.find('甲')  # 查找索引find(), 找不到返回-1 
print(index)

print('len=',len(ss))  # 字符串长度len()

ss2 = ss.replace('甲乙丙丁','丁丁丁丁')  # 替换字符串 replace()
print(ss2)

ss3 = ss.split('1234')  # 分割字符串,返回值是一个列表 split()
print(ss3)


# 元组/tuple, 元组的元素可以是任意类型数据
# 取值: 根据下标取值
d = (1,2,3,a,b,True,None,'lol',(1,2,3,4))
print(d[7],d[-4])  # 负数从右往左取

# 列表/list, 可变的元组: 取值/删除/添加/修改/排序 
e = [1,2,3,a,b,True,'lol',None]
print(e)
e[4] = 'oiiii'  # 修改
print(e)

e.append("water")  # 在末尾添加 append()
print(e)

e.insert(9, 'fire')  # 插入 insert(下标, 值)
print(e)

e.remove('lol')  # 删除 remove(元素的值)
print(e)

e1 = [555,78,5,15,0,5698]
e1.sort()  # 排序, 从小到大 sort()
print(e1)

# 字典/dict
g = {'user':"root", 'password':'123456'}  # value可以是任意数据类型

g1 = g['user']  # 获取值, 取不到会报错
print(g1)
g2 = g.get('user')  # 获取值, 取不到会返回空值
print(g2)

g['sex'] = 'male'  # 新增
print(g)

g['user'] = 'root1'  # 修改
print(g)
g.update({'user':'root2'})  # 修改
print(g)

del g['sex']  # 删除
print(g)

# 查看数据类型 type()
print(type(a))

# 获取内存地址
print(id(a))

# 快速注释 ctrl+?
# / 除法的结果是float类型
# 赋值的本质是把值的内存地址保存