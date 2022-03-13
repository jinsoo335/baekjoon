import sys

N, K = map(int, sys.stdin.readline().split())

def binary(n, k):
    if (n < 2) or (n == k):
        return 1
    if (n - k) == 0:
        return 1
    if k == 0:
        return 1
    if (k == 1) or ((n - k) == 1):
        return n

    return binary(n - 1, k - 1) + binary(n - 1, k)


print(binary(N, K))