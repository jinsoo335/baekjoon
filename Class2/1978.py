import math

N = int(input())

numArr = list(map(int, input().split()))

count = 0
maxNum = 1000

for num in numArr:
    check = True
    if num != 1:
        for i in range(2, int(math.sqrt(maxNum)) - 1):
            if num % i == 0 and num != i:
                check = False
                break
    else:
        check = False

    if check:
        count += 1

print(count)