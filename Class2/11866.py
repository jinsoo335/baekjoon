import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

print("<", end="")

numQue = deque()

for i in range(1, N + 1):
    numQue.append(i)

while len(numQue) > 1:
    for i in range(K - 1):
        numQue.append(numQue.popleft())
    print(f"{numQue.popleft()}, ", end="")
print(numQue.popleft(), end=">")