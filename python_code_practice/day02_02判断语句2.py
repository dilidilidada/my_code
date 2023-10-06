level = [1, 6, 9, 13, 20, 30, 35, 85, 60, 99, 100, 200]
rookie = []
normal = []
master = []
# print(len(level), type(len(level)))

j = 0
while (j < len(level)):
    if level[j] <30:
        rookie.append(level[j])
    elif level [j] >= 30 and level [j] < 100:
        normal.append(level[j])
    else:
        master.append(level[j])
    j = j+1

print('rookie:', rookie,'\n'
      'normal:', normal,'\n'
      'master:', master)

