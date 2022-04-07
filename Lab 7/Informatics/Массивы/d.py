a = int(input())
cnt = 0
s = [int(i) for i in input().split()]
for i in range(0, len(s) - 1):
    if s[i + 1] > s[i]:
        cnt += 1
print(cnt)