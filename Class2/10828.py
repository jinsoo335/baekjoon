import sys

N = int(sys.stdin.readline())

intNums = []

for _ in range(N):
    temp = list(map(str, sys.stdin.readline().split()))

    if temp[0] == "push":
        intNums.append(temp[1])
    elif temp[0] == "top":
        if intNums:
            print(intNums[-1])
        else:
            print(-1)
    elif temp[0] == "size":
        print(len(intNums))
    elif temp[0] == "empty":
        if intNums:
            print(0)
        else:
            print(1)
    elif temp[0] == "pop":
        if intNums:
            print(intNums.pop())
        else:
            print(-1)

