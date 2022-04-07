n = int(input())
cnt = 0
s = [int(i) for i in input().split()]
for i in s:
    if i > 0:
        cnt += 1
print(cnt)