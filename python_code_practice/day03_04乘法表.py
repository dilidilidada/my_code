# author:J1097888190
# date:2021.08.31

# ------------按输入输出对应乘法表
height = int(input("需要几几乘法表: "))

num_height = 1
while num_height <= height:
    print("1*" + str(num_height) + "=" + str(1 * num_height), end="\t")

    num_width = 1
    while num_width != num_height:
        print(str(num_width + 1) + "*" + str(num_height) + "=" + str((num_width + 1) * num_height), end="\t")
        num_width += 1

    num_height += 1

    print()


