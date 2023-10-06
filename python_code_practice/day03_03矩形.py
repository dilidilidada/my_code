# author:J1097888190
# date:2021.08.30

# ----------------输入长和宽,用*输出对应矩形
height = int(input("请输入高: "))
width = int(input("请输入宽: "))

num_height = 1
while num_height <= height:
    print("*",end="  ")

    num_width = 1
    while num_width < width:
        print("*",end="  ")
        num_width += 1

    num_height += 1
    print()
