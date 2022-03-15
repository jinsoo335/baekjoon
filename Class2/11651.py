import sys

N = int(sys.stdin.readline())

numDict = {}

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    if y in numDict:
        check = True
        for i in range(len(numDict[y])):
            if numDict[y][i] > x:
                numDict[y].insert(i, x)
                check = False
                break
        if check:
            numDict[y].append(x)
    else:
        numDict[y] = []
        numDict[y].append(x)

numKeys = list(numDict.keys())
numKeys.sort()

for num in numKeys:
    if len(numDict[num]) == 1:
        print(numDict[num][0], num)
    else:
        for i in range(len(numDict[num])):
            print(numDict[num][i], num)
