a = int(input())
s = [int(i) for i in input().split()]
cnt = 0
for i in range(1, len(s) - 1):
    if s[i - 1] < s[i] and s[i + 1] < s[i]:
        cnt += 1
print(cnt)