a = int(input())
n = [int(i) for i in input().split()]
for i in n:
    if i % 2 == 0:
        print(i, end=' ')