a, b = int(input()), int(input())
c = str(a)

if len(c) == 4:
    cnt = 0
    for i in range(0, len(c) // 2):
        if c[i] == c[len(c) - i - 1]:
            cnt += 1
    if cnt == len(c) // 2:
        if b != 1:
            print('NO')
        else: print('YES')
elif b != 1:
    print('YES')
else:
    print('NO')
    
    
