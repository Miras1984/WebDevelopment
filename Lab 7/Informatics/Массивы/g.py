a = int(input())
s = [int(i) for i in input().split()]

q = list()
for i in range(len(s) - 1, -1, -1):
    q.append(s[i])
for i in q:
    print(i, end=' ')
