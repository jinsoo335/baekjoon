# 설정할 수 있는 높이의 최댓값을 구하는 프로그램이기 때문에
# 단순히 if treeSum == M으로 반복문을 탈출하면 틀린다.
# 배열에 넣은 다음 최댓값을 뽑아내는 방식도 좋을 듯 하다

import sys

N, M = map(int, sys.stdin.readline().split())

treeList = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(treeList)
result = 0

while low <= high:
    mid = (low + high) // 2
    treeSum = 0
    treeSum = sum([i - mid if mid < i else 0 for i in treeList])

    if treeSum < M:
        high = mid - 1
    else:
        low = mid + 1
        result = mid
print(result)