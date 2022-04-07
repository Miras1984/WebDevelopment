if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    arr.reverse()

    for i in arr:
        if i < max(arr):
            print(i)
            break
