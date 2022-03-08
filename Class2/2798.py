import sys

N, M = map(int, sys.stdin.readline().split())

numList = list(map(int, sys.stdin.readline().split()))

nearSol = 0

for i in range(len(numList)):
    for j in range(i + 1, len(numList)):
        for k in range(j + 1, len(numList)):
            temp = numList[i] + numList[j] + numList[k]

            if (nearSol < temp) and (temp <= M):
                nearSol = temp

print(nearSol)