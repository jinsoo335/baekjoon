import sys

while True:
    numList = list(map(int, sys.stdin.readline().split()))
    numList.sort()

    if sum(numList) == 0:
        break

    if numList[0] * numList[0] + numList[1] * numList[1] == numList[2] * numList[2]:
        print("right")
    else:
        print("wrong")

