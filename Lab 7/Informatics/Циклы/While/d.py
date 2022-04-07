n = int(input())
a = list()
for i in range(0, 100):
    a.append(2 ** i)
if n in a:
    print('YES')
else: print('NO')