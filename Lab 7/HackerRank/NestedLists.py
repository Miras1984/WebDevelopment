if __name__ == '__main__':
    names = list()
    a = list()
    scores = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    minn = min(scores)
    minn2 = 100000000
    for i in scores:
        if i < minn2 and i != minn:
            minn2 = i
    for i in range(0, len(scores)):
        if scores[i] == minn2:
            a.append(names[i])
    a.sort()
    for i in a:
        print(i)
