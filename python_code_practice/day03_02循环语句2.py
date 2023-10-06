# while循环
a = 1
while a < 5:
    print(a)
    a += 1

# 0-100求和
sum = 0
for i in range(0, 101):
    sum = sum + i
    i += 1
print(sum)

sum2 = 0
i = 0
while i < 101:
    sum2 = sum2 + i
    i += 1
print(sum2)

# break 终止当前循环
# break 跳过本次循环
b = 1
while b < 5:
    print(b)
    break

for i in range(5):
    if i == 2:
        continue
    print(i)
