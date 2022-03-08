N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
isAry = []

for i in range(M):
    low = 0
    high = len(A) - 1
    check = False

    while low <= high:
        mid = (low + high) // 2
        if A[mid] < B[i]:
            low = mid + 1
        elif A[mid] == B[i]:
            check = True
            isAry.append(1)
            break
        else:
            high = mid - 1

    if not check:
        isAry.append(0)

for sign in isAry:
    print(sign)


