def xor(a, b):
    if a == b:
        print(0)
    else:
        print(1)

a, b = [int(i) for i in input().split()]
xor(a, b)