import math

M, N = input().split()

M = int(M)
N = int(N)

if M == 1:
    M = 2

for i in range(M, N + 1):
    check = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)
