# startPos 잡지 말고, M값과 큐에 있는 값이 같은지를 비교해서 break하는게 더 빠름

from collections import deque

cases = int(input())
countAry = []

for _ in range(cases):
    N, M = input().split()
    weightList = list(map(int, input().split()))
    weightQueue = deque()

    for i in range(int(N)):
        weightQueue.append(weightList[i])

    startPos = int(M)
    count = 0
    while True:
        if max(weightQueue) == weightQueue[0]:
            temp = weightQueue.popleft()
            count += 1
            if startPos == 0:
                break
            else:
                startPos -= 1

        elif max(weightQueue) > weightQueue[0]:
            temp = weightQueue.popleft()
            weightQueue.append(temp)
            startPos -= 1
            if startPos < 0 :
                startPos = len(weightQueue) - 1

    countAry.append(count)

for count in countAry:
    print(count)


