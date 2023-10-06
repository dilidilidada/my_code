import random

random_list = random.sample(range(100), 10)
print(random_list)

for i in range(len(random_list)):
    for j in range(i+1, len(random_list)):
        if random_list[i] > random_list[j]:
            temp = random_list[j]
            random_list[j] = random_list[i]
            random_list[i] = temp

print(random_list)
