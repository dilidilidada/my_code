# 判断语句
'''
# 例1
age = int(input('请输入年龄:'))
if age < 12:
    print('baby')
elif age >= 12 and age < 18:
    print('teen')
else:
    print('adlut')

# 例2
name = input('请输入姓名:')
if name == '张三':
    print('true')
else:
    print('false')
    '''

# 例3
name = (input('请输入姓名:'))
if '马冬梅' in name:  # 不在 not in, 条件可用and/or连接
    print('什么冬梅?马什么梅?马冬什么?')
else:
    print('钝角')
