# print(i, end=' ') 이거 쓰면 줄 안바뀌고 띄어쓰기로 바뀐다,...

import sys

N = int(sys.stdin.readline())

peopleList = []

for i in range(N):
    peopleList.append(list(map(int, sys.stdin.readline().split())))


count = 1
ranks = []

for i in range(N):
    count = 1
    for j in range(N):
        if i == j:
            continue

        if (peopleList[i][0] < peopleList[j][0]) and (peopleList[i][1] < peopleList[j][1]):
            count += 1

    ranks.append(count)

strRank = ""
for i in range(len(ranks)):
    strRank += str(ranks[i])

    if i != (len(ranks) - 1):
        strRank += " "

print(strRank)