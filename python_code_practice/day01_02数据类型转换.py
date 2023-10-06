# 数据类型的转换

a = 123
b = str(a)  # 整型转字符串
c = int(b)  # 字符串转整型, 字符串要为0-9
print(type(a), type(b), type(c))

s1 = '(1,2,3)'
s2 = '[1,2,3]'
s3 = '''{'username':'root'}'''
print(type(s1), type(s2), type(s3))

s11 = eval(s1)  # 根据内容格式自动匹配转换的数据类型 eval()
s22 = eval(s2)
s33 = eval(s3)
print(type(s11), type(s22), type(s33))

s4 = '123'
s5 = '123.12'
print(type(eval(s4)), type(eval(s5)))