import sys

K = int(sys.stdin.readline())

stack = []
for _ in range(K):
    temp = int(sys.stdin.readline())

    if temp != 0:
        stack.append(temp)
    elif temp == 0 and stack:
        stack.pop()

print(sum(stack))