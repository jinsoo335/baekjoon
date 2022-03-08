import sys

testCase = int(input())

peopleList = []
tempList = [i + 1 for i in range(14)]

peopleList.append(tempList)

for i in range(1, 15):
    tempList = [0 for _ in range(14)]
    for j in range(14):
        prevSum = 0
        for a in range(j + 1):
            prevSum += peopleList[i - 1][a]
        tempList[j] = prevSum
    peopleList.append(tempList)

solList = []

for _ in range(testCase):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    solList.append(peopleList[k][n - 1])
for sol in solList:
    print(sol)