# from collections import deque 잊지말자..

import sys
from collections import deque

N = int(sys.stdin.readline())
numQue = deque()

for _ in range(N):
    temp = list(map(str, sys.stdin.readline().split()))

    if temp[0] == "push":
        numQue.append(temp[1])

    elif temp[0] == "pop":
        if numQue:
            print(numQue.popleft())
        else:
            print(-1)

    elif temp[0] == "size":
        print(len(numQue))

    elif temp[0] == "empty":
        if numQue:
            print(0)
        else:
            print(1)

    elif temp[0] == "front":
        if numQue:
            print(numQue[0])
        else:
            print(-1)

    elif temp[0] == "back":
        if numQue:
            print(numQue[-1])
        else:
            print(-1)