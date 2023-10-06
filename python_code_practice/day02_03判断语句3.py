level = [1, 6, 9, 13, 20, 30, 35, 85, 60, 99, 100, 200]
rookie = []
normal = []
master = []

for i in level:
    if i < 30:
        rookie.append(i)
    elif i >= 30 and i < 100:
        normal.append(i)
    else:
        master.append(i)
        
print('rookie:', rookie,'\n'
      'normal:', normal,'\n'
      'master:', master)