import sys

N = int(sys.stdin.readline())

peopleDict = {}

for _ in range(N):
    temp = list(map(str, sys.stdin.readline().split()))

    if int(temp[0]) in peopleDict:
        peopleDict[int(temp[0])].append(temp[1])
    else:
        peopleDict[int(temp[0])] = []
        peopleDict[int(temp[0])].append(temp[1])


ages = list(peopleDict.keys())
ages.sort()

for age in ages:
    if len(peopleDict[int(age)]) == 1:
        print(age, peopleDict[age][0])
    else:
        for i in range(len(peopleDict[int(age)])):
            print(age, peopleDict[age][i])