import sys

N = int(sys.stdin.readline())

points = {}

for _ in range(N):
    key, value = map(int, sys.stdin.readline().split())

    if key in points:
        check = True
        for i in range(len(points[key])):
            if points[key][i] > value:
                points[key].insert(i, value)
                check = False
                break
        if check:
            points[key].append(value)
    else:
        points[key] = []
        points[key].append(value)

keys = list(points.keys())
keys.sort()

for i in keys:
    if len(points[i]) == 1:
        print(i, points[i][0])
    else:
        for j in range(len(points[i])):
            print(i, points[i][j])
