if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    scores = list()
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = [float(i) for i in scores]
        student_marks[name] = scores
    query_name = input()
    a = sum(student_marks[query_name]) / len(scores)
    print('%.2f' % a)
