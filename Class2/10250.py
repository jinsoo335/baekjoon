import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    count = 101
    for i in range(1, H * W + 1):
        if i == N:
            break
        count += 100

        if count > ((H + 1) * 100):
            count = count - H * 100 + 1

    print(count)

