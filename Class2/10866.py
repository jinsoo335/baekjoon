import sys
from collections import deque

N = int(sys.stdin.readline())
numDeq = deque()

for _ in range(N):
    temp = list(map(str, sys.stdin.readline().split()))

    if temp[0] == "push_front":
        numDeq.appendleft(temp[1])

    elif temp[0] == "push_back":
        numDeq.append(temp[1])

    elif temp[0] == "pop_front":
        if numDeq:
            print(numDeq.popleft())
        else:
            print(-1)

    elif temp[0] == "pop_back":
        if numDeq:
            print(numDeq.pop())
        else:
            print(-1)

    elif temp[0] == "size":
        print(len(numDeq))

    elif temp[0] == "empty":
        if numDeq:
            print(0)
        else:
            print(1)

    elif temp[0] == "front":
        if numDeq:
            print(numDeq[0])
        else:
            print(-1)

    elif temp[0] == "back":
        if numDeq:
            print(numDeq[-1])
        else:
            print(-1)
