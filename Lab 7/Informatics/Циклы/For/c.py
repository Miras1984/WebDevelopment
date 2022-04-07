qq = list()
for j in range(0, 200):
    qq.append(j ** 2)

a, b = int(input()), int(input())
for i in range(a, b):
    if i in qq:
        print(i)