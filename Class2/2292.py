# 1   6   12  18  24

N = int(input())

count = 1
num = 1

while num < N:
    num += count * 6
    count += 1

print(count)


