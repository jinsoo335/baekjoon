import sys, math

A, B, V = map(int, sys.stdin.readline().split())

dayCount = (V - B) / (A - B)
print(math.ceil(dayCount))

