import sys

N = int(input())

numArr = []
numCountArr = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    numArr.append(num)

    if num not in numCountArr:
        numCountArr[num] = 1
    else:
        numCountArr[num] += 1

numArr.sort()

print(round(sum(numArr) / N))
print(numArr[(N - 1) // 2])

keyArr = list(numCountArr.keys())
valueArr = list(numCountArr.values())
maxValue = max(valueArr)
indexArr = []

for i in range(len(valueArr)):
    if valueArr[i] == maxValue:
        indexArr.append(i)

if len(indexArr) == 1:
    print(keyArr[indexArr[0]])
else:
    manyNums = []
    for i in indexArr:
        manyNums.append(keyArr[i])
    manyNums.sort()
    print(manyNums[1])

print(numArr[-1] - numArr[0])