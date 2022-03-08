import sys

N = int(sys.stdin.readline())

numList = []
for _ in range(N):
    numList.append(int(sys.stdin.readline()))

numList.sort()

for num in numList:
    print(num)
