# import random

# random_list = random.sample(range(100), 10)
# print(sorted(random_list))  # sort方法适用于list, sorted适用于所有可迭代的对象
# random_list.sort()
# print(random_list)

a = [3, 13, 22, 88, 33, 13, 69, 95, 88, 95]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            print(i, j)
print(len(a))

