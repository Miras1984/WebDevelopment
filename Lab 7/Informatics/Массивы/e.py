a = int(input())
s = [int(i) for i in input().split()]
f = False

for i in range(0, len(s) - 1):
    if s[i] * s[i+1] > 0:
        f = True
        break
if f:
    print('YES')
else:
    print('NO')